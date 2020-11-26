import asyncio
import threading
import time
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
import hashlib
from hfc.fabric import Client
import json
from datetime import datetime
import nest_asyncio
nest_asyncio.apply()

loop = asyncio.get_event_loop()

cli = Client(net_profile="test/fixtures/network.json")
org1_admin = cli.get_user('org1.example.com', 'Admin')

# Make the client know there is a channel in the network
cli.new_channel('businesschannel')

# Install Example Chaincode to Peers
# GOPATH setting is only needed to use the example chaincode inside sdk
import os
gopath_bak = os.environ.get('GOPATH', '')
gopath = os.path.normpath(os.path.join(
                      os.path.dirname(os.path.realpath('__file__')),
                      'cc'
                     ))
os.environ['GOPATH'] = os.path.abspath(gopath)

sk = b'0:GtPWlZ/XlEv80+nWa/oZMtQRtYY='

Hash1pre = hashlib.md5

param_id = 'SS512'
group = PairingGroup(param_id)

def Hash1(w):
    # 先对关键词w进行md5哈希
    hv = Hash1pre(str(w).encode('utf8')).hexdigest()
    # print(hv)
    # 再对md5值进行group.hash哈希，生成对应密文
    # 完整的Hash1由md5和group.hash组成
    hv = group.hash(hv, type=G1)
    return hv

Hash2 = hashlib.sha256

def TdGen(sk, w, param_id='SS512'):
    group = PairingGroup(param_id)
    sk = group.deserialize(sk)
    td = Hash1(w) ** sk
    # 对陷门进行序列化
    return group.serialize(td)

def Test(td, c, param_id='SS512'):
    group = PairingGroup(param_id)
    # print(c[0])
    c1 = group.deserialize(c[0])
    c2 = c[1]
    # print(c2)
    td = group.deserialize(td)
    return Hash2(group.serialize(pair(td, c1))).hexdigest() == c2


# tstart = datetime.now()
def exec_enc():
  # Query a chaincode
  args = [str(float('-inf')),str(float('inf'))]
  # The response should be true if succeed
  response = loop.run_until_complete(cli.chaincode_query(
                 requestor=org1_admin,
                 channel_name='businesschannel',
                 peers=['peer0.org1.example.com'],
                 args=args,
                 cc_name='queryenc'
                 ))
  # print(response)

  response = json.loads(response)

  # del response[-1]
  # del response[-1]
  # del response[-1]

  # print(response)

  w = "headache"
  td = TdGen(sk, w, param_id='SS512')



  for js in response:
    # print(type(js))
    # print(type(js['key']))
    # print(js['key'].encode(encoding="utf-8"))
    # print(js['valu'])
    c = js['key']
    c = c.encode()
    c = c[1:-1].split(b',')
    c_arr = []
    c_arr.append(c[0][2:-1])
    c_arr.append(c[1][2:-1].decode())

    flag = Test(td, c_arr)
    # print("是否搜索到关键字：", flag)
    # if flag == True:
    #   tend = datetime.now()
      # print("花费时间（微秒）：", (tend-tstart).microseconds)

for loops in range(0,5):
  
  threads = []
  tstart = datetime.now()

  for i in range(20):
    texec = threading.Thread(target=exec_enc)
    threads.append(texec)

  for t in threads:
    t.daemon = True
    t.start()

  time.sleep(1)

  for t in threads:
    t.join()


  tend = datetime.now()
  print((tend-tstart))

