# Blind second coding: how did the harmed party learn an AI agent was involved?

Frozen 2026-11-04 before the second coder saw any row. Task #647 (issue 17).
Scope: the 26 rows of rows/aiid_agents.jsonl with unit_type == event and harmed != operator-self.
Coder 1 (errata, unblinded, from row notes): notes/awareness-firstpass-2026-11-04.py.
Coder 2 (Claude Fable 5.1, separate session): sees only the packet below, never coder 1's codes or row notes.

## Packet per row
event id; AIID title, description and listed harmed parties; the text of every local source file for that row
(sources/). Rows with no local source are coded from the AIID text only and flagged `aiid-only`.

## Fields
1. `harmed_party`: who was harmed or nearly harmed, outside the party that ran the agent, in a few words.
2. `awareness`, one of:
   - `knew-at-time`: the harmed party saw the AI agent's action and knew or said it was an AI around the time
     of the event (same day to a few days);
   - `learned-later`: the harmed party (or the public) learned an agent was involved only from someone else's
     later disclosure: developer, evaluator, researcher, the agent's operator, a court filing, the press;
   - `unclear`: the packet does not say.
3. `disclosed_by`: who first made the agent's involvement public (developer, evaluator, researcher, operator,
   harmed party, press, court, unclear).
4. `victim_named`: does the first public disclosure name the harmed party (`yes` / `no` / `n.a.` when
   awareness is knew-at-time and no separate disclosure exists).
5. `quote`: the shortest passage from the packet that decides field 2; `none` if unclear.

Rule: code only what the packet says. Absence of a statement is `unclear`, never a guess.

## Agreement
Cohen's kappa on `awareness` (three classes) and percent agreement on `victim_named`, then every disagreement
is read against the sources and resolved in a dated note; the published column is the resolved one.
