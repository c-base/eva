#!/usr/bin/env python
import msgflo
import logging
import requests

class blockchain(msgflo.Participant):
  def __init__(self, role):
    d = {
      'component': 'eva/blockchain',
      'label': '',
      'icon': 'star-o',
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
      log.info(str(resp.content))
      self.send('history', msg.data)
      self.ack(msg)

if __name__ == '__main__':
  msgflo.main(blockchain)
