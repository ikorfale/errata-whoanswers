"""Outcome type by platform type in the NOPE AI incident export (nope.net/incidents, CC BY 4.0), NOPE's own codes,
no recoding. Usage: python3 nope_outcomes.py export.csv[.gz]. Output of 3 Nov 2026: nope_outcomes_20261103.out."""
import csv, collections, gzip, io, sys
p = sys.argv[1]
raw = gzip.open(p).read() if p.endswith('.gz') else open(p, 'rb').read()
n = list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
legal = {'Lawsuit Filed', 'Lawsuit Ongoing', 'Lawsuit Dismissed', 'Lawsuit Settled', 'Regulatory Action',
         'Criminal Charges', 'Investigation Opened'}
for pt in ['agent', 'chatbot', 'companion', 'assistant', 'other']:
    g = [x for x in n if x['Platform Type'] == pt]
    print(pt, len(g), collections.Counter(x['Outcome Type'] or '(none recorded)' for x in g).most_common())
for pt in ['agent', 'chatbot', 'companion', 'assistant', 'other']:
    g = [x for x in n if x['Platform Type'] == pt]
    for lo, hi in [('2000', '2025-05'), ('2025-05', '2026-08'), ('2026-08', '2099')]:
        h = [x for x in g if lo <= (x['Incident Date'] or x['Reported Date'])[:7] < hi]
        print(pt, lo, hi, len(h), 'legal/official', sum(x['Outcome Type'] in legal for x in h))
