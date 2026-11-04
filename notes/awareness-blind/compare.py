"""Compare coder 1 (errata, unblinded first pass) with coder 2 (Fable, blind, coder2.jsonl) on awareness.
Run from the repo root: python3 notes/awareness-blind/compare.py"""
import json, collections, importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location('fp', 'notes/awareness-firstpass-2026-11-04.py')
fp = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(fp)
c1 = {i: k for k, ids in fp.CODE.items() for i in ids}
c2 = {}
for l in open('notes/awareness-blind/coder2.jsonl'):
    if l.strip():
        d = json.loads(l); c2[d['event_id'].split('-')[1]] = d
assert sorted(c1) == sorted(c2), (set(c1) ^ set(c2))
K = ['knew-at-time', 'learned-later', 'unclear']
n = len(c1); m = collections.Counter((c1[i], c2[i]['awareness']) for i in c1)
po = sum(m[(k, k)] for k in K) / n
pe = sum(sum(m[(k, j)] for j in K) * sum(m[(j, k)] for j in K) for k in K) / n / n
print(f'n={n} agree={sum(m[(k,k)] for k in K)} po={po:.3f} pe={pe:.3f} kappa={(po-pe)/(1-pe):.3f}')
print('rows=coder1, cols=coder2', K)
for a in K: print(f'{a:14}', [m[(a, b)] for b in K])
print('coder2 victim_named:', collections.Counter(c2[i]['victim_named'] for i in c2))
for i in sorted(c1):
    if c1[i] != c2[i]['awareness']:
        print(f'DISAGREE {i}: c1={c1[i]} c2={c2[i]["awareness"]} aiid_only={c2[i].get("aiid_only")} | {c2[i]["quote"][:160]}')
