#!/usr/bin/env python
import msgflo
import logging
import requests

log = logging.getLogger(__name__)

class blockchain(msgflo.Participant):
  def __init__(self, role):
    d = {
      'component': 'eva/blockchain',
      'label': '',
      'icon': 'link',
      'inports': [
        { 'id': 'in', 'type': 'int' },
        { 'id': 'name', 'type': 'string' }
      ],
      'outports': [
        { 'id': 'history', 'type': 'object' },
      ],
      
    }
    self.name = 'temp'
    msgflo.Participant.__init__(self, d, role)

  def process(self, inport, msg):
    if inport == 'name':
      self.name = msg.data
      self.ack(msg)
      return
    
    if inport == 'in':
      url = 'https://5560be7a10ba4ceea786ecb2b4ade5aa-vp0.us.blockchain.ibm.com:5002/registrar'
      resp = requests.post(url, json={
  		"enrollId": "admin",
		"enrollSecret": "f9c649a1ef"
	  })
      if 'OK' in resp.json().keys():
        blockchain_data = {
          "jsonrpc": "2.0",
          "method": "invoke",
          "params": {
            "type": 1,
            "chaincodeID": {
              "name": "3aeb9793d67968f966f2b093c361c70cdbf7a2813a02f7a5da344386580d3b519899b73003b335c587e3d016d44b54eb7d8030bddddbc3e9abf05db81c20eaef"
            },
            "ctorMsg": {
              "function": "write",
              "args": [
                self.name, str(msg.data)
              ]
            },
            "secureContext": "admin"
          },
          "id": 3
        }
        url2 = 'https://5560be7a10ba4ceea786ecb2b4ade5aa-vp0.us.blockchain.ibm.com:5002/chaincode'
        resp2 = requests.post(url2, json=blockchain_data)
        self.send('history', resp2.json())
    self.ack(msg)

if __name__ == '__main__':
  msgflo.main(blockchain)
