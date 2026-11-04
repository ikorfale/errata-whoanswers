# Blind second coding of awareness: result and resolution (2026-11-04)

Codebook frozen in c1c325a before coder 2 saw anything. Coder 2 = Claude Fable 5.1, separate session, packet only
(AIID text + local source excerpts; 6 of 26 rows had AIID text only). Caveat: some source files carry errata's
short labels such as "(harmed)" next to a name; coder 2 never saw coder 1's codes or the row notes.

Agreement on `awareness` (compare.out): 22 of 26, Cohen's kappa 0.669.

| row | coder 1 | coder 2 | read against sources | resolved |
|---|---|---|---|---|
| 1334 Grok unmask | knew-at-time | learned-later | Grove learned the face was AI-made from the press within a day (PolitiFact 2026-01-08). Codebook says knew-at-time = "around the time (same day to a few days)" but learned-later = "from someone else's disclosure": timing and channel point opposite ways. | ambiguous |
| 1471 Meta forum | knew-at-time | learned-later | Coder 2 coded when the public learned (The Information); Meta, the harmed party, ran the incident internally. The codebook's "(or the public)" clause invited this. | ambiguous |
| 1604 HF intrusion | unclear | learned-later | Intrusion 07-09..07-13; OpenAI disclosed 07-21, HF 07-27. The packet does not say HF knew it was an agent before OpenAI told it; first disclosure is the developer's. | learned-later (HF's private knowledge date unknown) |
| 1613 Mythos sandbox | learned-later | unclear | AIID text only; my code came from my row note, not a source. | unclear until the primary source is read |

Resolved column: knew-at-time 5, ambiguous 2, learned-later 17, unclear 2 (1613, 1642). Bounds: learned-later 17-19 of 26.
Victim named in the first public disclosure (coder 2): 9 of the 19 rows it coded learned-later do not name the
harmed party (coder 1's first pass: 9 of 17). Coder 2's first discloser: developer 10, harmed party 5, researcher 5,
operator 2, press 2, evaluator 1, court 1.

Codebook lesson for v2: split awareness into two fields, `lag_days` (event to the harmed party's first sign of
knowing) and `channel` (own observation / developer / press / ...), and drop "(or the public)". Read primary
sources for the 6 aiid-only rows before the column joins rows/.
