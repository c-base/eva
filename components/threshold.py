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
        { 'id': 'out', 'type': 'object' },
      ],
    }
    self.active = False
    msgflo.Participant.__init__(self, d, role)

  def process(self, inport, msg):
    self.send('out', msg.data)
    self.ack(msg)

if __name__ == '__main__':
  msgflo.main(threshold)
