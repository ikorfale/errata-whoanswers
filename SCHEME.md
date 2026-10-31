# Who Answers — coding scheme v9 (2026-10-31, not frozen)

v1 -> v2: all 17 points of a second-model review (fable-scheme-v1.txt) applied. Main changes: a bearer exists only
where a consequence is recorded; `reachable` (who the deciding forum could touch) next to every bearer count;
consequence split by mode (imposed / voluntary / absorbed); the harmed party can be the bearer; dedup by event.

Unit: one **event** = one harmful episode attributed (in part) to an AI system. Sources give *records* (a court
decision, an incident page, a filing); several records can belong to one event (`event_id`, cross-source) and one
person can appear in many events (`person_id`, within source). Headline counts are events, never rows.

## Event fields

| field | values | rule |
|---|---|---|
| `event_id`, `records` | id; list of (source, source id) | Mata v. Avianca in Charlotin + AIID + press = one event |
| `unit_type` | event, pattern, practice | discrimination suits, GDPR fines, FTC orders are pattern/practice; reported apart |
| `intent` | error, autonomous-action, misuse | **headline uses error + autonomous-action only**; misuse (deepfake fraud) is reported apart |
| `harm` | misinformation-to-court, financial, physical, psychological, privacy, discrimination, property/data, other | as the record names it |
| `harmed` | court/public, client, user, third party, operator-self | `operator-self`: agent harmed its own operator (deleted DB) |
| `n_harmed` | 1, 2-10, 11-1000, >1000, unknown | |
| `chain` | ordered list: developer (foundation model maker) -> vendor(s) (wrappers, resellers) -> deployer -> user | CoCounsel = vendor, its base model = developer |
| `autonomy` | advisory, acted-with-approval, acted-without-approval | Air Canada chatbot = advisory |
| `operator` | user-chosen, deployer-integrated | |
| `tool_named` | yes, disputed, no | Thomson Reuters rows = disputed |
| `vendor_voice` | n/a (no tool named), none, denial, acknowledgment, fix-announced | |
| `claims` | list of (party, ground): one entry per ground pleaded or decided against each named party or respondent in the forum of one of `records` | ground: building-the-model, operating-or-publishing, professional-duty, other, unstated |
| `reachable` | derived per bucket from `claims` (see Headline), never coded by hand | |
| `last_checked` | date | |

## Consequence rows (zero or more per event)

| field | values |
|---|---|
| `bearer` | user, employer (firm/hospital/company whose staff used the tool), deployer (puts AI in front of outsiders), vendor, developer, harmed (absorbed the loss) |
| `mode` | imposed (court, regulator, employer discipline), voluntary (refund, apology, fix by the party itself), absorbed (loss left where it fell) |
| `kind` | warning, admonishment, fine-to-court, costs-or-damages-to-party, professional sanction, referral (pending, not a sanction), dismissal-as-sanction, striking, injunction/order, settlement, refund/credit, correction/withdrawal, product change, system withdrawn, apology |
| `amount`, `currency`, `payee` | as recorded; payee: court, opposing party, harmed, fund, unknown |
| `status` | final, pending (incl. appealed) — per consequence, not per event |
| `claim` | the (party, ground) entry of `claims` this consequence answers; a settlement with no stated ground answers every claim against that party |

No consequence recorded -> **no row**, and the event is `outcome=unknown`. Never infer a bearer.

## Rules

1. Code what the record says. A consequence I expect but cannot source is not coded.
2. `harmed/absorbed` needs a dated check >= 90 days after the event that found no imposed or voluntary consequence.
3. Sealed settlement = `settlement`, amount unknown.
4. A product change counts for vendor/developer only if they link it to the event.
5. Charlotin: Party -> person role; a bearer row only when Outcome, Monetary Penalty or Professional Sanction is
   non-empty; bar referrals coded `referral`, not `professional sanction`. Pro se rows (user = client = harmed) are
   reported apart from lawyers.
6. Same-party agentic incidents (agent harmed its own operator) default to `absorbed` unless a refund/fix is recorded.

## Headline (the only cross-party comparison published)

Review history: v1 -> v9 through eight blocking-only reviews by a second model (fable-scheme-v1..v8.txt; 17, 6, 6, 5,
4, 4, 2, 2 points, all applied) plus one board point (zenith-claude, #109766: code the ground of liability, not only
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
the number of such entries is printed beside each share. A party with several roles (xAI running the Grok account)
is reachable in a bucket only through a claim whose ground maps there. Resolution steps 1-5 run per bucket on that
bucket's claims and the consequence rows answering them only. A record that imposes on one ground and rejects another
on the merits gives `imposed-final` in one bucket and `cleared` in the other; one that imposes on one ground and is
silent on another gives `not-reached` in the silent bucket.

**reachable** (per bucket) = at least one `claims` entry maps to the bucket (a claim was actually brought on that
ground). In Charlotin the filer (lawyer or pro se) is always reachable.

**resolution**, per event and bucket, by precedence across all forums and parties in the bucket:
0. `no-claim` — the bucket is not in `reachable`. Outside N, P, R and U; counted only in T minus M. A voluntary
   refund, apology or fix with no claim brought stays `no-claim` (it is printed as a separate count of voluntary
   responses, never as `settled`). Employer discipline of a staff member makes that person reachable in the operator
   bucket: the employer is the forum.
1. `imposed-final` — a final imposed consequence in the bucket (answering one of the bucket's claims). Referral, order to show cause, hearing set, or any step inviting a
   later decision is never final.
2. `pending` — a claim in the bucket still live and nothing imposed-final. Beside the share print how many N events
   still have another live claim in the bucket.
3. `settled` — claim ended with the party bearing a settlement, refund, or a fix it links to the event.
4. `dropped` / `not-reached` — plaintiff-initiated or without-prejudice dismissal with no reason; dismissal for
   jurisdiction, standing, arbitration, mootness; any stipulated dismissal with prejudice (never `cleared`).
5. `cleared` — the record states a merits or sanctions ruling with nothing imposed. In Charlotin only when the
   Outcome records that the court considered sanctions and declined; a hallucination merely noted is `not-reached`.
6. `unchecked` — no dated check >= 90 days after the event.

**N** = events with resolution imposed-final, settled or cleared. Pending, dropped/not-reached and unchecked counts are
printed beside every share.

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
apart: k4 of N4; pending P, dropped or not reached R, unchecked U; and in M of the T events in this scope and source a
claim was brought against the model maker at all."

## Known biases (printed next to every number)
- Charlotin includes a case only when a court noticed the hallucination; the court cannot reach the model maker.
- AIID is press-driven, US-heavy; consequences need follow-up, so `unknown` will dominate until rechecked.
- Lawsuits against developers are mostly pending: a censored series, not "developers never pay".
- Tool identification in court records is self-reported and overweights ChatGPT.
