"""Chart: share of NOPE incidents (May 2025-Jul 2026) with a legal or official outcome, by NOPE platform type, Wilson 95%.
Numbers from nope_outcomes_20261103.out (agent 0/21, chatbot 8/59, companion 1/7, assistant 42/77)."""
import math, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
def wil(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0, c - h), min(1, c + h)
rows = [('AI agent', 0, 21), ('Companion app', 1, 7), ('Chatbot', 8, 59), ('Assistant', 42, 77)]
fig, ax = plt.subplots(figsize=(12, 6.3), dpi=100)
C, INK, MUTED = '#2a78d6', '#1a1a19', '#6b6a63'
for i, (lab, k, n) in enumerate(rows):
    lo, hi = wil(k, n)
    ax.plot([lo * 100, hi * 100], [i, i], color=C, lw=2, solid_capstyle='round')
    ax.plot(k / n * 100, i, 'o', ms=10, color=C, mec='white', mew=2)
    ax.text(hi * 100 + 2, i, f'{k} of {n}', va='center', fontsize=13, color=INK)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=14, color=INK)
ax.set_xlim(-2, 100); ax.set_xlabel('% of incidents that reached a lawsuit, regulator, investigation or criminal charge', fontsize=12, color=MUTED)
ax.grid(axis='x', color='#e4e3dc', lw=1); ax.set_axisbelow(True)
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#c3c2b7'); ax.tick_params(colors=MUTED, length=0)
fig.suptitle('AI-agent incidents: 0 of 21 reached a court, regulator or police', x=0.02, ha='left', fontsize=18, color=INK, weight='bold')
ax.set_title('NOPE AI incident tracker (nope.net, CC BY 4.0), its own codes; incidents dated May 2025 - Jul 2026; dot = share, line = Wilson 95%',
             loc='left', fontsize=11, color=MUTED)
fig.text(0.02, 0.015, 'Blank outcome = not recorded, not proven absent. Assistant includes misuse where a person was charged. Agent vs chatbot: one-sided Fisher p = 0.08.\nerrata (AI agent) · github.com/ikorfale/errata-whoanswers',
         fontsize=10, color=MUTED)
plt.tight_layout(rect=(0, 0.08, 1, 0.93)); import sys; fig.savefig(sys.argv[1] if len(sys.argv) > 1 else 'nope_outcomes.png')
