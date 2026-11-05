#!/usr/bin/env python3
"""Who Answers collector: one daily snapshot of each source and one ledger line per source per run.

Sources:
  charlotin  Damien Charlotin's AI Hallucination Cases CSV  -> data/charlotin-YYYYMMDD.csv (first fetch of the day wins)
  aiid       AI Incident Database weekly backup (incidents.csv and the classification tables, streamed out of the
             tar.bz2 without writing the archive to disk)          -> data/aiid/incidents.csv (+ dated copy)
Ledger: data/ledger.jsonl, append-only: {"ts","source","file","sha256_16","rows","prev","added","removed", ...}.
Run: python3 lab/whoanswers/collect.py [--force] [--only charlotin|aiid|alt|nope]. Exit 1 if any source failed.
  alt        AI Lawsuit Tracker dataset (ailawsuittracker.com/data, CC BY 4.0; 331 cases on 03.11, category agentic_ai,
             wrongful_death...)                                     -> data/alt/ai-lawsuits-YYYYMMDD.csv, key = slug
  nope       NOPE AI incident tracker export (nope.net/incidents, CC BY 4.0; 1096 cases on 03.11, with Outcome Type and
             Outcome Status per case)                               -> data/nope/export-YYYYMMDD.csv.gz, key = ID
             Both are stored only when the body changed since the last stored file (NOPE is ~12 MB).
Credit when published: AI Lawsuit Tracker (ailawsuittracker.com); NOPE (nope.net). Use is research and citation, not
model training (ailawsuittracker's terms forbid ML training without a licence).
"""
import csv, datetime as dt, hashlib, io, json, os, re, sys, tarfile, urllib.request, collections

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
LEDGER = os.path.join(DATA, 'ledger.jsonl')
CHARLOTIN_URL = 'https://www.damiencharlotin.com/hallucinations/hallucinations/download.csv'
AIID_PAGE = 'https://incidentdatabase.ai/research/snapshots/'
UA = 'errata-whoanswers-collector/1 (AI agent; errata@agentmail.to; one fetch a day)'
ALT_URL = 'https://ailawsuittracker.com/data/ai-lawsuits.csv'
NOPE_URL = 'https://nope.net/incidents/export.csv'
TODAY = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d')


def get(url, timeout=120):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return urllib.request.urlopen(req, timeout=timeout)


def sha16(b):
    return hashlib.sha256(b).hexdigest()[:16]


def last_rows(source):
    """(ts, rows) of the newest ledger line for source that carried a row count, or (None, None)."""
    if not os.path.exists(LEDGER):
        return None, None
    ts = n = None
    for line in open(LEDGER):
        r = json.loads(line)
        if r.get('source') == source and r.get('rows') is not None:
            ts, n = r['ts'], r['rows']
    return ts, n


def log(row):
    row = dict(ts=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), **row)
    # absent is not zero: a source that shrinks is logged as a warning, not as a quiet day (Pulse lesson, 04.11)
    if row.get('rows') is not None:
        _, prev_n = last_rows(row['source'])
        if prev_n and row['rows'] < 0.95 * prev_n:
            row['warn'] = f"rows fell {prev_n} -> {row['rows']}: check the source before counting"
    with open(LEDGER, 'a') as f:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
    print(json.dumps(row, ensure_ascii=False))


def charlotin_key(r):
    return (r['Case Name'].strip(), r['Court'].strip(), r['Date'].strip())


def collect_charlotin(force=False):
    out = os.path.join(DATA, f'charlotin-{TODAY}.csv')
    body = get(CHARLOTIN_URL).read()
    # 05.11: the source added a leading case_id column; check the key columns, not the first bytes
    head = next(csv.reader(io.StringIO(body[:2000].decode('utf-8', 'replace').splitlines()[0])), [])
    if not {'Case Name', 'Court', 'Date'} <= set(head):
        raise RuntimeError(f'key columns missing; first bytes {body[:40]!r}')
    rows = list(csv.DictReader(io.StringIO(body.decode('utf-8'))))
    snaps = sorted(f for f in os.listdir(DATA) if re.fullmatch(r'charlotin-\d{8}\.csv', f))
    note = {}
    if os.path.exists(out) and not force:
        # the day's file is the record: report its rows and hash; the fresh body only tells whether the source moved today
        old = open(out, 'rb').read()
        note['kept_first_fetch_of_day'] = True
        note['intraday_changed'] = sha16(old) != sha16(body)
        note['live_rows'] = len(rows)
        body = old
        rows = list(csv.DictReader(io.StringIO(body.decode('utf-8'))))
    else:
        open(out, 'wb').write(body)
    prev_candidates = [f for f in snaps if f < os.path.basename(out)]
    prev = prev_candidates[-1] if prev_candidates else None
    added = removed = None
    if prev:
        pk = collections.Counter(charlotin_key(r) for r in csv.DictReader(open(os.path.join(DATA, prev), encoding='utf-8')))
        nk = collections.Counter(charlotin_key(r) for r in rows)
        added = sum((nk - pk).values()); removed = sum((pk - nk).values())
    log(dict(source='charlotin', file=os.path.basename(out), sha256_16=sha16(body), rows=len(rows), prev=prev,
             added=added, removed=removed, **note))


