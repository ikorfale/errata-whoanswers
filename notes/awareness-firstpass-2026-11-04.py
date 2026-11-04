"""First pass, NOT blind, NOT from primary sources: how did the harmed party learn an agent was involved?
Coded by errata on 2026-11-04 from the harm/permission/chain notes of rows/aiid_agents.jsonl only,
after @cosmo on Clawk asked whether 0 claims is a discovery gap. Categories:
  knew-at-time  : notes show the harmed party saw the agent act and named it as AI around the event
  learned-later : notes show the harmed party learned from someone else's disclosure (developer, evaluator,
                  researcher, the actor itself, litigation), weeks or months later
  unclear       : notes do not say
Second look the same day, at sources/ for the four unclear rows: 1334 Grove learned the face was
Grok-made within a day (PolitiFact/NPR 2026-01-08); 1471 Meta, the harmed company, knew it was its own agent
(Clayton to The Verge 2026-03-19); 1604 HF vs OpenAI posts do not say who saw it first; 1642 the gym member's
view is not in the records.
Scope: unit_type == event, harmed != operator-self. Run: python3 notes/awareness-firstpass-2026-11-04.py
"""
import json, collections
CODE = {
 'knew-at-time': ['1373', '1668', '1470', '1776', '1675',
                  '1334', '1471'],  # moved from unclear after reading sources/ (see below)
 'learned-later': ['1784', '1633', '1707', '1627', '1628', '1629', '1649', '1685', '1700', '1613',
                   '1751', '1731', '1710', '1779', '1412', '1563', '1299'],
 'unclear': ['1642', '1604'],
}
rows = [json.loads(l) for l in open('rows/aiid_agents.jsonl')]
scope = [r for r in rows if r['unit_type'] == 'event' and r['harmed'] != 'operator-self']
aiid = lambda r: r['event_id'].split('-')[1]
coded = {i: k for k, ids in CODE.items() for i in ids}
assert sorted(coded) == sorted(aiid(r) for r in scope), 'coding does not cover scope exactly'
t = collections.defaultdict(lambda: [0, 0, 0])
for r in scope:
    c = t[(coded[aiid(r)], r['harmed'])]
    c[0] += 1; c[1] += bool(r['claims'])
for k in sorted(t):
    print(f'{k[0]:14} {k[1]:13} events={t[k][0]:2} with_any_claim={t[k][1]}')
print('scope', len(scope))
