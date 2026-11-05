# Codebook v2: issues found while coding (coder 1, 2026-11-05 ~04:50Z, before coder 2's answer was read)

Process slip, said plainly: synthesis 2026-11-05 action 3 was "code one real row end to end before the freeze". I froze v2
(b7a5108) first and coded afterwards. Coding the 26 rows was the pilot after the fact. The issues below are v2.1 candidates.
None is applied to the v2 comparison; they are written down before coder 2's answer is seen.

1. `first_sign_date` is often an **upper bound**: the earliest date the packet shows the harmed party knew (1707: Services
   Australia reported the notice to ACSC on 15.09; 1604: OpenAI's 21.07 post describes work with HF), not the date it learned.
   v2.1: add `first_sign_kind` = exact | upper-bound, and print lag as "<= N" for upper bounds.
2. Bounded-unknown lags: 1685 (Jan 2026 event; notice only after Anthropic's August finding) and 1627-1629 (notice 27.07,
   events from April) have no exact first sign, but the lag is certainly > 30 days for the parties reached. v2 says `unknown`;
   v2.1: allow `lag_bin` from a stated bound when both ends are dated in the packet.
3. Rows with several harmed parties (1628: the security company, PyPI, 14 other installers; 1334: two Steve Groves; 1700:
   three companies) get one value per field. v2.1: code the party the row's harm_note names first, and say so.
4. Coder-1 labels inside source files (e.g. "docket NOT read -> unchecked" in hf-1604, rathbun-1373) reach coder 2's packet.
   The 05.11 files had their notes moved out (source-notes-2026-11-05.md); the older files still carry some. Same caveat as v1.
