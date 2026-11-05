import unittest
from sse_cursor_ledger.core import run
class RedeliveryTests(unittest.TestCase):
 def test_redelivery_is_not_discarded(self):
  x=run({'connections':[{'chunks':['id: a\ndata: one\n\n']},{'chunks':['id: a\ndata: one\n\nid: a\ndata: two\n\n']}]})
  self.assertEqual(len(x['events']),3);self.assertEqual(x['identical_id_payload_redeliveries'],[{'id':'a','connection':1,'event_index':1}]);self.assertEqual(len(x['reused_id_payload_changes']),1)
 def test_idless_not_deduplicated(self):
  x=run({'connections':[{'chunks':['data: x\n\ndata: x\n\n']}]});self.assertEqual(x['identical_id_payload_redeliveries'],[])
