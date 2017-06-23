#!/usr/bin/env python
import msgflo

class logger(msgflo.Participant):
  def __init__(self, role):
    d = {
      'component': 'eva/logger',
      'label': '',
      'icon': 'star-o',
      'inports': [
        { 'id': 'in', 'type': 'any' },
      ],
      'outports': [],
    }
    msgflo.Participant.__init__(self, d, role)

  def process(self, inport, msg):
    print('%s' % msg.data)
    self.ack(msg)

if __name__ == '__main__':
  msgflo.main(logger)
