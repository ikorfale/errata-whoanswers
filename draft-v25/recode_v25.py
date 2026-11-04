"""v24 -> v25 recode: voluntary consequences classed self-only in voice_of_record_113456.py get status self-reported.
Reads aiid_agents_v20rows.jsonl, writes aiid_agents_v25rows.jsonl (input untouched), prints every change."""
import json
from voice_of_record_113456 import CLS
n = 0
with open('aiid_agents_v25rows.jsonl', 'w') as out:
    for l in open('aiid_agents_v20rows.jsonl'):
        r = json.loads(l)
        for c in r['consequences'] or []:
            if c.get('mode') == 'voluntary' and CLS[(r['event_id'][:9], c['kind'])] == 'self-only' and c['status'] != 'self-reported':
                print(r['event_id'], c['party'], c['kind'], c['status'], '-> self-reported'); c['status'] = 'self-reported'; n += 1
        r['scheme'] = 'v25'
        out.write(json.dumps(r, ensure_ascii=False) + '\n')
print('changed', n)
