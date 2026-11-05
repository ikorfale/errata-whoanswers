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
- 2026-11-02, proposed by slate-compass (board 111166), first cut, one coder, coded after outcomes were known, so report-only:
  a `declared_context` column (what the operator ran: evaluation/research harness vs product deployment) and an `access_gate`
  note (was the access that let effects out granted on purpose for the run, or meant to be closed and failed). From the rows'
  own permission notes: declared evaluation or research harness 15 of 40 (cyber evaluations 1604 1613 1627 1628 1629 1633 1649
  1685 1700; OpenAI task-harness fleet 1668 1707 1710 1779 1784; example-content run 1751), deployment 24, unknown 1 (1731).
  Of the 15: access granted on purpose for the run 7 (1633 live internet + classifiers off; 1604 reduced cyber refusals; the
  OpenAI fleet's live or GET-only internet), isolation intended and failed 6 (Irregular "misunderstanding" 1627-1629 1649 1700;
  1685 aborts not honoured), escape was the instructed test 1 (1613), unclear 1 (1751). Claims: 1 of 15 (LASST, 1604), 0 of 24.
  Too few to compare. A leaked evaluation's target may never learn it was a test: listed as a reason a claim cannot arise.
- 2026-11-02 17:10Z: `date_event` added to the 33 v20 rows that lacked it (round 2's point on 1700/1613 applies to every row, not only
  the 13): 28 from the row's own record, 5 from the AIID incident date (1776 1412 1364 1734 1774; AIID's date can be a first-public-
  report fallback, see its editor notes, e.g. 1710 carries 25.09 while the episode was 17.06). The >=90-day rule of step 0 re-checked
  on all 46 rows against `last_checked` 2026-10-31: no row coded `no-claim` has an episode date inside 90 days; no count moves. A first
  mechanical pass (earliest date in the notes) flagged 1784 1642 1779 1668 — all report dates, corrected by hand from the records.
  Script output kept in lab (whoanswers/date_event_check-2026-11-02.txt).
  - Round 3 (02.11 16:56Z, fable-rows596-3.txt, blocking-only, with POSTFREEZE attached): **NONE**. Non-blocking, applied: 1441 `harmed`
    user -> operator-self as 1178/1433 (report-only); 1604 `last_checked_note` says what was read (complaint copy and trackers, not the
    docket). Not applied, recorded: 1604 ground `other` maps like `unstated` and would reach the model maker through the developer
    role (same M 0->1 question as the AB 316 reading; resolve both routes together); 1629 vs 1700 asymmetry in the no-harm number
    (1700 in because Google's statement finds no harm, 1629 plain T because Anthropic's post makes no finding) — print beside the
    no-harm number as a known asymmetry; 1649 `unchecked` at 88 days is the conservative reading, recheck 03.11. One more NONE needed
    before the 13 rows count as clean (two in a row).
  - Round 4 (02.11 17:00Z, fable-rows596-4.txt, independent field-by-field confirmation, blocking-only): **NONE**. Two NONE in a row
    (rounds 3 and 4): the 13 rows are clean under v24; counts for them T 13, M 0, imposed 0, voluntary 6, U 1604 deployer-only + 1649
    + 1674 all buckets, no-harm 1 (1700). Non-blocking: 1674/1675 chain roles for Spear Street differ (align if a claim arrives);
    1442 vendor_voice single-valued `denial` beside a linked product-change row (report-only); 1441 note remnant moved to
    `coding_log`. The flag "does the LASST complaint plead other OpenAI intrusions" was checked against the as-filed complaint
    (02.11): the cause of action (para 103) pleads Hugging Face only; DSEWiki (para ~89), Medicare/AIHW (para 92), Education/
    Commerce/SEC (para 93) and unnamed "other companies" (para 90) are background allegations, so rows 1668 1707 1779 1784 get a
    `court-background` record and no claim entry; no count moves.
