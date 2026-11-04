"""Build the blind packet for coder 2: AIID text + local source files per row; no row notes, no coder-1 codes.
Run from the repo root: python3 notes/awareness-blind/build_packet.py > notes/awareness-blind/packet.txt"""
import json, os, re, csv, glob, sys
csv.field_size_limit(10**9)
AIID = os.path.expanduser('~/work/lab/whoanswers/data/aiid/incidents-20261102.csv')
inc = {r['incident_id']: r for r in csv.DictReader(open(AIID))}
rows = [json.loads(l) for l in open('rows/aiid_agents.jsonl')]
scope = [r for r in rows if r['unit_type'] == 'event' and r['harmed'] != 'operator-self']
for r in scope:
    a = r['event_id'].split('-')[1]
    fs = sorted(f for f in glob.glob('sources/*') if not f.endswith('.sha256')
                and re.search(r'(^|-)' + a + r'(-|\.)', os.path.basename(f)))
    i = inc.get(a, {})
    print(f'\n######## ROW {r["event_id"]}' + ('' if fs else '  [aiid-only]'))
    print('AIID title:', i.get('title', 'NOT IN SNAPSHOT'))
    print('AIID description:', i.get('description', ''))
    print('AIID harmed or nearly harmed:', i.get('Alleged harmed or nearly harmed parties', ''))
    for f in fs:
        print(f'\n--- source file {os.path.basename(f)}\n' + open(f, errors='replace').read())
print(f'\n# {len(scope)} rows', file=sys.stderr)
