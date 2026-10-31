# Post-freeze notes on scheme v20

Points found while coding under the frozen scheme. The scheme text is not edited; each point says whether it moves a
headline count. A point that moves a count goes to a new version with its own freeze; the others wait here.

- 2026-10-31, AIID 1424: intent `error` vs `autonomous-action` is close when an instructed task contains an uninstructed
  sub-step (state swap) followed by an approved command. Both are headline intents, so no count moves; `permission_source`
  (report-only) is filled only for autonomous-action, so the cross-tab can differ. Coded `error`, alternative printed.
- 2026-10-31, AIID 1424: the `kind` list has no value for an absorbed loss (rule 6 and `mode=absorbed` assume one).
  Absorbed rows enter no count; coded `n/a (description)`.
- 2026-10-31, AIID 1469: a party outside the AI chain (infrastructure provider Railway) restored the data and patched its
  API. `bearer` has no role for it, so no row; noted in `counts`. Moves no count (voluntary rows never enter k or s), but the
  "voluntary responses" printout would differ if a coder created a row: print it as a separate "outside-chain response" line.
- 2026-10-31, `harmed` takes one value; 1469 hit the operator and its customers. Report-only field, no count moves.
- 2026-10-31, AIID 1671/1672: a vendor statement announcing mitigations for "a handful of reports" without naming the event.
  Rule 4 needs the vendor to link a product change to the event, so no row; `vendor_voice` = fix-announced. Two coders could
  differ on whether a generic statement made in reply to named public reports is a link. Voluntary rows enter no count.
- 2026-10-31, AIID 1719: events younger than 90 days have every bucket `unchecked` (step 6 runs first), even with no claim at all.
  This moves events from T-minus-M into U until the check date; it is what the text says, and it is printed (recheck 2026-12-18).
- 2026-10-31, AIID 1313: the primary record (Anthropic's own write-up: a red-team installation handed to reporters to
  test adversarially) moves it from the T pre-sort to `misuse`. Not a scheme ambiguity: the pre-sort read only the AIID
  text, which omits the framing. T 28 -> 27 so far. Pre-sorts from AIID text are provisional until each row is coded.
- 2026-10-31, AIID 1673 (MAY MOVE A COUNT, ask in the next review round): a third-party package removed the agent's
  confirmations; the agent's own over-scope steps did the harm. `attack` ("an outsider caused the harmful step through the
  system") vs `autonomous-action` ("a step nobody instructed"). Coded autonomous-action: the package instructed no deletion.
  A coder who reads guardrail removal by an outsider as causing the step moves 1673 from T to attack.
