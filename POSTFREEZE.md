# Post-freeze notes on scheme v20

Points found while coding under the frozen scheme. The scheme text is not edited; each point says whether it moves a
headline count. A point that moves a count goes to a new version with its own freeze; the others wait here.

- 2026-10-31, AIID 1424: intent `error` vs `autonomous-action` is close when an instructed task contains an uninstructed
  sub-step (state swap) followed by an approved command. Both are headline intents, so no count moves; `permission_source`
  (report-only) is filled only for autonomous-action, so the cross-tab can differ. Coded `error`, alternative printed.
- 2026-10-31, AIID 1424: the `kind` list has no value for an absorbed loss (rule 6 and `mode=absorbed` assume one).
  Absorbed rows enter no count; coded `n/a (description)`.
