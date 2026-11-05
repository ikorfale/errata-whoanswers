"""Compare coder 1 and coder 2 on codebook v2: Cohen's kappa on `channel` and on the lag bin, agreement on the rest.
Run from this folder: python3 compare_v2.py"""
import json, re, collections

def load(p):
    out = {}
    for l in open(p):
        l = l.strip()
        if l.startswith('{'):
            r = json.loads(l); out[r['event_id']] = r
    return out

def lagbin(v):
    try: d = int(v)
    except (TypeError, ValueError): return 'unknown'
    return '0-3' if d <= 3 else '4-30' if d <= 30 else '>30'

def kappa(pairs):
    n = len(pairs); po = sum(a == b for a, b in pairs) / n
    ca = collections.Counter(a for a, _ in pairs); cb = collections.Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n / n
    return po, (po - pe) / (1 - pe) if pe < 1 else float('nan')

c1, c2 = load('coder1-v2.jsonl'), load('coder2-v2.jsonl')
ids = sorted(set(c1) & set(c2)); print('rows both coded:', len(ids), '| only c1:', sorted(set(c1) - set(c2)), '| only c2:', sorted(set(c2) - set(c1)))
for f, fn in [('channel', lambda r: r['channel']), ('lag bin', lambda r: lagbin(r['lag_days']))]:
    pairs = [(fn(c1[i]), fn(c2[i])) for i in ids]; po, k = kappa(pairs)
    print(f'{f}: agree {sum(a == b for a, b in pairs)}/{len(ids)}, kappa {k:.3f}')
    print('   c1', dict(collections.Counter(a for a, _ in pairs)), '\n   c2', dict(collections.Counter(b for _, b in pairs)))
for f in ['disclosed_by', 'victim_named', 'filer', 'loss_class', 'could_name_responsible_at_time']:
    print(f'{f}: agree {sum(str(c1[i][f]).split(" ")[0] == str(c2[i][f]).split(" ")[0] for i in ids)}/{len(ids)}')
print('\nDisagreements on channel or lag bin:')
for i in ids:
    a, b = c1[i], c2[i]
    if a['channel'] != b['channel'] or lagbin(a['lag_days']) != lagbin(b['lag_days']):
        print(f"- {i}: c1 {a['channel']}/{a['first_sign_date']}/{lagbin(a['lag_days'])} | c2 {b['channel']}/{b['first_sign_date']}/{lagbin(b['lag_days'])} | c2 quote: {str(b.get('quote'))[:160]}")
