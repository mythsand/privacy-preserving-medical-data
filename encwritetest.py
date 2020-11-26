import asyncio
from hfc.fabric import Client

from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
import hashlib

Hash1pre = hashlib.md5

param_id = 'SS512'
# [sk, pk] = Setup(param_id)

group = PairingGroup(param_id)

def Hash1(w):
    # 先对关键词w进行md5哈希
    hv = Hash1pre(str(w).encode('utf8')).hexdigest()
    print(hv)
    # 再对md5值进行group.hash哈希，生成对应密文
    # 完整的Hash1由md5和group.hash组成
    hv = group.hash(hv, type=G1)
    return hv

Hash2 = hashlib.sha256

def Setup(param_id='SS512'):
    # 代码符号G1 x G2 →  GT
    group = PairingGroup(param_id)
    # 方案选用的是对称双线性对，故G2 = G1
    g = group.random(G1)
    alpha = group.random(ZR)
    # 生成私钥与公钥并进行序列化
    # Serialize a pairing object into bytes
    sk = group.serialize(alpha)
    pk = [group.serialize(g), group.serialize(g ** alpha)]
    return [sk, pk]


def Enc(pk, w, param_id='SS512'):
    group = PairingGroup(param_id)
    # 进行反序列化
    g, h = group.deserialize(pk[0]), group.deserialize(pk[1])
    r = group.random(ZR)
    t = pair(Hash1(w), h ** r)
    c1 = g ** r
    c2 = t
    # 对密文进行序列化
    # print(group.serialize(c2))
    return [group.serialize(c1), Hash2(group.serialize(c2)).hexdigest()]


param_id = 'SS512'
[sk, pk] = Setup(param_id)

print('pk:',pk)
print('sk:',sk)
print(type(sk))

sk = b'0:GtPWlZ/XlEv80+nWa/oZMtQRtYY='
pk = [b'1:iIKi7xkaI1Xs/yzMqtcPk588DlmxmHrmLXujrY7fU+kfVPs8SbcejZ4O0ppo2Bznq+FqYdTCxWK1DrC04To1nQE=', b'1:CqOW/H/Lj4yJRjctC5EC6D4oQDdckSjWasw9oWj6xeDEcX+dBSo0bLaGD2Vesj1ZEBwYzaGj2JEZyE402Sn/MQE=']


c = Enc(pk, "headache")

# print('c0:',c[0])
# print('c1:',c[1])

# c = Enc(pk, "yes")

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

# The response should be true if succeed
# responses = loop.run_until_complete(cli.chaincode_install(
#                requestor=org1_admin,
#                peers=['peer0.org1.example.com',
#                       'peer1.org1.example.com'],
#                cc_path='github.com/queryenc3',
#                cc_name='queryenc6',
#                cc_version='v1.0'
#                ))

# print(responses)

# # Instantiate Chaincode in Channel, the response should be true if succeed
# args = ['a', '200', 'b', '300']

# # policy, see https://hyperledger-fabric.readthedocs.io/en/release-1.4/endorsement-policies.html
# policy = {
#     'identities': [
#         {'role': {'name': 'member', 'mspId': 'Org1MSP'}},
#     ],
#     'policy': {
#         '1-of': [
#             {'signed-by': 0},
#         ]
#     }
# }
# response = loop.run_until_complete(cli.chaincode_instantiate(
#                requestor=org1_admin,
#                channel_name='businesschannel',
#                peers=['peer0.org1.example.com'],
#                args=args,
#                cc_name='queryenc6',
#                cc_version='v1.0',
#                cc_endorsement_policy=policy, # optional, but recommended
#                collections_config=None, # optional, for private data policy
#                transient_map=None, # optional, for private data
#                wait_for_event=True # optional, for being sure chaincode is instantiated
#                ))
# print(response)

# Invoke a chaincode
args = [str(c), str(1)]
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_invoke(
               requestor=org1_admin,
               channel_name='businesschannel',
               peers=['peer0.org1.example.com'],
               args=args,
               cc_name='queryenc',
               transient_map=None, # optional, for private data
               wait_for_event=True, # for being sure chaincode invocation has been commited in the ledger, default is on tx event
               #cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
               ))

print(response)




# args = ['a','b']
# response = loop.run_until_complete(cli.chaincode_invoke(
#                requestor=org1_admin,
#                channel_name='businesschannel',
#                peers=['peer0.org1.example.com'],
#                args=args,
#                cc_name='queryenc6',
#                fcn='query1',
#                # transient_map=None, # optional, for private data
#                # wait_for_event=True, # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#                #cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
#                ))

# print(response+"what")

# Query a chaincode
# args = ['a','neng']
# # The response should be true if succeed
# response = loop.run_until_complete(cli.chaincode_query(
#                requestor=org1_admin,
#                channel_name='businesschannel',
#                peers=['peer0.org1.example.com'],
#                args=args,
#                cc_name='queryenc6'
#                ))

# print(response)
