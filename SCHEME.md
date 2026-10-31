# Who Answers — coding scheme v18 (2026-10-31, not frozen)

v1 -> v2: all 17 points of a second-model review (fable-scheme-v1.txt) applied. Main changes: a bearer exists only
where a consequence is recorded; `reachable` (who the deciding forum could touch) next to every bearer count;
consequence split by mode (imposed / voluntary / absorbed); the harmed party can be the bearer; dedup by event.

v11 -> v12 (fable-scheme-v11.txt, three blocking points): Charlotin rows carry a derived `(filer, professional-duty)`
claim; dismissals on the law (failure to state a claim, immunity, anti-SLAPP) are `cleared` when they end the claim,
leave to amend is `pending`; a claim known only from press or summaries is `unchecked` (U only).
v12 -> v13 (fable-scheme-v12.txt, four blocking points): Charlotin fields are the record for Charlotin; the forum-record
test runs before step 0; `other` maps like `unstated`; employer discipline needs the employer's own statement.
v13 -> v14 (fable-scheme-v13.txt, four blocking points): press-only claims are coded with `read: no`; final and
cleared need the forum docket read after the appeal period; P, R, U are per bucket; both tests of step 6 run first;
consequence rows name `party` and carry a single-role bearer.
v14 -> v15 (fable-scheme-v14.txt, four blocking points): an unread claim or row poisons a bucket only when nothing
deciding that bucket was read; finality is read in the forum's docket or register or the reviewing court's; leave to
amend clears only through a closing judgment; an employer's responsibility for its staff's filing is professional-duty.
v15 -> v16 (fable-scheme-v15.txt, one blocking point): employer discipline is final when the employer's statement
records the measure as taken.
v16 -> v17 (fable-scheme-v16.txt, three points): any step-6 record can show discipline taken; a `read: no` claim
takes the summary's ground; a verbatim attributed employer statement in press counts.
v17 -> v18 (fable-scheme-v17.txt, narrow test: only points that move a count on coded rows or the 51 AIID agent
candidates): `intent` defined, with `attack` split from `misuse`; AIID incident = one event unless it aggregates
independent deployers; `out-of-scope` for incidents with no AI action in the chain.

Unit: one **event** = one harmful episode attributed (in part) to an AI system. Sources give *records* (a court
decision, an incident page, a filing); several records can belong to one event (`event_id`, cross-source) and one
person can appear in many events (`person_id`, within source). Headline counts are events, never rows.

## Event fields

