import codecs,re,hashlib
from .common import identifier,integer

def run(data):
 connections=data['connections']
 if not isinstance(connections,list)or not 1<=len(connections)<=50:raise ValueError('connections')
 cursor='';retry=None;events=[];receipts=[];seen={};conflicts=[]
 for ci,connection in enumerate(connections):
  chunks=connection['chunks'];encoding=connection.get('encoding','text')
  if not isinstance(chunks,list)or len(chunks)>10000 or encoding not in ('text','hex'):raise ValueError('chunks')
  decoder=codecs.getincrementaldecoder('utf-8')('strict');parts=[];size=0
  for chunk in chunks:
   if not isinstance(chunk,str):raise ValueError('chunk')
   raw=bytes.fromhex(chunk)if encoding=='hex'else chunk.encode('utf-8');size+=len(raw)
   if size>2_000_000:raise ValueError('size')
   parts.append(decoder.decode(raw))
  parts.append(decoder.decode(b'',final=True));text=''.join(parts)
  if text.startswith('\ufeff'):text=text[1:]
  start=cursor;id_buffer=cursor;payload=[];kind='';count=0
  # Last unterminated line and incomplete event are discarded at EOF.
  for line in re.split(r'\r\n|\r|\n',text)[:-1]:
   if not line:
    cursor=id_buffer
    if not payload:continue
    body='\n'.join(payload);event={'connection':ci,'id':cursor,'type':kind or'message','data':body};events.append(event);count+=1
    if cursor:
     digest=hashlib.sha256(body.encode()).hexdigest()
     if cursor in seen and seen[cursor]!=digest:conflicts.append({'id':cursor,'connection':ci})
     seen[cursor]=digest
    payload=[];kind='';continue
   if line.startswith(':'):continue
   name,sep,value=line.partition(':')
   if value.startswith(' '):value=value[1:]
   if name=='data':payload.append(value)
   elif name=='event':kind=value
   elif name=='id'and'\x00'not in value:id_buffer=value
   elif name=='retry'and value and value.isascii()and value.isdecimal()and len(value)<=12:retry=int(value)
  receipts.append({'connection':ci,'request_last_event_id':start or None,'resume_last_event_id':cursor or None,'dispatched':count,'incomplete_event_discarded':bool(payload),'retry_ms':retry})
 return {'events':events,'connections':receipts,'reused_id_payload_changes':conflicts,'final_cursor':cursor,'model':'whatwg_sse_framing_and_reconnect_cursor_not_terminal_response_validation'}
