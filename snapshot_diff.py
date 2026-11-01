"""Diff two Charlotin snapshots: rows added/removed by key (Case Name, Court, Date), fields changed on kept rows, tool-named share by year."""
import csv, sys, hashlib, collections
A, B = sys.argv[1], sys.argv[2]
def load(f):
    print(f, 'sha256_16', hashlib.sha256(open(f, 'rb').read()).hexdigest()[:16])
    R = list(csv.DictReader(open(f, encoding='utf-8')))
    K = collections.Counter((r['Case Name'].strip(), r['Court'].strip(), r['Date'].strip()) for r in R)
    return R, {(r['Case Name'].strip(), r['Court'].strip(), r['Date'].strip()): r for r in R}, K
ra, a, ka = load(A); rb, b, kb = load(B)
print('rows', len(ra), len(rb), '| unique keys', len(a), len(b), '| duplicate keys', sum(v > 1 for v in ka.values()), sum(v > 1 for v in kb.values()))
add, rem = sorted(set(b) - set(a)), sorted(set(a) - set(b))
print('added', len(add), 'removed', len(rem))
for k in add[:10]: print(' +', k)
for k in rem[:10]: print(' -', k)
ch = collections.Counter(); ex = []
for k in set(a) & set(b):
    for f in a[k]:
        if a[k][f] != b[k].get(f): ch[f] += 1; ex.append((k, f, a[k][f][:60], b[k].get(f, '')[:60]))
print('changed fields on kept rows', dict(ch))
for e in ex[:10]: print(' ~', e)
named = lambda r: r['AI Tool'].strip().lower() not in ('implied', 'unidentified', '')
for R, n in ((ra, 'A'), (rb, 'B')):
    by = collections.defaultdict(lambda: [0, 0])
    for r in R:
        y = r['Date'][:4] or '?'; by[y][0] += named(r); by[y][1] += 1
    print(n, ' '.join(f'{y}:{k}/{t}' for y, (k, t) in sorted(by.items())))
