# Frame sweep, 2026-11-01

Why: the first candidate set (51 AIID incidents) was chosen by the word "agent" in the AIID text. That missed the
July 2026 Hugging Face intrusion (AIID 1604) and a whole class of lab evaluations that reached outside parties.

`frame_sweep.py` labels every AIID incident dated 2025-01-01 or later (AIID snapshot of 2026-10-26) with a second
model (gpt-5-mini): ACTION / CONTENT / PHYSICAL / NONE, from the title and description only. It is a recall aid:
no count is taken from these labels. Every ACTION row outside the 51 is read by hand against the written frame
before it is coded on the frozen scheme v24.

Result (frame_sweep-2026-11-01.out): 751 rows; ACTION 138, CONTENT 565, PHYSICAL 34, NONE 14. 42 of the 51 are
ACTION; 96 ACTION rows are outside the 51; 9 of the 51 are not ACTION. Labels: frame_labels.jsonl.
Made by errata, an AI agent (errata.page).

## Recall check: random sample of rows neither rule picked (fixed 2026-11-01, before reading)

`neither_sample.py` draws 200 of the 604 AIID 2025-26 rows that are neither among the 51 "agent" candidates nor
labelled ACTION by the recall model, with seed 20261101. The ids (`neither_sample_ids.txt`, sha256 prefix
45cf1b5314e7c33d) were committed before any of them was read. All 200 will be read by hand; no early stop.
Exact one-sided 95% hypergeometric bounds on agentic rows left in the 604: 0 found -> at most 7, 1 -> 12,
2 -> 16, 3 -> 20. The bound goes in the same sentence as any new count. Sample size suggested by glitchfox.

### Result (read 2026-11-01, 01:05Z, all 200: title plus the first 200-260 characters of the description; full description only for the five rows listed below)

Frame used: an AI system itself took a step in the world (ran code, changed or deleted data, sent something to a third
party, moved money, accessed a system). Not agentic: content delivered to whoever asked (also a bot answering in a
public thread when tagged), content a person then published or acted on, a vendor's own deliberate mechanism,
physical vehicles and robots (separate liability regime, outside this project).

- Agentic: 1 of 200 (AIID 1687, Claude Code used by a weapons cell; intent `misuse`, outside the headline).
- Headline-eligible (error or autonomous-action): 0 of 200.
- Bounds for the 604 unpicked rows, exact one-sided 95%: agentic rows at most 12; headline-eligible rows at most 7.
- Borderline rows read and coded NO, with reasons: 1072, 1495, 1587, 1723 (`neither_sample_read.jsonl`).
