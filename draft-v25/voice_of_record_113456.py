"""slate-compass #113456: which mode=voluntary codes rest only on the acting party's own account?
Hand classification of each consequence's src (04.11 ~06:00Z, errata), printed with counts. Classes:
(04.11 ~18:00Z: base switched from the stale v20-era working copy to the published ../rows/aiid_agents.jsonl,
 which carries date_event, the 1649 90-day check and its two voluntary fixes, and 1441's harmed recode.)
(v25 r1, 04.11: 1563 KPMG moved unchecked -> self-only, spokesperson verbatim with the act stated as done.)
  speech-act  : the consequence IS a statement (apology); the party's post is the primary record
  self-only   : a change in the world (product change, withdrawal, refund) known only from the acting party's words
                (incl. wires relaying them)
  independent : a record by someone other than the acting party shows the change
  unchecked   : already coded unchecked"""
import json, collections
CLS = {  # (event_id prefix, kind) -> class
 ('aiid-1152', 'apology'): 'speech-act', ('aiid-1152', 'product change'): 'self-only', ('aiid-1152', 'refund/credit'): 'unchecked',
 ('aiid-1373', 'apology'): 'speech-act', ('aiid-1373', 'system withdrawn'): 'independent',  # Shambaugh part 4 (harmed party)
 ('aiid-1784', 'product change'): 'self-only', ('aiid-1751', 'product change'): 'self-only', ('aiid-1633', 'product change'): 'self-only',
 ('aiid-1707', 'apology'): 'speech-act', ('aiid-1707', 'product change'): 'self-only', ('aiid-1707', 'refund/credit'): 'unchecked',
 ('aiid-1470', 'apology'): 'speech-act', ('aiid-1563', 'correction/withdrawal'): 'self-only', ('aiid-1442', 'product change'): 'self-only',
 ('aiid-1604', 'product change'): 'self-only', ('aiid-1627', 'product change'): 'self-only', ('aiid-1628', 'product change'): 'self-only',
 ('aiid-1629', 'product change'): 'self-only', ('aiid-1700', 'product change'): 'self-only',
 ('aiid-1649', 'product change', 'Meta'): 'self-only',  # Meta retrospective 2026-08-14, Meta's own account
 ('aiid-1649', 'product change', 'Irregular'): 'unchecked'}  # Irregular's fix told by others; its own paper not read
def cls(eid, x):
  return CLS.get((eid[:9], x['kind'], x['party'].split()[0]), CLS.get((eid[:9], x['kind'])))
def main():
  c = collections.Counter(); fin = collections.Counter()
  for l in open('aiid_agents_v25rows.jsonl'):
      r = json.loads(l)
      for x in r['consequences'] or []:
          if x.get('mode') != 'voluntary': continue
          k = cls(r['event_id'], x); assert k, (r['event_id'], x['kind'])
          c[k] += 1; fin[(k, x['status'])] += 1
  print('voluntary consequences:', sum(c.values()), dict(c))
  print('by class and status:', dict(fin))

if __name__ == '__main__':
    main()
