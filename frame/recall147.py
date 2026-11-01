"""Recall check (#598): the 147 rows picked by either rule (51 'agent' word + 96 ACTION outside them).
Stage 1 prints snippets (title + first 250 chars); stage 2 prints full descriptions. Usage: recall147.py snip|full [from] [to]"""
import json, csv, sys
csv.field_size_limit(10**8)
L = [json.loads(l) for l in open('frame_labels.jsonl')]
cand = {json.loads(l)['incident_id'] for l in open('agent_candidates.jsonl')}
act = {x['id'] for x in L if x['label'] == 'ACTION'}
ids = sorted(cand | act, key=int)
rows = {r['incident_id']: r for r in csv.DictReader(open('data/aiid/incidents.csv'))}
mode = sys.argv[1]; a = int(sys.argv[2]) if len(sys.argv) > 2 else 0; b = int(sys.argv[3]) if len(sys.argv) > 3 else len(ids)
if mode == 'ids': print(len(ids), len(cand), len(act), len(cand & act)); sys.exit()
for i, k in enumerate(ids[a:b], a):
    r = rows[k]; d = ' '.join(r['description'].split())
    src = ('W' if k in cand else '') + ('A' if k in act else '')
    print(f"[{i}] {k} {src} {r['date']} | {r['title']}\n    {d[:250] if mode=='snip' else d}")
