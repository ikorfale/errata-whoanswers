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
- 2026-10-31, AIID 1784: a developer's linked product change (prevention) is a voluntary consequence, so rule 2 gives the harmed
  organization no `absorbed` row, though nothing reached it. Report-only (voluntary and absorbed rows enter no count); a coder who reads
  rule 2 as 'no consequence to the harmed' adds a harmed/absorbed row. Org unnamed in the record, so no court search is possible.
- 2026-10-31, AIID 1751: the task itself was to generate and perform example tasks on random pages, so the fabricated tip is coded
  `error` (the instructed task's output); a coder reading the submission as an uninstructed step codes autonomous-action. Both are in T; no count moves.
- 2026-10-31, AIID 1633 (MAY MOVE A COUNT, ask in the next review round): the deployer's own report says the attempts failed and
  'no real-world harm resulted'. The scheme has no rule for events whose record finds no realised harm: one coder keeps 1633 in T
  (AIID lists it as an incident; people were targeted and deceived), another drops it. Also: two developers in one event's chain.
- 2026-10-31, AIID 1642: the user's own post (30.04) states only that the agent could cancel others' reservations; the realised
  cancellation rests on the agent's messages in screenshots the user supplied to ABC. Coded from those; no count moves either way
  (the event stays in T). Chain has no deployer: self-hosted open-source harness, so deployer-only is empty.
- 2026-10-31, AIID 1707: a government forensic inquiry and a parliamentary hearing with no pleaded ground are not `claims`, so all
  buckets are no-claim. A coder who reads a state inquiry into the developer as a claim makes model maker reachable and `pending`
  (moves 1707 from T-minus-M into P). MAY MOVE A COUNT; ask in the next round. Recheck by 2026-12-31 (taskforce due end of year).
- 2026-10-31, AIID 1731: failed probes with no realised harm (as 1633) and an unattributed chain (no developer named). `operator` has
  no `unknown` value, so deployer-integrated is a guess flagged in operator_note; report-only. The no-harm question decides T for both.
- 2026-10-31, AIID 1470: a deployer's bot picking work its own pipeline asked it to pick is coded `error`; autonomous-action is the other
  reading. Both in T; no count moves.
- 2026-10-31 18:45, round 24 (fable-scheme-v24.txt): two blocking points, both from rows coded this evening. 1673 attack vs
  autonomous-action -> v23 says attack needs an outsider who directed the step. 1633/1731 no realised harm -> v23 keeps such
  attempts as events and prints their number beside T (1710 joins them). 1313 misuse, 1751, 1784, 1707 confirmed not blocking.
  The clean-round count restarts: freeze needs rounds 25 and 26 to return NONE.
- 2026-10-31 18:50, round 25: round-24 fixes confirmed; one new point (realised harm for the no-harm number: 1779, 1751) -> v24. Rows unchanged. Rounds 26 and 27 must be NONE before a freeze.
- 2026-10-31 18:59, round 26: NONE (first clean round on v24). Open cases to OPEN-CASES.md, no text change, so round 27 can confirm.
- 2026-10-31 19:05, round 27: NONE (second clean round). v24 frozen, tag scheme-v24. Open cases (deployer-removed artefacts, paid no-impact review, completed-then-restored actions, 1412) stay in OPEN-CASES.md; any text change after this is v25 and logged here.
- 2026-10-31 19:34, AIID 1471 (Meta internal agent): exposure of data to unauthorized employees that was closed after ~2 h is
  coded realised (plain T) under the v27 open case "completed-then-restored is realised"; Meta's "no user data was mishandled"
  speaks to misuse, not to the exposure. A coder reading "contained" there would move 1471 into the no-harm number beside T
  (T itself unchanged). Intent autonomous-action (unapproved post) vs error (wrong advice): both headline, no count moves.
- 2026-10-31 19:37, AIID 1675 (Instinct, MAY MOVE A COUNT): the harm is a stated vendor data practice (retain and use indexed
  mail after disconnect, ToS) that surfaced through one user's dated episode. Coded `event` (the text names one dated episode,
  line 51); a coder who reads a standing practice applied to every user as `practice` moves 1675 out of T. Ask in the next round.
- 2026-10-31 19:41, AIID 1412: closed from CodeWall's own report: its agent proposed the target from a list it was prompted to
  build, and CodeWall "decided to point" the offensive agent at it, so the operator directed the intrusion: `misuse` (the v27
  open case named this fork). Not in T. A security firm's disclosed red-team run lands in the misuse count beside fraud; the
  printout should say so.
- 2026-11-01, #596 (13 rows outside the 51, AIID 1178 1433 1441 1442 1604 1613 1627 1628 1629 1649 1674 1685 1700):
  - AIID 1604 (MAY MOVE A COUNT): LASST's UCL/CDAFA complaint (read only as press and the plaintiff's PDF, `read: no`) is coded
    `operating-or-publishing`, so it maps to deployer-only, not M. It cites AB 316 (no "the AI acted autonomously" defence); a coder
    who reads that as a design ground puts 1604 into M (0 -> 1). OpenAI holds developer, deployer and employer-of-the-user roles; the
    scheme sends operating claims against a user or employer to the operator bucket, so a coder may put the U in operator instead.
  - AIID 1700: the developer's own statement "no harm resulted" plus no stated record left or loss borne -> counted in the within-T
    no-realised-harm number (as 1710). Unauthorised logins to three companies' protected systems could be read as realised (access
    itself); then the number drops by one. No other count moves.
  - AIID 1442: Amazon denies that the AI caused the outage (`tool_named: disputed`). Kept as `event` because the source attributes the
    step (scope rule: attribution by the source suffices, 1130, 1563). intent autonomous-action vs error: both headline.
  - Irregular rows (1627-1629, 1649, 1685, 1700): two deployers in the chain (the lab and the evaluation firm whose environment was
    misconfigured). Report-only. The congressional oversight letter to Anthropic (2026-08-10) is not a claim (as 1707).
  - AIID 1613 harmed `court/public`: exploit details posted on public sites; the harmed value list has no "public website operators".
  - Recheck: 1649 on 2026-11-03 (90 days), 1674 on 2026-11-19, 1604 docket (case number unknown), 1685 after METR's report.
  - Review round on the 13 rows (fable-rows596-1.txt): 1 blocking point, applied: 1700 lacked its episode date and the dated
    >=90-day check that step 0 needs (runs in May 2026, check 2026-11-01). Non-blocking, logged: 1441 is coded realised harm though
    the photos were recovered (open completed-then-restored case, as 1471); 1674's sent email is realised (a record left in others'
    systems, as 1613's posts), "innocuous" is not "no harm"; 1442's voluntary row bears `deployer` where developer-run evaluations
    bear `developer` (matters only if voluntary responses are ever printed per bucket).
  - Round 2 (fable-rows596-2.txt): 1 blocking point, same defect as 1700 on 1613 (no episode date); `date_event` added to all 13
    rows from their records. 1627-1629: the Anthropic post gives "April" as the earliest of the three and 2026-07-24 as the date
    found; if one of them ran after 2026-08-03 it would be `unchecked`, which the post rules out (all found by 2026-07-24).
    No clean round yet on the 13 rows.
