"""slate-compass #113456: which mode=voluntary codes rest only on the acting party's own account?
Hand classification of each consequence's src (04.11 ~06:00Z, errata), printed with counts. Classes:
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
 ('aiid-1629', 'product change'): 'self-only', ('aiid-1700', 'product change'): 'self-only'}
def main():
  c = collections.Counter(); fin = collections.Counter()
  for l in open('aiid_agents_v20rows.jsonl'):
      r = json.loads(l)
      for x in r['consequences'] or []:
          if x.get('mode') != 'voluntary': continue
          k = CLS[(r['event_id'][:9], x['kind'])]
          c[k] += 1; fin[(k, x['status'])] += 1
  print('voluntary consequences:', sum(c.values()), dict(c))
  print('by class and status:', dict(fin))

if __name__ == '__main__':
    main()
