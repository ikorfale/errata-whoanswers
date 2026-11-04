"""v24 -> v25 recode: voluntary consequences classed self-only in voice_of_record_113456.py get status self-reported.
Reads the published v24 rows ../rows/aiid_agents.jsonl (input untouched), writes aiid_agents_v25rows.jsonl, prints every
change. 04.11 ~18:00Z: the first draft read a stale v20-era working copy and lost date_event on 33 rows, the 1649 check
and 1441's recode; this version starts from the published rows. Round-2 edit carried: 1700's src with Adkins' verbatim words."""
import json
from voice_of_record_113456 import cls
SRC_1700 = ('Adkins statement via Reuters 2026-09-18, verbatim and attributed (also BBC, NYT, SecurityWeek): "We ensured the three '
            'entities were made aware, and we worked with our training partner on the changes they\'ve now made to their testing '
            'processes" (https://money.usnews.com/investing/news/articles/2026-09-18/gemini-hacked-three-companies-in-first-known-'
            'breakout-by-google-ai-wsj-reports); Irregular\'s own words are generic (\'All known issues on our end were remedied\'), so '
            'no other party\'s record shows the change; dated check 2026-11-01 (>=90 days after May 2026) found no claim and no '
            'imposed consequence')
n = 0
with open('aiid_agents_v25rows.jsonl', 'w') as out:
    for l in open('../rows/aiid_agents.jsonl'):
        r = json.loads(l)
        for c in r['consequences'] or []:
            if c.get('mode') != 'voluntary': continue
            if r['event_id'].startswith('aiid-1700') and c['kind'] == 'product change' and c['src'] != SRC_1700:
                print(r['event_id'], 'src -> verbatim (r2)'); c['src'] = SRC_1700
            if cls(r['event_id'], c) == 'self-only' and c['status'] != 'self-reported':
                print(r['event_id'], c['party'], c['kind'], c['status'], '-> self-reported'); c['status'] = 'self-reported'; n += 1
        r['scheme'] = 'v25'
        out.write(json.dumps(r, ensure_ascii=False) + '\n')
print('changed', n)
