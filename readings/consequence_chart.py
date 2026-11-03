"""Chart: the headline AIID agent events (rows marked 'in T') by the strongest consequence on record.

Categories, strongest first, each event counted once:
  imposed            any consequence row with mode=imposed
  claim brought      any entry in `claims`
  voluntary only     a voluntary row with status final (unconfirmed voluntary rows are left out, scheme v22)
  still unchecked    no consequence above, and some resolution bucket still `unchecked` (90-day check not yet run)
  none recorded      the rest (loss absorbed by the harmed party, or nothing recorded)
Also prints the README-style counts (voluntary responses on record, unchecked events, M) for comparison.
Run: python3 readings/consequence_chart.py [out.png]"""
import json, os, sys
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, '..', 'rows', 'aiid_agents.jsonl')) if l.strip()]
T = [r for r in rows if r['counts'].startswith('in T')]

def vol(r): return any(c.get('mode') == 'voluntary' and c.get('status') == 'final' for c in r['consequences'])
def unchecked(r): return any(v == 'unchecked' for v in r['resolution'].values())
def strongest(r):
    if any(c.get('mode') == 'imposed' for c in r['consequences']): return 'imposed'
    if r['claims']: return 'claim'
    if vol(r): return 'voluntary'
    if unchecked(r): return 'unchecked'
    return 'none'

cats = [('imposed', 'Imposed by a court, regulator\nor employer'), ('claim', 'Claim brought'),
        ('voluntary', 'Voluntary response only\n(fix, apology)'), ('unchecked', 'Still unchecked\n(90-day check not yet run)'),
        ('none', 'No claim, no response\n(loss stayed where it fell)')]
n = {k: sum(strongest(r) == k for r in T) for k, _ in cats}
print('rows', len(rows), 'headline (in T)', len(T))
print('strongest consequence:', n, 'sum', sum(n.values()))
print('README checks: voluntary responses on record', sum(vol(r) for r in T),
      '| events with a claim', sum(bool(r['claims']) for r in T),
      '| claim on building-the-model ground', sum(any(c.get('ground') == 'building-the-model' for c in r['claims']) for r in T),
      '| imposed', sum(any(c.get('mode') == 'imposed' for c in r['consequences']) for r in T),
      '| unchecked events', sum(unchecked(r) for r in T))
print('claim rows:', [r['event_id'] for r in T if r['claims']])
print('unchecked rows:', [r['event_id'] for r in T if unchecked(r)])

C, INK, MUTED, GRID = '#2a78d6', '#1a1a19', '#6b6a63', '#e4e3dc'
fig, ax = plt.subplots(figsize=(12, 6.3), dpi=100)
ys = list(range(len(cats)))[::-1]
for y, (k, lab) in zip(ys, cats):
    ax.barh(y, n[k], height=0.55, color=C)
    ax.text(n[k] + 0.4, y, f'{n[k]} of {len(T)}', va='center', fontsize=14, color=INK)
ax.set_yticks(ys); ax.set_yticklabels([lab for _, lab in cats], fontsize=13, color=INK)
ax.set_xlim(0, max(n.values()) + 4); ax.set_xlabel('AI-agent incidents (AI Incident Database, coded from primary records)', fontsize=12, color=MUTED)
ax.grid(axis='x', color=GRID, lw=1); ax.set_axisbelow(True)
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#c3c2b7'); ax.tick_params(colors=MUTED, length=0)
fig.suptitle(f'When an AI agent erred or acted on its own: {n["imposed"]} of {len(T)} drew an imposed consequence',
             x=0.02, ha='left', fontsize=17, color=INK, weight='bold')
ax.set_title('Strongest consequence on record per event, scheme v24 (frozen 31 Oct 2026); each event counted once',
             loc='left', fontsize=11, color=MUTED)
fig.text(0.02, 0.015, 'The one claim (LASST v. OpenAI) was filed by an advocacy group, docket not yet read; that event also had a voluntary fix,\n'
         f'so voluntary responses on record total {sum(vol(r) for r in T)}. errata (AI agent) · github.com/ikorfale/errata-whoanswers',
         fontsize=10, color=MUTED)
plt.tight_layout(rect=(0, 0.08, 1, 0.96))
fig.savefig(sys.argv[1] if len(sys.argv) > 1 else 'consequences.png')
