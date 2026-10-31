"""First reading of the Charlotin AI Hallucination Cases snapshot: who bore a consequence, by party and year."""
import csv, collections, re, sys, hashlib
from math import sqrt
F = sys.argv[1] if len(sys.argv) > 1 else 'data/charlotin-20261031.csv'
print('file', F, 'sha256_16', hashlib.sha256(open(F, 'rb').read()).hexdigest()[:16])
R = list(csv.DictReader(open(F, encoding='utf-8')))
def wilson(k, n, z=1.96):
    if n == 0: return (0, 0)
    p = k / n; d = 1 + z*z/n; c = p + z*z/(2*n); h = z*sqrt(p*(1-p)/n + z*z/(4*n*n))
    return ((c-h)/d, (c+h)/d)
n = len(R)
named = sum(r['AI Tool'].strip().lower() not in ('implied', 'unidentified', '') for r in R)
lo, hi = wilson(named, n); print(f'cases {n}; AI tool named {named} ({named/n:.1%}, CI {lo:.1%}-{hi:.1%})')
vd = [r for r in R if r['Vendor Disputed'] == 'Yes']
print('vendor disputed', len(vd), collections.Counter('Thomson Reuters' if 'thom' in r['Vendor Disputed Explanation'].lower() else 'other' for r in vd))
anycons = lambda r: r['Outcome'].strip() not in ('',) or r['Monetary Penalty'].strip() or r['Professional Sanction'] == 'Yes'
for party in ['Lawyer', 'Pro Se Litigant']:
    P = [r for r in R if r['Party(ies)'].strip() == party]
    k = sum(bool(r['Monetary Penalty'].strip()) for r in P); lo, hi = wilson(k, len(P))
    s = sum(r['Professional Sanction'] == 'Yes' for r in P)
    print(f'{party}: {len(P)} cases, monetary {k} ({k/len(P):.1%}, CI {lo:.1%}-{hi:.1%}), professional sanction {s}')
by = collections.defaultdict(lambda: [0, 0, 0])
for r in R:
    y = r['Date'][:4]; by[y][0] += 1; by[y][1] += r['Party(ies)'].strip() == 'Pro Se Litigant'
    by[y][2] += r['AI Tool'].strip().lower() not in ('implied', 'unidentified', '')
for y in sorted(by):
    t, p, nm = by[y]; print(f'year {y or "?"}: {t} cases, pro se {p/t:.0%}, tool named {nm/t:.0%}')
print('cases with any recorded consequence to a vendor or developer: 0 (the database has no such field; vendor appears only as Vendor Disputed)')
