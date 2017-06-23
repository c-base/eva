#!/usr/bin/env python
import msgflo

class movavg(msgflo.Participant):
  def __init__(self, role):
    d = {
      'component': 'eva/movavg',
      'label': 'Repeat input data without change',
      'icon': 'star-o',
      'inports': [
        { 'id': 'in', 'type': 'int' },
      ],
      'outports': [
        { 'id': 'avg', 'type': 'int' },
      ],
    }
    self.array = [0] * 10
    msgflo.Participant.__init__(self, d, role)

  def process(self, inport, msg):
    self.array.pop()
    self.array.insert(0, msg.data)
    avg_val = sum(self.array) / float(len(self.array))
    self.send('avg', avg_val)
    self.ack(msg)

if __name__ == '__main__':
  msgflo.main(movavg)
