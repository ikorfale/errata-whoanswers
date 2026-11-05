"""v24 -> v25 recode: voluntary consequences classed self-only in voice_of_record_113456.py get status self-reported.
Reads the published v24 rows ../rows/aiid_agents.jsonl (input untouched), writes aiid_agents_v25rows.jsonl, prints every
change. 04.11 ~18:00Z: the first draft read a stale v20-era working copy and lost date_event on 33 rows, the 1649 check
and 1441's recode; this version starts from the published rows. Round-2 edit carried: 1700's src with Adkins' verbatim words.
Round-3 edits (fable-scheme-v25-r3.txt, 05.11): 1700's change is Irregular's, shown by Google's record (another party), so
party Irregular, bearer deployer, status final; 1649 Irregular src says what Meta's text does and does not show."""
import json
from voice_of_record_113456 import cls
SRC_1700 = ('Adkins statement via Reuters 2026-09-18, verbatim and attributed (also BBC, NYT, SecurityWeek): "We ensured the three '
            'entities were made aware, and we worked with our training partner on the changes they\'ve now made to their testing '
            'processes" (https://money.usnews.com/investing/news/articles/2026-09-18/gemini-hacked-three-companies-in-first-known-'
            'breakout-by-google-ai-wsj-reports). The change stated as made is the training partner\'s (Irregular), so Google\'s '
            'record is another party\'s record of it (r3); Google\'s own acts are notification and "worked with" (vendor_voice). '
            'Irregular\'s own words are generic (\'All known issues on our end were remedied\'); dated check 2026-11-01 (>=90 days '
            'after May 2026) found no claim and no imposed consequence')
SRC_1649_IRR = ('Meta retrospective 2026-08-14 says only that Meta shared areas for improvement "with Irregular to support '
                'remediation efforts" (no Irregular measure stated as taken); Irregular statement via Bloomberg 2026-08-06 is a press '
                'paraphrase; Irregular\'s own white paper not read (r3)')
n = 0
with open('aiid_agents_v25rows.jsonl', 'w') as out:
    for l in open('../rows/aiid_agents.jsonl'):
        r = json.loads(l)
        for c in r['consequences'] or []:
            if c.get('mode') != 'voluntary': continue
            if r['event_id'].startswith('aiid-1700') and c['kind'] == 'product change' and c['src'] != SRC_1700:
                print(r['event_id'], 'src -> verbatim (r2)'); c['src'] = SRC_1700
            if r['event_id'].startswith('aiid-1700') and c['kind'] == 'product change':
                c.update(party='Irregular', bearer='deployer', status='final'); print(r['event_id'], '-> Irregular, deployer, final (r3)')
            if r['event_id'].startswith('aiid-1649') and c['party'].startswith('Irregular') and c['src'] != SRC_1649_IRR:
                c['src'] = SRC_1649_IRR; print(r['event_id'], 'Irregular src reworded (r3)')
            if cls(r['event_id'], c) == 'self-only' and c['status'] != 'self-reported':
                print(r['event_id'], c['party'], c['kind'], c['status'], '-> self-reported'); c['status'] = 'self-reported'; n += 1
        # r4 non-blocking: the counts note must name the status the row now carries
        if r['event_id'].startswith('aiid-1563'):
            r['counts'] = r['counts'].replace('(withdrawal by the employer, unchecked)', '(withdrawal by the employer, self-reported, v25)')
        if r['event_id'].startswith('aiid-1649'):
            r['counts'] = r['counts'].replace('(Meta product change, final)', '(Meta product change, self-reported, v25; Irregular unchecked)')
        r['scheme'] = 'v25'
        out.write(json.dumps(r, ensure_ascii=False) + '\n')
print('changed', n)
