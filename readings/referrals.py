"""Charlotin 'Professional Sanction' rows: how many are only a referral (re-derivable count; replaces the
unscripted '95 / 81' of 31 Oct). Usage: python3 referrals.py charlotin.csv
Referral = 'referr' in Outcome. Referral-only = no suspen|reprimand|disqualif|disbar in Outcome."""
import csv, re, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8')))
ps = [x for x in rows if x['Professional Sanction'].strip() == 'Yes']
ref = [x for x in ps if 'referr' in x['Outcome'].lower()]
only = [x for x in ref if not re.search(r'suspen|reprimand|disqualif|disbar', x['Outcome'].lower())]
print(f'records {len(rows)} | professional sanction {len(ps)} | referral {len(ref)} | referral only {len(only)}'
      f' ({100 * len(only) / len(ps):.1f}% of sanction rows)')