def collect_aiid(force=False):
    adir = os.path.join(DATA, 'aiid'); os.makedirs(adir, exist_ok=True)
    marker = os.path.join(adir, 'CURRENT')
    page = get(AIID_PAGE).read().decode('utf-8', 'replace')
    urls = sorted(set(re.findall(r'https://[^"\'<> ]+/backup-(\d{14})\.tar\.bz2', page)))
    if not urls:
        raise RuntimeError('no backup-*.tar.bz2 link on the snapshots page')
    stamp = urls[-1]
    url = re.search(r'https://[^"\'<> ]+/backup-' + stamp + r'\.tar\.bz2', page).group(0)
    current = open(marker).read().strip() if os.path.exists(marker) else None
    if current == stamp and not force:
        log(dict(source='aiid', stamp=stamp, unchanged=True, note='newest backup already on disk'))
        return
    want = {'incidents.csv', 'classifications_CSETv1.csv', 'classifications_MIT.csv'}
    prev_ids = set()
    if os.path.exists(os.path.join(adir, 'incidents.csv')):
        prev_ids = {r['incident_id'] for r in csv.DictReader(open(os.path.join(adir, 'incidents.csv'), encoding='utf-8'))}
    got = {}
    with get(url, timeout=600) as resp, tarfile.open(fileobj=resp, mode='r|bz2') as tar:
        for m in tar:
            name = os.path.basename(m.name)
            if m.isfile() and name in want:
                got[name] = tar.extractfile(m).read()
            if len(got) == len(want):
                break
    if 'incidents.csv' not in got:
        raise RuntimeError(f'incidents.csv not in backup {stamp}; got {sorted(got)}')
    for name, b in got.items():
        open(os.path.join(adir, name), 'wb').write(b)
    open(os.path.join(adir, f'incidents-{stamp[:8]}.csv'), 'wb').write(got['incidents.csv'])
    ids = {r['incident_id'] for r in csv.DictReader(io.StringIO(got['incidents.csv'].decode('utf-8')))}
    open(marker, 'w').write(stamp + '\n')
    log(dict(source='aiid', stamp=stamp, prev=current, file=f'incidents-{stamp[:8]}.csv', sha256_16=sha16(got['incidents.csv']),
             rows=len(ids), added=len(ids - prev_ids) if prev_ids else None, removed=len(prev_ids - ids) if prev_ids else None,
             added_ids=sorted(ids - prev_ids, key=int)[:50] if prev_ids else None, tables=sorted(got)))


def collect_csv(name, url, key, first, gz=False):
    """Generic CSV tracker: store a dated copy when the body changed, ledger rows/added/removed by key column."""
    import gzip
    d = os.path.join(DATA, name); os.makedirs(d, exist_ok=True)
    body = get(url).read()
    if not body.startswith(first):
        raise RuntimeError(f'unexpected first bytes {body[:40]!r}')
    rows = list(csv.DictReader(io.StringIO(body.decode('utf-8-sig'))))
    ext = '.csv.gz' if gz else '.csv'
    snaps = sorted(f for f in os.listdir(d) if f.endswith(ext))
    prev = snaps[-1] if snaps else None
    old = None
    if prev:
        raw = open(os.path.join(d, prev), 'rb').read()
        old = gzip.decompress(raw) if gz else raw
    if old is not None and sha16(old) == sha16(body):
        log(dict(source=name, unchanged=True, file=prev, sha256_16=sha16(body), rows=len(rows)))
        return
    base = os.path.basename(url).rsplit('.', 1)[0]
    out = f'{base}-{TODAY}{ext}'
    open(os.path.join(d, out), 'wb').write(gzip.compress(body) if gz else body)
    added = removed = added_keys = None
    if old is not None:
        pk = {r[key] for r in csv.DictReader(io.StringIO(old.decode('utf-8-sig')))}
        nk = {r[key] for r in rows}
        added, removed, added_keys = len(nk - pk), len(pk - nk), sorted(nk - pk)[:50]
    log(dict(source=name, file=out, sha256_16=sha16(body), rows=len(rows), prev=prev, added=added, removed=removed,
             added_keys=added_keys))


def collect_alt(force=False):
    collect_csv('alt', ALT_URL, 'slug', b'slug,case_name,')


def collect_nope(force=False):
    collect_csv('nope', NOPE_URL, 'ID', b'ID,Name,Summary,', gz=True)


if __name__ == '__main__':
    force = '--force' in sys.argv
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
    rc = 0
    now = dt.datetime.now(dt.timezone.utc)
    for name in ('charlotin', 'aiid', 'alt', 'nope'):
        ts, _ = last_rows(name)
        if ts and now - dt.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=dt.timezone.utc) > dt.timedelta(days=3):
            log(dict(source=name, warn=f'no row count since {ts}: source silent for >3 days'))
    for name, fn in (('charlotin', collect_charlotin), ('aiid', collect_aiid), ('alt', collect_alt), ('nope', collect_nope)):
        if only and only != name:
            continue
        try:
            fn(force)
        except Exception as e:  # one failing source must not hide the other
            rc = 1
            log(dict(source=name, error=f'{type(e).__name__}: {e}'[:300]))
    sys.exit(rc)
