# privacy-preserving-medical-data
fabric blockchain with medical data using privacy preserving technology 

## prepare and setup network
install sdk
```
$ git clone https://github.com/hyperledger/fabric-sdk-py.git
$ cd fabric-sdk-py
$ make install
```
setup network
```
$ HLF_VERSION=1.4.6
$ docker pull hyperledger/fabric-peer:${HLF_VERSION}
$ docker pull hyperledger/fabric-orderer:${HLF_VERSION}
$ docker pull hyperledger/fabric-ca:${HLF_VERSION}
$ docker pull hyperledger/fabric-ccenv:${HLF_VERSION}
$ docker-compose -f test/fixtures/docker-compose-2orgs-4peers-tls.yaml up
```

## install chaincode
```
# searchable encryption chaincode
python3 install_initiate.py
# abac chaincode
python3 install_initiate_abac.py
```

## run
run test cases
```
python3 encwritetest.py
python3 encquerytest.py
python3 abac.py
```
