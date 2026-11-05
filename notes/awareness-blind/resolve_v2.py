"""Resolved v2 column (2026-11-05): coder 2's codes where both coders agree or coder 2 was right on the packet, with the
overrides below read against packet-v2.txt (RESULT-v2-2026-11-05.md gives the line for each). Prints channel x lag bin."""
import json, collections
from compare_v2 import load, lagbin
c1, c2 = load('coder1-v2.jsonl'), load('coder2-v2.jsonl')
R = {i: dict(c2[i]) for i in c2}
O = {  # event_id suffix: (first_sign_date, lag, channel, kind)
 '1412': ('2026-03-02', 2, 'operator', 'exact'),
 '1470': ('2026-06-04', 37, 'operator', 'upper-bound'),
 '1751': ('2026-10-08', 'unknown', 'developer', 'exact'),
 '1604': ('2026-07-21', 12, 'unclear', 'upper-bound'),
 '1779': ('2026-10-05', 'c2', 'own-observation', 'upper-bound'),
 '1776': ('unknown', 0, 'own-observation', 'same-moment'),
 '1563': ('2026-06-15', '>30', 'press', 'upper-bound'),
 '1613': ('unknown', 'unknown', 'unclear', '-'),
 '1471': ('unknown', 'unknown', 'unclear', '-'),
 '1700': ('unknown', 'unknown', 'unclear', '-'),
}
for i, r in R.items():
    k = i.split('-')[1]
    if k in O:
        d, lag, ch, kind = O[k]
        r['first_sign_date'], r['channel'], r['first_sign_kind'] = d, ch, kind
        if lag != 'c2': r['lag_days'] = lag
def b(v): return '>30' if v == '>30' else lagbin(v)
with open('resolved-v2.jsonl', 'w') as f:
    for i in sorted(R): f.write(json.dumps(R[i], ensure_ascii=False) + '\n')
t = collections.Counter((R[i]['channel'], b(R[i]['lag_days'])) for i in R)
print('channel:', dict(collections.Counter(R[i]['channel'] for i in R)))
print('lag bin:', dict(collections.Counter(b(R[i]['lag_days']) for i in R)))
for k in sorted(t): print(f'  {k[0]:16} {k[1]:8} {t[k]}')
print('rows', len(R))
