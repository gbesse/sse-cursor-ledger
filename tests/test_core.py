import unittest
from sse_cursor_ledger import run
class Tests(unittest.TestCase):
 def test_utf8_and_crlf_at_every_byte_boundary(self):
  raw='\ufeffid: é\r\ndata: café\r\ndata: ☕\r\n\r\n'.encode()
  for i in range(len(raw)+1):
   r=run({'connections':[{'encoding':'hex','chunks':[raw[:i].hex(),raw[i:].hex()]}]});self.assertEqual(r['events'][0]['data'],'café\n☕');self.assertEqual(r['final_cursor'],'é')
 def test_incomplete_block_cannot_advance_resume_cursor(self):
  r=run({'connections':[{'chunks':['id: good\ndata: x\n\nid: pending\ndata: y\n']},{'chunks':['data: z\n\n']}]});self.assertEqual([e['id']for e in r['events']],['good','good']);self.assertEqual(r['connections'][1]['request_last_event_id'],'good')
 def test_id_only_blank_block_and_reset_are_effective(self):
  r=run({'connections':[{'chunks':['id: remembered\n\n']},{'chunks':['id:\ndata: x\n\n']}]});self.assertEqual(r['connections'][1]['request_last_event_id'],'remembered');self.assertEqual(r['final_cursor'],'')
 def test_nul_id_retry_comments_and_lone_cr(self):
  r=run({'connections':[{'chunks':[':comment\rretry: 30\rid: good\rdata: x\r\rid: bad\x00id\rdata: y\r\r']}]});self.assertEqual([e['id']for e in r['events']],['good','good']);self.assertEqual(r['connections'][0]['retry_ms'],30);self.assertEqual(len(r['reused_id_payload_changes']),1)
 def test_eof_does_not_dispatch(self):self.assertEqual(run({'connections':[{'chunks':['data: x\n']}]})['events'],[])

class EofDiagnostics(unittest.TestCase):
 def test_unterminated_data_line_is_reported_as_discarded_without_cursor_advance(self):
  r=run({'connections':[{'chunks':['id: a\ndata: x\n\n']},{'chunks':['id: b\ndata: unfinished']}]})
  self.assertEqual(r['final_cursor'],'a');self.assertEqual(len(r['events']),1);self.assertTrue(r['connections'][1]['incomplete_event_discarded']);self.assertTrue(r['connections'][1]['unterminated_line_discarded'])
