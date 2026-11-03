# Blind coding task: declared_context and access_gate (40 rows)

Each line of rows_blind.jsonl is one incident where an AI agent (a model acting with tools) caused or nearly caused harm.
Outcome fields (claims, lawsuits, consequences, vendor responses) were removed; a few sentences mentioning outcomes were redacted.
Code ONLY from the text given. Do not use outside knowledge of what happened afterwards.

For every row (R01..R40) give:

1. declared_context — what the operator was running when the effect happened:
   - `evaluation` : an evaluation, red-team, research or benchmark harness (a test run, declared as such by whoever ran it)
   - `deployment` : a product or real work deployment (a user or company using the agent for real tasks)
   - `unknown`    : the text does not say
2. access_gate — only for rows coded `evaluation` (write `n/a` for others):
   - `granted`  : the access that let the effect out (internet, credentials, refusals off, classifiers off) was granted on purpose for the run
   - `failed`   : isolation/containment was intended and failed (sandbox escape by misconfiguration, aborts not honoured, "misunderstanding" of scope)
   - `instructed`: escaping or reaching outside was itself the instructed test
   - `unclear`  : the text does not let you decide
3. one short quote (≤ 20 words) from the row that decides each code.

Output: a TSV block with columns row, aiid, declared_context, access_gate, quote; then any row where you hesitated, with why.
