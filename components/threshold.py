#!/usr/bin/env python
import msgflo

class threshold(msgflo.Participant):
  def __init__(self, role):
    d = {
      'component': 'eva/threshold',
      'label': 'Send out an object when in is higher than thresh.',
      'icon': 'star-o',
      'inports': [
        { 'id': 'in', 'type': 'int' },
        { 'id': 'thresh', 'type': 'int' },
      ],
      'outports': [
        { 'id': 'out', 'type': 'boolean' },
      ],
    }
    self.active = False
    self.thresh = 255
    msgflo.Participant.__init__(self, d, role)

  def process(self, inport, msg):
    if inport == 'thresh':
      self.thresh = msg.data
      
    if inport == 'in':
    	if self.active == True:
          if msg.data < self.thresh:
            self.send('out', False)
            self.active = False
        else:
          if msg.data >= self.thresh:
            self.send('out', True)
            self.active = True
            
    self.ack(msg)

if __name__ == '__main__':
  msgflo.main(threshold)