| field | values | rule |
|---|---|---|
| `event_id`, `records` | id; list of (source, source id) | Mata v. Avianca in Charlotin + AIID + press = one event. Every lawsuit or regulator record is matched against both Charlotin and AIID before coding; `records` carries the match or an explicit negative with the snapshot date checked |
| `unit_type` | event, pattern, practice, out-of-scope | discrimination suits, GDPR fines, FTC orders are pattern/practice; reported apart. An AIID incident is one `event` whatever its victim count; it is `pattern` only when its text names no single dated episode and aggregates independent deployers or users (AIID 1734, 1774). `out-of-scope`: no AI system's output or action is in the causal chain (a leaked database of an AI company, AIID 1364); counted beside T |
| `intent` | error, autonomous-action, misuse, attack | **headline uses error + autonomous-action only**; misuse and attack are reported apart, each with its own count. `misuse`: the harmful step was the purpose of the operator or user who directed the system (deepfake fraud, jailbreak tests such as AIID 1238). `attack`: an outsider caused the harmful step through the system (prompt injection, malware coercing an agent, agent-run intrusions: AIID 1003, 1210). `autonomous-action`: the system took a step nobody instructed. `error`: an instructed task produced a wrong output or decision (AIID 1334: users asked for an identification, the fabricated face and name were not their purpose). Precedence when several apply: out-of-scope, then pattern/practice, then attack, then misuse |
| `harm` | misinformation-to-court, misinformation-about-person, financial, physical, psychological, privacy, discrimination, property/data, other | as the record names it |
| `harmed` | court/public, client, user, third party, operator-self | `operator-self`: agent harmed its own operator (deleted DB) |
| `n_harmed` | 1, 2-10, 11-1000, >1000, unknown | |
| `chain` | ordered list: developer (foundation model maker) -> vendor(s) (wrappers, resellers) -> deployer -> user | CoCounsel = vendor, its base model = developer; the party that itself serves the product to the user or outsider holds the deployer role too, even when it is also the developer (OpenAI serving ChatGPT) |
| `autonomy` | advisory, acted-with-approval, acted-without-approval | Air Canada chatbot = advisory |
| `operator` | user-chosen, deployer-integrated | |
| `permission_source` | user-task-grant, operator-standing-config, vendor-default, unknown | autonomous-action events only: who granted the permission the agent used for the harmful step (slate-compass, #109799). Report-only: never enters k, s or N; cross-tabbed with bearer to show whether users pay for defaults a vendor chose |
| `tool_named` | yes, disputed, no | Thomson Reuters rows = disputed |
| `vendor_voice` | n/a (no tool named), none, denial, acknowledgment, fix-announced | |
| `claims` | list of (party, ground): one entry per ground pleaded or decided against each named party or respondent in the forum of one of `records` | ground = the cause of action or duty pleaded or ruled on as such: building-the-model (product liability, design defect, negligent development), operating-or-publishing (defamation, misrepresentation, negligence or consumer claims against the service as offered), professional-duty (the filer's own professional obligations, and an employer's responsibility for its staff member's filing), other, unstated (the record names none). Facts a court weighs inside another ground's element (design care as evidence of a publisher's fault) do not create a ground. Each entry carries `read`: yes (the forum record or Charlotin's fields were read) or no. A claim known only from press, trackers or summaries is coded with `read: no`; it makes the bucket reachable, resolves `unchecked`, and the number of such entries is printed beside M. A `read: no` entry takes the ground the summary names, or `unstated` if it names none |
| `reachable` | derived per bucket from `claims` (see Headline), never coded by hand | |
| `last_checked` | date the forum's own docket or decision was last read (not a tracker or press summary); a `pending` resolution is published only with such a check within the publication window; `imposed-final` and `cleared` need a docket read after the appeal period (step 1, step 5). Tracker appeal checks are not accepted | |

## Consequence rows (zero or more per event)

| field | values |
|---|---|
| `party` | the named party bearing the row (org_id or person_id) |
| `bearer` | one role per row: user, employer (firm/hospital/company whose staff used the tool), deployer (puts AI in front of outsiders), vendor, developer, harmed (absorbed the loss) |
| `mode` | imposed (court, regulator, employer discipline), voluntary (refund, apology, fix by the party itself), absorbed (loss left where it fell) |
| `kind` | warning, admonishment, fine-to-court, costs-or-damages-to-party, professional sanction, referral (pending, not a sanction), dismissal-as-sanction, striking, injunction/order, settlement, refund/credit, correction/withdrawal, product change, system withdrawn, apology |
| `amount`, `currency`, `payee` | as recorded; payee: court, opposing party, harmed, fund, unknown |
| `status` | final (step 1 finality test; for a voluntary settlement, the record shows the claim ended), pending (incl. appealed), unchecked (known only from press or summaries, or finality not read) — per consequence, not per event |
| `claim` | the (party, ground) entry of `claims` this consequence answers; one row per bearing party and role (a party holding two roles gets two rows); `(party, *)` answers every claim against that party (a settlement with no stated ground) |

No consequence recorded -> **no row**; resolution follows the Headline steps (cleared, not-reached, no-claim or unchecked). Never infer a bearer.

## Rules

1. Code what the record says. A consequence I expect but cannot source is not coded.
2. `harmed/absorbed` needs a dated check >= 90 days after the event that found no imposed or voluntary consequence.
3. Sealed settlement = `settlement`, amount unknown.
4. A product change counts for vendor/developer only if they link it to the event.
5. Charlotin: Party -> person role; a bearer row only when Outcome, Monetary Penalty or Professional Sanction is
   non-empty; bar referrals coded `referral`, not `professional sanction`. Pro se rows (user = client = harmed) are
   reported apart from lawyers. Charlotin's fields are the record for Charlotin rows: step 6's tracker clause applies
   to AIID and court records only (printed as a known bias: Charlotin's own reading of each decision is trusted).
6. Same-party agentic incidents (agent harmed its own operator) default to `absorbed` unless a refund/fix is recorded.

## Headline (the only cross-party comparison published)

Review history: v1 -> v11 through ten blocking-only reviews by a second model (fable-scheme-v1..v10.txt; 17, 6, 6, 5,
4, 4, 2, 2, 3, 5 points, all applied) plus one board point (zenith-claude, #109766: code the ground of liability, not only
the defendant's name). This section is the consolidated rule; older wordings are void.

**Scope.** Per source (Charlotin, AIID), never pooled. `unit_type=event`, intent error or autonomous-action.
Pattern/practice events with an imposed-final consequence on a model maker (FTC, GDPR) are excluded and their count
printed beside the share. Lawsuit and regulator records attach to events as records, or are reported as raw counts
with their collection rule, never as a share.

**Buckets** (a party may hold several chain roles; all three printed): *model maker* = any party with a developer or
vendor role; *operator* = user + employer, **pro se excluded** (their count and own k/N printed beside it);
*deployer-only*.

**Ground decides the bucket, through the claim.** Each `claims` entry maps to one bucket: building-the-model ->
model maker; operating-or-publishing -> deployer-only (operator, if the party is a user or employer);
professional-duty -> operator (pro se apart). `unstated` maps to every bucket the party holds a chain role in, and
the number of such entries is printed beside each share. `other` maps like `unstated` and is counted in the same
printed number. A party with several roles (xAI running the Grok account)
is reachable in a bucket only through a claim whose ground maps there. Resolution steps 1-5 run per bucket on that
bucket's claims and the consequence rows answering them only. A record that imposes on one ground and rejects another
on the merits gives `imposed-final` in one bucket and `cleared` in the other; one that imposes on one ground and is
silent on another gives `not-reached` in the silent bucket.

**reachable** (per bucket) = at least one `claims` entry maps to the bucket (a claim was actually brought on that
ground). In Charlotin every row carries a `(filer, professional-duty)` claims entry, because the court's notice of the
hallucination is the forum raising the filer's own duty; so the filer is reachable by derivation, not by hand.

**resolution**, per event and bucket, by precedence across all forums and parties in the bucket. Both tests of step 6
(forum record, and a dated check >= 90 days after the event) run first: steps 0 to 5 use only claims and consequences read in the forum's own record (or Charlotin's fields);
anything else leaves the bucket `unchecked`. A `read: no` claim or `status: unchecked` consequence leaves the bucket
`unchecked` only when no forum record deciding or ending a claim in that bucket was read; otherwise it is ignored for
steps 0 to 5 and its count is printed beside R and N.
0. `no-claim` — the bucket is not in `reachable`. Outside N, P, R and U; counted only in T minus M. A voluntary
   refund, apology or fix with no claim brought stays `no-claim` (it is printed as a separate count of voluntary
   responses, never as `settled`). Employer discipline of a staff member makes that person reachable in the operator
   bucket: the employer is the forum.
1. `imposed-final` — a final imposed consequence in the bucket (answering one of the bucket's claims). Final only when
   the docket or register of the forum, or of the court to which an appeal or review would lie, read after the appeal
   period, shows no appeal or review, or the record states the ruling is unappealable, or a finality certificate is in
   the record; employer discipline is final when a step-6 record of the discipline (the employer's statement, or the
   court or bar record noting it) records the measure as taken;
   a measure announced as proposed, under review or reversed is `pending`;
   docket showing an appeal -> `pending`; docket not read for appeal -> `unchecked`. Charlotin rows: Charlotin's fields
   decide finality (the printed Charlotin bias). Referral, order to show cause, hearing set, or any step inviting a
   later decision is never final. Interim or preliminary relief (TRO, preliminary injunction, einstweilige
   Verfügung) is `pending` until the record shows a final judgment, a closing declaration, or that the challenge
   period lapsed unchallenged.
2. `pending` — a claim in the bucket still live and nothing imposed-final. Beside the share print how many N events
   still have another live claim in the bucket.
3. `settled` — claim ended with the party bearing a settlement, refund, or a fix it links to the event. A settlement
   is `settled` only when the record shows the claim ended (dismissal entered or settlement approved); an announced
   settlement or one in principle is `pending`.
4. `dropped` / `not-reached` — plaintiff-initiated or without-prejudice dismissal with no reason; dismissal for
   jurisdiction, standing, arbitration, mootness; any stipulated dismissal with prejudice (never `cleared`).
5. `cleared` — the record states a merits or sanctions ruling with nothing imposed. A ruling that the claim fails as a
   matter of law or fact on its pleaded ground (failure to state a claim, immunity such as Section 230, privilege,
   First Amendment, anti-SLAPP) is `cleared` when it ends the claim; the same finality test as step 1 applies (no
   appeal on the forum docket read after the appeal period, else `pending` or `unchecked`); a dismissal with leave to amend is `pending` until
   the amendment deadline lapses unused, then `cleared` once a closing judgment passes the step 1 finality test; until
   then `pending`. In Charlotin only when the
   Outcome records that the court considered sanctions and declined; a hallucination merely noted is `not-reached`.
6. `unchecked` — no dated check >= 90 days after the event, or a claim or consequence known only from press, trackers
   or law-firm summaries (the forum's own record not read). Unchecked buckets enter U and nothing else. For employer
   discipline the forum record is the employer's own statement, on its channels or quoted verbatim and attributed to
   it in press (a paraphrase alone is not), or a court or bar record noting the
   discipline.

**N** = events with resolution imposed-final, settled or cleared, per bucket. P, R and U are per bucket too, printed
beside that bucket's N; an event with claims in two buckets can be in N of one and P of the other.

**k** counts only events with resolution imposed-final, and imposed-final has one test for both: a consequence row
with `mode=imposed` and `status=final` (whatever its `kind`). **s** counts settled; k + s <= N; k_sub + k_warn = k.
**k split** by the most severe imposed-final row, mapping every `kind` when imposed:
*substantive* = fine-to-court, costs-or-damages-to-party, professional sanction (all forms: reprimand, censure,
suspension, disqualification, ordered training, client-notification order), injunction/order, dismissal-as-sanction,
ordered refund/credit, ordered product change, ordered system withdrawal;
*warning-level* = warning, admonishment, striking, ordered correction/withdrawal (incl. an order to refile), ordered
apology. Referral is never final. Settlement is agreed, not imposed: code it `mode=voluntary`, it goes to s. Rows with `mode=voluntary` never
enter k, whatever their kind.

**Clustering.** Beside every CI: distinct parties D in the bucket (`org_id`, `person_id`); no CI when D < 5.

**Sentence**, per source: "Of N events in which a claim was brought against the model maker and decided or settled,
k ended with an imposed consequence on it, down to a warning (k_sub substantive; CI; D distinct parties), and s were
settled; the operator (lawyers and other non-pro-se filers): k2 of N2 (same split); deployer-only: k3 of N3; pro se
apart: k4 of N4; with each bucket its own pending P, dropped or not reached R, unchecked U; and in M of the T events in this scope and source a
claim was brought against the model maker on a model-building ground at all." M = events where the model maker bucket
is in `reachable`; beside it print the count of events where any developer or vendor party was sued on any ground,
and how many of the M rest on a `read: no` claim.

## Known biases (printed next to every number)
- Charlotin includes a case only when a court noticed the hallucination; the court cannot reach the model maker.
- AIID is press-driven, US-heavy; consequences need follow-up, so `unknown` will dominate until rechecked.
- Lawsuits against developers are mostly pending: a censored series, not "developers never pay".
- Tool identification in court records is self-reported and overweights ChatGPT.
- Charlotin rows trust Charlotin's own reading of each decision (step 6 applies to AIID and court records only).
