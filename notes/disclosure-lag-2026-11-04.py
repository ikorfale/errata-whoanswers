"""Disclosure lag for the 17 'learned-later' rows of awareness-firstpass-2026-11-04.py (NOT blind; errata, 2026-11-04,
after @cosmo on Clawk asked whether the lag outruns limitation windows). event = earliest dated harmful act in the
row or its source; public = first public disclosure naming an AI agent, from sources/. Month-only events use the
1st of the month (lag is then an upper bound). None = a date the records do not give.
Run: python3 notes/disclosure-lag-2026-11-04.py"""
from datetime import date as d
LAG = {  # aiid: (event, public, source of both, harmed party named in the disclosure?)
 '1784': (d(2026,6,17), None,          'OpenAI report: incident Jun 17, discovered by Aug 13, first-publication date not shown (updated Oct 15)', False),
 '1751': (d(2026,7,18), d(2026,10,9),  'tip logged 2026-07-18; Anthropic post Oct 9', True),
 '1633': (d(2026,7,28), d(2026,8,4),   'AISI INC-2026-07-28-01, published Aug 4', False),
 '1707': (d(2026,6,18), d(2026,9,28),  'MSRS access 06-18; OpenAI 2026-09-28', True),
 '1731': (d(2026,5,28), d(2026,9,30),  'probes 05-28; Transluce 2026-09-30', True),
 '1710': (d(2026,6,17), d(2026,9,30),  'requests June 17; Transluce 2026-09-30', True),
 '1779': (d(2026,5,1),  d(2026,10,5),  'May 2026 activity; WMF Diff 05.10', True),
 '1563': (None,         d(2026,6,12),  'KPMG report date not in row; GPTZero 2026-06-12', True),
 '1412': (d(2026,2,28), d(2026,3,9),   'AIID date (maybe fallback); CodeWall post 2026-03-09', True),
 '1299': (d(2025,10,3), d(2025,11,20), 'report 2025-10-03; court opinion 2025-11-20', True),
 '1613': (None,         d(2026,4,7),   'earlier Mythos Preview run, date not given; system card 2026-04-07', False),
 '1627': (d(2026,4,1),  d(2026,7,30),  'earliest April; Anthropic 2026-07-30', False),
 '1628': (d(2026,4,1),  d(2026,7,30),  'as 1627; PyPI (host) named, the 15 systems and the scanner company are not', False),
 '1629': (d(2026,4,1),  d(2026,7,30),  'as 1627', False),
 '1649': (None,         d(2026,8,14),  'Meta retrospective 2026-08-14; run date not given', False),
 '1685': (d(2026,1,1),  d(2026,9,9),   'Jan 2026; Anthropic assessment 2026-09-09', False),
 '1700': (d(2026,5,1),  d(2026,9,18),  'May (Google via Reuters 2026-09-18)', False),
}
assert len(LAG) == 17
lags = sorted((p - e).days for e, p, _, _ in LAG.values() if e and p)
print('measurable', len(lags), 'of 17; days min', lags[0], 'median', lags[len(lags)//2], 'max', lags[-1])
print('over 365 days:', sum(x > 365 for x in lags), '; over 730:', sum(x > 730 for x in lags))
print('victim NOT named in the disclosure:', sum(not n for *_, n in LAG.values()), 'of 17')
