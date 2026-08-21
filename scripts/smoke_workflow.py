import json,os,re,time
from genlayer_py import create_client,create_account
from genlayer_py.chains import testnet_bradbury
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));W=os.path.abspath(os.path.join(R,'..','..','..','..'))
def v(n):return re.search(rf'^\s*{n}\s*=\s*"?([^"\r\n]+)',open(os.path.join(W,'accounts.env'),encoding='utf-8').read(),re.M).group(1).strip()
def send(fn):
 for p in (0,3,7,12):
  if p:time.sleep(p)
  try:return fn()
  except Exception as e:last=e
 raise last
 a=create_account(account_private_key=v('ACCOUNT_3_GENLAYER_PRIVATE_KEY'));cl=create_client(chain=testnet_bradbury,account=a);addr=json.load(open(os.path.join(R,'night-receipt.json')))['receipt']['sigil'];i='DT-'+str(int(time.time()));h=send(lambda:cl.write_contract(address=addr,function_name='bind_dream',args=[i,'A red elevator descends through a sea that remembers every passenger.',['red elevator','salt rain'],['name the lost station','return the brass token'],'https://en.wikipedia.org/wiki/Dream']));print('bindTx',h,flush=True);cl.wait_for_transaction_receipt(transaction_hash=h,status='ACCEPTED',retries=80,interval=20000);g=send(lambda:cl.write_contract(address=addr,function_name='wake',args=[i,['name the lost station','return the brass token']]));print('wakeTx',g,flush=True);cl.wait_for_transaction_receipt(transaction_hash=g,status='ACCEPTED',retries=80,interval=20000);assert cl.get_transaction(transaction_hash=h).get('tx_execution_result_name')=='FINISHED_WITH_RETURN';assert cl.get_transaction(transaction_hash=g).get('tx_execution_result_name')=='FINISHED_WITH_RETURN'