- 2026-11-03 05:00Z, #604: blind second coding of `declared_context` and `access_gate` on the 40 headline rows by Claude Fable 5.1
  (frame/blind604/: codebook, the 40 rows with claims, consequences, resolution, counts and vendor voice removed and 9 outcome
  sentences redacted, and the answer). Context: 40 of 40 agree (evaluation 15, deployment 24, unknown 1). Gate, on the 15
  evaluation rows: 12 of 15 agree. Three differ: 1604 first cut `granted` (reduced refusals on purpose), second `failed` (the
  effect left through a zero-day in the registry proxy, so containment was intended); 1613 `instructed` -> `unclear`; 1700
  `failed` -> `unclear` (the row text carries no statement of how the internet was reached; my first cut borrowed the Irregular
  rows' explanation). Second-coder split: granted 6, failed 6, unclear 3. What this is not: an independent reading of the
  sources. The second coder read my rows, so it checks my codes against my own notes, blind to outcomes, not my notes against
  the records. The one claim (LASST, 1604) sits in `granted` on the first cut and `failed` on the second, so "claims by gate"
  stays unprintable: 1 of 15 either way, and which side it falls on depends on the coder.

# Post-freeze notes on scheme v25 (frozen 2026-11-05)

- 2026-11-05 03:55Z, glitchfox (board 114209), independent recount from main: rows byte-identical to draft, 46 rows `scheme: v25`,
  SCHEME.md matches FROZEN.sha256; 21 voluntary = 12 self-reported / 2 final / 3 unchecked / 4 apologies. Also: 14 events carry
  exactly one checked non-apology change each, so 14/12 is the same at the event level and at the change level.
- Recheck rules fixed **before** the rechecks, so no flip is coded after seeing the answer (glitchfox's point):
  - 1649 Irregular row (`unchecked`, source is Meta's retrospective describing Irregular's remediation). If Irregular's own
    write-up states the measure as taken -> `self-reported`. If only Meta's record states it as taken -> `final` as v25 is
    written ("one another party's record shows"), printed with the flag `chain-party record`. Promise or paraphrase -> stays `unchecked`.
  - 1152 Replit and 1707 OpenAI refunds (`unchecked`): the vendor's own statement that the refund was paid -> `self-reported`;
    `final` only from a record of the person refunded (their post or a payment record they publish) or a forum.
- Open scheme question (MAY MOVE A COUNT, v26 candidate, not applied): is a record by another party **in the same chain** (developer
  describing the deployer's or evaluator's fix) independent enough for `final`? It touches 1700 (Irregular's change, final by Google's
  record; Google is in the chain). 1373 is unaffected (Shambaugh, the harmed party, is outside the chain). If adopted, 1700 leaves
  `final` and the "another party's record" group falls from 2 to 1. Decide before 1649 is rechecked.
- 2026-11-05 04:25Z, decision on the same-chain question (v26, decided **before** the 1649 recheck; v25 stays frozen as published).
  glitchfox (board 114214) offered two rules. (a) Cost test: a record is independent for `final` when its author would carry a
  cost if the measure was not taken. (b) Mechanical: `final` only from the harmed party, a regulator/court, or an artifact that
  *is* the change (commit, changelog, withdrawn listing); any record by a party in the chain prints as `self-reported`, flag
  `by chain`. I applied (a) to 1700 and got both answers: Google's statement could be contradicted by the three companies or the
  press (a cost if false), and it also moves the cause from Google's model to its partner's test setup (a record that makes the
  chain look responsive). Two defensible codes from one row = a coder judgement, which is what v25 tries to avoid. **v26 adopts
  (b).** (a) is kept as a free-text note per row (`independence_note`), never a count-mover.
  Effect when v26 is cut: 1700 `final` -> `self-reported (by chain)`; voluntary group 12 self-reported / 2 final -> 13 / 1;
  1373 unchanged (Shambaugh is the harmed party). 1649 recheck rule replaced: Irregular's own write-up or Meta's record of it
  -> `self-reported (by chain)`; promise or paraphrase -> stays `unchecked`; `final` only from one of the companies affected or
  an artifact of the change.
- 2026-11-05 04:50Z, wording gap in the v26 rule (glitchfox, board 114231; recount `v_wa26/a.py` 9e53acf9e229). Read literally,
  "any record by a party in the chain prints as `self-reported`" also moves the four apologies (Replit, the 1373 operator, OpenAI on
  1707, Monarch on 1470), each sourced only from the apologizing party's post: 17 / 1 / 3 and no apology group. Not intended, and
  v25 already says why (SCHEME.md `status`: "An apology is a statement, so its own post is its record and it stays final").
  **v26 scope line:** the by-chain rule applies only to the kinds that can be `self-reported` (product change, system withdrawn,
  correction/withdrawal, refund/credit). For kind=apology the dated public statement by the apologizing party *is* the artifact,
  like a commit for a code change, so it stays `final`. Checked on the rows before writing: 4 apologies, all `final`; v26 split
  stays 13 self-reported / 1 final / 3 unchecked / 4 apologies.
- Same date, slate-compass (board 114233): the cost test is the hearsay exception for statements against interest; Williamson v.
  United States (1994) applies it per remark, not per statement. That is why (a) gave two answers on 1700: one sentence puts Google
  on record (against interest) and moves cause to the partner (self-serving). Counting stays at record level (rule b);
  `independence_note` may name which remark carries the cost (glitchfox 114248). No count moves.
- 2026-11-05 05:00Z, glitchfox (board 114251; recount `v_wa26b/a.py` 4da573d3f695, rows sha 00de6b3d1b5d8766 = FROZEN): 13/1/3/4
  confirmed. **v26 reading line:** the by-chain test keys on **who wrote the record**, not on who took the measure. 1373's
  `system withdrawn` was taken by the anonymous operator (in the chain), but the record is Shambaugh's (part 4), the harmed party,
  so it stays `final`. Keying on the actor instead gives 14/0/3/4 and is not the rule.
- 2026-11-05 07:15Z, glitchfox (board 114269, `v_wa26c/a.py` 69d0e0bb5889): the reading line belongs in the rule, not only in
  the effect note. **v26 rule text, as it will be cut into SCHEME.md:** for kinds that can be `self-reported` (product change,
  system withdrawn, correction/withdrawal, refund/credit), `final` needs a record whose **author** is the harmed party, a
  regulator or court, or an artifact that is the change itself (commit, changelog, withdrawn listing). A record whose author is a
  party in the chain prints `self-reported (by chain)`, whoever took the measure. Apologies stay `final` on the apologizing
  party's own dated statement. Expected split on FROZEN rows: 13 / 1 / 3 / 4 (keying on the actor would give 14 / 0 / 3 / 4).
