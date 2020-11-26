import asyncio
from hfc.fabric import Client
from datetime import datetime
import time
import threading
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
# gopath = os.path.normpath(os.path.join(
#                       os.path.dirname(os.path.realpath('__file__')),
#                       'test/fixtures/chaincode'
#                      ))
gopath = os.path.normpath(os.path.join(
                      os.path.dirname(os.path.realpath('__file__')),
                      'cc'
                     ))
os.environ['GOPATH'] = os.path.abspath(gopath)

times = 100

def exec_abac():
  args = ['r1', 'd1','read','192.168.1.100','linux']
  response = loop.run_until_complete(cli.chaincode_invoke(
                 requestor=org1_admin,
                 channel_name='businesschannel',
                 peers=['peer0.org1.example.com'],
                 args=args,
                 cc_name='abac',
                 transient_map=None, # optional, for private data
                 # wait_for_event=True, # for being sure chaincode invocation has been commited in the ledger, default is on tx event
                 #cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
                 ))
  # print(response)

for loops in range(0,5):
  
  threads = []
  tstart = datetime.now()

  for i in range(20):
    texec = threading.Thread(target=exec_abac)
    threads.append(texec)

  for t in threads:
    t.daemon = True
    t.start()

  time.sleep(1)

  for t in threads:
    t.join()


  tend = datetime.now()
  print((tend-tstart))
