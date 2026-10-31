# Open cases (non-blocking), from second-model reviews v17 and v18

Decide each when the first record that hits it is coded; note the decision in SCHEME.md.

## v19

- 1412: the record never says who directed the probe; the 1238 analogy gives `misuse`, but a one-line default ("a security firm or researcher reporting its own agent's intrusion directed it") would remove the only inference.
- 1633, 1751: evaluation agents; `autonomous-action` because the live step was "unsanctioned"; say that an evaluator's elicitation is `misuse` only when the harmful step itself was the elicited one (1238).
- 1070: misconfigured database of an agent platform, `out-of-scope` like 1364; name it beside 1364 so the "AI platform exposed" title does not tempt an `error` reading.
- 1710, 1731, 1633, 1470: no harm identified; the text (and naming 1731) forces inclusion with `harm=other`, unchanged from round 18.
- 1779, 1668: one deployer (OpenAI) and no users named in the text, so `event`; a clause that a provider's fleet is one deployer would close it.
- 1362, 1390: the AI output is in the chain and was the agent's purpose, so `misuse`, not `out-of-scope`; both excluded either way.
- Data notes: `court_seed.jsonl:3` coding_note still says "enters U only" though the row is court-only and, like row 1, a raw count outside every share; 1152 still v6. No count moves.
## v18

- 962: one conspiracy across four countries; both code `misuse` because the entities are not "independent deployers", but say whether a network of named fronts is one deployer.
- 1130, 1563, 1586: the AI action is only suspected ("may have been involved", "unconfirmed"); the Unit's "attributed (in part)" keeps both coders in scope, but a clause "attribution by the source suffices" would close the `out-of-scope` reading.
- 1710, 1731, 1633: attempts with no harm identified; no scope value for a harmless attempt, so both must include them with `harm=other`.
- 1412: whether CodeWall directed the probing is not in the record; under fix 1 the intent turns on that fact, not on the text.
- 1362, 1390: the AI identification was correct and the harm is human retaliation; `misuse` versus `out-of-scope`, both excluded.
- 1779, 1668: many agents but one deployer (OpenAI), so `event`; confirm a provider's fleet is one deployer, not "independent users".
- 1152: still v6 with "promised; delivery not independently confirmed" as a status; recode, no count moves.
- 1751, 1633, 1784, 1774: developer or evaluator in the deployer role; `operator` still has no fitting value (report-only).
## v17

- No scope value removes AIID incidents where no AI system did anything (`1364` Moltbook database, `1070` Serviceaide misconfiguration, `1362` a possibly bluffed facial-recognition claim); both coders include them as `error`. Decide whether that is intended.
- `1412` CodeWall: whether CodeWall directed the access to McKinsey's Lilli is not in the description; intent under fix 1 depends on that fact.
- `1070`: class actions against Serviceaide may exist; the match at `SCHEME.md:31` would make deployer-only reachable (U or P). Data, not text.
- If misuse and pattern/practice are printed as separate exclusion counts, campaigns like `1661`, `1766`, `1781` need an order of precedence between them.
- Rule 6 at `SCHEME.md:71` defaults to `absorbed`, while `SCHEME.md:59` says never infer a bearer and rule 2 needs a 90-day check; the `1152` row has such a row. No headline count moves.
- `1152` is coded under v6 with non-scheme status text ("promised; delivery not independently confirmed") and old resolution labels; recode to v17 values, no count moves.
- Evaluation incidents (`1751`, `1633`, `1784`, `1774`) put the developer or an evaluation body in the deployer role; nothing moves, but `operator` (user-chosen / deployer-integrated) has no fitting value.
- Row 1 "why" still reads as if the event enters U; harmless while court-only events stay raw counts.- 2026-10-31 (round 26, NONE): open, not blocking: (a) "left in the target's systems" when the deployer itself removed its artefacts (1633); (b) a paid review that found no impact ("nor is its cost"); (c) 1412 misuse vs autonomous-action from CodeWall's own report; (d) 1751/1707 recheck by 2026-12-31; (e) 1710 uncoded, U until 2026-12-24.
