"""Seeded random sample from AIID 2025-26 rows that neither selection rule picked
(not in the 51 'agent' candidates, not labelled ACTION by the recall model).
Drawn and published before any row is read. Usage: python3 neither_sample.py"""
import json, random, hashlib
from math import comb
N_SAMPLE, SEED = 200, 20261101
L = [json.loads(l) for l in open('frame_labels.jsonl')]
cand = {json.loads(l)['incident_id'] for l in open('agent_candidates.jsonl')}
act = {x['id'] for x in L if x['label'] == 'ACTION'}
pool = sorted((x['id'] for x in L if x['id'] not in cand and x['id'] not in act), key=int)
sample = sorted(random.Random(SEED).sample(pool, N_SAMPLE), key=int)

def upper(N, n, k, alpha=0.05):
    # largest K with P(X<=k | N,K,n) > alpha: exact one-sided hypergeometric bound
    K = k
    while K < N:
        p = sum(comb(K+1, i)*comb(N-K-1, n-i) for i in range(k+1)) / comb(N, n)
        if p <= alpha: return K
        K += 1
    return N

print('pool', len(pool), 'sample', N_SAMPLE, 'seed', SEED)
print('bounds (found -> at most missed in pool):', {k: upper(len(pool), N_SAMPLE, k) for k in range(5)})
s = '\n'.join(sample) + '\n'
open('neither_sample_ids.txt', 'w').write(s)
print('ids sha256', hashlib.sha256(s.encode()).hexdigest()[:16])
