#!/usr/bin/env python3
"""Who Answers #596: rebuild the candidate frame by what happened, not by the word "agent".

Labels every AIID incident dated 2025-01-01 or later (snapshot data/aiid/incidents.csv) with a second model
(gpt-5-mini, recall aid only): ACTION = the description says an AI system itself took a step in the world beyond
producing content for a human reader (ran code or commands, changed/deleted/created data or files, sent messages or
posts on its own, moved money, bought, accessed or intruded into systems, used tools in a multi-step task);
CONTENT = AI output (text, image, voice, video, a chatbot answer) that a human read, published or acted on;
PHYSICAL = a vehicle or robot; NONE = no AI step in the chain. Every ACTION row not among the 51 is then read by hand.
Output: frame_labels.jsonl (one row per incident) and a summary on stdout.
"""
import csv, json, os, sys, importlib.machinery, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_loader('oa', importlib.machinery.SourceFileLoader('oa', os.path.expanduser(os.environ.get("OA_TOOL", "~/work/tools/oa"))))
oa = importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)

MODEL = 'gpt-5-mini'; OUT = os.path.join(HERE, 'frame_labels.jsonl'); BATCH = 25
PROMPT = """Label each AI incident below with exactly one label, from the description only:
ACTION: an AI system itself took a step in the world beyond producing content for a human reader: ran code or shell
commands, changed/deleted/created data or files, sent messages, emails or posts on its own, moved money or traded,
made a purchase or booking, accessed or broke into computer systems, used tools in a multi-step task. Include cases
where a human directed the system but the system performed the steps (attacks run by an AI agent count as ACTION).
CONTENT: the AI produced text, images, audio, video or an answer, and the harm came through a human reading,
publishing or acting on it (deepfakes, hallucinated citations, chatbot advice, generated ads).
PHYSICAL: an autonomous vehicle, drone or robot moving in the physical world.
NONE: no AI system output or action is in the causal chain (e.g. a leaked database of an AI company).
Return only JSON: {"labels": [{"id": "<incident_id>", "label": "ACTION|CONTENT|PHYSICAL|NONE", "why": "<=12 words"}]}
Incidents:
"""

def main():
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'data/aiid/incidents.csv'))) if r['date'] >= '2025-01-01']
    done = {}
    if os.path.exists(OUT):
        for l in open(OUT):
            d = json.loads(l); done[d['id']] = d
    todo = [r for r in rows if r['incident_id'] not in done]
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        text = '\n'.join(f"[{r['incident_id']}] {r['title']} :: {r['description'][:700]}" for r in chunk)
        d = oa.call('/responses', {'model': MODEL, 'input': PROMPT + text})
        out = ''.join(c.get('text', '') for o in d.get('output', []) if o.get('type') == 'message' for c in o.get('content', []))
        oa.log('ask', MODEL, {'question': f'whoanswers frame_sweep batch {i // BATCH}'}, d.get('usage'))
        try:
            labs = json.loads(out[out.index('{'):out.rindex('}') + 1])['labels']
        except Exception as e:
            print('parse fail batch', i // BATCH, e, out[:200], file=sys.stderr); continue
        ids = {r['incident_id'] for r in chunk}
        with open(OUT, 'a') as f:
            for x in labs:
                if str(x.get('id')) in ids:
                    f.write(json.dumps({'id': str(x['id']), 'label': x.get('label'), 'why': x.get('why', '')}) + '\n')
        print('batch', i // BATCH, 'ok', len(labs), flush=True)
    labels = {}
    for l in open(OUT):
        d = json.loads(l); labels[d['id']] = d
    cand = {json.loads(l)['incident_id'] for l in open(os.path.join(HERE, 'agent_candidates.jsonl'))}
    from collections import Counter
    print('rows', len(rows), 'labelled', len(labels), Counter(d['label'] for d in labels.values()))
    act = {i for i, d in labels.items() if d['label'] == 'ACTION'}
    print('ACTION in 51:', len(act & cand), ' ACTION not in 51:', len(act - cand), ' 51 not labelled ACTION:', len(cand - act))
    title = {r['incident_id']: r['title'] for r in rows}
    for i in sorted(act - cand, key=int): print('NEW', i, title.get(i, '')[:110])
    for i in sorted(cand - act, key=int): print('51-not-ACTION', i, labels.get(i, {}).get('label'), title.get(i, '')[:90])

if __name__ == '__main__':
    main()
