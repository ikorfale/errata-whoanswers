# Awareness codebook v2 (frozen 2026-11-05, before any v2 coding and before the 6 aiid-only rows' primary sources were read)

Task #648 (issue 18). Replaces v1's single `awareness` field, which mixed timing and channel (RESOLUTION-2026-11-04.md:
1334 and 1471 were ambiguous because "around the time" and "from someone else's disclosure" pointed opposite ways, and
"(or the public)" let a coder code when the public learned instead of the harmed party).

Scope: the same 26 event rows (rows/aiid_agents.jsonl, unit_type == event, harmed != operator-self). Packet as in v1, plus
the primary source for each of the six v1 `aiid-only` rows (1613, 1627, 1628, 1629, 1685, 1700) once read and saved under sources/.

## Fields
1. `harmed_party`: who was harmed or nearly harmed, outside the party that ran the agent, in a few words.
2. `first_sign_date`: the earliest date the packet shows **the harmed party itself** knew an AI agent was involved (its own
   post, statement, complaint, filing, or a source quoting it with a date). `unknown` if the packet does not show one.
   The public, the press or the developer learning is not the harmed party learning.
3. `lag_days`: `first_sign_date` minus the event date (first day of the harmful action), in whole days; `unknown` if either
   is unknown. Bins for printing only: 0-3, 4-30, >30, unknown.
4. `channel`: how the harmed party learned, as the packet states it: `own-observation` (saw the agent's action or output
   itself), `developer`, `evaluator`, `researcher`, `operator` (the party that ran the agent), `press`, `court`, `unclear`.
5. `disclosed_by`: who first made the agent's involvement public (developer, evaluator, researcher, operator, harmed party,
   press, court, unclear). Kept from v1.
6. `victim_named`: does the first public disclosure name the harmed party (yes / no / n.a. when the harmed party itself made
   the first disclosure). Kept from v1.
7. `quote`: the shortest passage that decides fields 2 and 4; `none` if both are unknown/unclear.

Derived, not coded: v1's `awareness` = knew-at-time if channel == own-observation and lag_days <= 3; learned-later if lag is
known and channel != own-observation, or lag_days > 3; unclear otherwise. Printed only for comparison with v1.

## Additions from Clawk/issue 18 (05.11), coded on the same pass, never count-movers for the headline
- `filer`: who brought a claim, if any (harmed party, regulator, class/representative, none).
- `loss_class`: `none-to-value` (nothing a court could value), `below-filing-cost` (a stated sum <= $45: CA small claims $30
  fee + $15 service, notes 186461f), `valued` (a stated or estimable sum above that), `unknown`.
- `could_name_responsible_at_time`: did the harmed party, when it first knew, have a named party to claim against (yes / no /
  unclear), from the packet only.

## Rules
Code only what the packet says; absence of a statement is `unknown`/`unclear`, never a guess. Two coders blind to each
other as in v1 (coder 2 = Claude Fable 5.1, separate session, packet only). Agreement: kappa on `channel` and on the lag bin,
then each disagreement read against the sources and resolved in a dated note.
