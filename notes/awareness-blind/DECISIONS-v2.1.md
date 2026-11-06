# Awareness v2.1: V2-ISSUES decided (2026-11-06)

Applied by `resolve_v21.py` to `resolved-v2.jsonl` -> `awareness-v2.1.jsonl` (output: `resolve_v21.out`). The column is joined
to the frozen rows by `event_id` and records the rows commit (1f44877, scheme v25); rows/ itself is not edited.

1. **first_sign_kind, adopted.** Every dated first sign is `exact`, `upper-bound` ("knew by D") or `same-moment`, with the
   packet line in `kind_line`. An upper-bound sign gives only `lag <= N`. Its bin is known only when N <= 3; otherwise
   it is `unknown (<= N)`. v2 counted these as dated lags. That was wrong for the headline (see below).
2. **Bounded lags, adopted, but narrower than V2-ISSUES said.** A lower bound on the lag needs both an event upper bound and a
   first sign that is not itself an upper bound. 1627-1629: the evaluations stopped on Thu 23.07 and the reached
   organisations were notified on 27.07, having "not previously detected the activity". That gives a lag of at least 4 days.
   V2-ISSUES said "certainly > 30", and the packet does not support that ("earliest incidents date to April" bounds the
   first incident, not each one). 1685 is an upper-bound sign ("We have notified" in the 09.09 post), so it gets no lower bound.
3. **Several harmed parties: code the party the row's harm_note names first**, and say so. No row changed codes under it today.
4. **Coder-1 labels in older source files:** they are moved to a notes file before any v3 packet is built. This is a procedure
   rule, so no code changed.

## What changes in the published reading (board 114263, 05.11)
| | v2 (05.11) | v2.1 |
|---|---|---|
| lag 0-3 days | 5 | 5 |
| lag >= 4 days, certain | 10 | 7 (3 at least 4, 1 at 4-30, 3 over 30) |
| lag over 30 days, certain | 8 | 3 (1707, 1710, 1731) |
| only bounded above (`<= N`, N > 3) | counted as dated | 6 (1299, 1470, 1563, 1604, 1685, 1779) |
| unknown | 11 | 8 |

Of the 7 rows where the harmed party certainly learned 4 or more days after the event, 6 learned it from the developer or an
outside researcher (all 6 come from lab evaluations or OpenAI's disclosures), and 1 noticed it itself (DSEWiki, 9 days). In the 5
rows where it learned within 3 days, it saw the harm itself, was told by the operator, or read about it in the press.
