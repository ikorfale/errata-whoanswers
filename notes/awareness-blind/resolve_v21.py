"""Awareness v2.1 (2026-11-06): V2-ISSUES items 1-4 decided (DECISIONS-v2.1.md) and applied to resolved-v2.jsonl.

Every dated first sign gets a kind. An upper-bound sign ("knew by D") gives only lag <= N, so its bin is known only
when N <= 3; otherwise the bin is 'unknown (<= N)'. A bounded lag needs an event upper bound AND a first sign that is
not an upper bound (item 2). Output: awareness-v2.1.jsonl keyed by event_id, with the rows commit it joins to
(rows/ is frozen at v25, so the column lives here, not in rows/)."""
import json, collections, subprocess, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = os.path.join(HERE, '..', '..', 'rows', 'aiid_agents.jsonl')
rows_commit = subprocess.run(['git', '-C', HERE, 'log', '-1', '--format=%h', '--', '../../rows/aiid_agents.jsonl'],
                             capture_output=True, text=True).stdout.strip()
KIND = {  # event_id number: (kind, reason from packet-v2.txt)
 '1299': ('upper-bound', 'court record date Nov 20; knowledge on record by then'),
 '1334': ('upper-bound', "'by Jan 8' he received threats"),
 '1373': ('exact', 'subject saw the post himself, month precision'),
 '1412': ('exact', 'disclosure email 03-01, CISO ack 03-02'),
 '1470': ('upper-bound', "her own first statement 06-04; told by the operator 04-28, so true lag <= 1"),
 '1604': ('upper-bound', "OpenAI's 07-21 post is the first dated sign that an agent did it"),
 '1563': ('upper-bound', 'IAB 06-15 citing FT'),
 '1627': ('exact', "notified 07-27; 'had not previously detected the activity'"),
 '1628': ('exact', "notified 07-27; 'had not previously detected the activity'"),
 '1629': ('exact', "notified 07-27 or later: 'continuing to reach out to the third'"),
 '1668': ('exact', "'noticed the agent spam posts on June 2nd, at 23:24 UTC'"),
 '1675': ('exact', 'observed the same day'),
 '1685': ('upper-bound', "'We have notified all affected parties' in the 09-09 post"),
 '1707': ('exact', "'We notified Services Australia... on 10 September'"),
 '1710': ('exact', "'disclosed... to the Department of Education on September 25'"),
 '1731': ('exact', "'disclosed... to the Canadian government on September 28'"),
 '1751': ('exact', "'shared this finding with the department on October 8'"),
 '1776': ('same-moment', 'learned when the buyer arrived'),
 '1779': ('upper-bound', 'WMF investigation post 10-05, prompted by earlier reports'),
}
# item 2: event upper bound from the packet, with the line; lag_lo = first sign - event_max
EVENT_MAX = {
 '1627': ('2026-07-23', "'stopped all cyber evaluations the same day' (Thu July 23)"),
 '1628': ('2026-07-23', "'stopped all cyber evaluations the same day' (Thu July 23)"),
 '1629': ('2026-07-23', "'stopped all cyber evaluations the same day' (Thu July 23)"),
}
def num(v):
    try: return int(v)
    except (TypeError, ValueError): return None
def binlo(lo): return '>30' if lo > 30 else '>3' if lo > 3 else None
out, C = [], collections.Counter()
frozen_ids = {json.loads(l)['event_id'] for l in open(ROWS)}
for l in open(os.path.join(HERE, 'resolved-v2.jsonl')):
    r = json.loads(l); k = r['event_id'].split('-')[1]
    kind, why = KIND.get(k, ('-', 'no first-sign date in the packet'))
    lag = r['lag_days']; n = num(lag); lo = hi = None
    if kind in ('exact', 'same-moment') and n is not None: lo = hi = n
    elif kind == 'upper-bound' and n is not None: hi = n
    elif lag == '>30': lo = 31
    if k in EVENT_MAX:
        from datetime import date
        lo = (date.fromisoformat(r['first_sign_date']) - date.fromisoformat(EVENT_MAX[k][0])).days
    if lo is not None and hi is not None: b = '0-3' if hi <= 3 else '4-30' if hi <= 30 else '>30'
    elif hi is not None: b = '0-3' if hi <= 3 else f'unknown (<= {hi})'
    elif lo is not None: b = binlo(lo) or 'unknown'
    else: b = 'unknown'
    if kind == 'upper-bound' and lag == '>30': b = 'unknown (upper-bound sign)'
    r.update(first_sign_kind=kind, kind_line=why, lag_lo=lo, lag_hi=hi, lag_bin_v21=b,
             event_max=EVENT_MAX.get(k, (None,))[0], rows_commit=rows_commit,
             in_frozen_rows=r['event_id'] in frozen_ids)
    out.append(r); C[(r['channel'], b if not b.startswith('unknown') else 'unknown')] += 1
with open(os.path.join(HERE, 'awareness-v2.1.jsonl'), 'w') as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('rows', len(out), '| in frozen rows/', sum(r['in_frozen_rows'] for r in out), '| rows commit', rows_commit)
print('kind:', dict(collections.Counter(r['first_sign_kind'] for r in out)))
print('bin v2.1:', dict(collections.Counter(r['lag_bin_v21'] if not r['lag_bin_v21'].startswith('unknown (') else 'unknown (bounded above)' for r in out)))
for k in sorted(C): print(f'  {k[0]:16} {k[1]:8} {C[k]}')
print('certain >30:', [r['event_id'].split('-')[1] for r in out if r['lag_bin_v21'] == '>30'])
print('bounded above only:', [(r['event_id'].split('-')[1], r['lag_hi']) for r in out if r['lag_bin_v21'].startswith('unknown (')])
