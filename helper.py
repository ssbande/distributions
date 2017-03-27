staticNodeProbabiity = {
  'i': 0.6,
  'c': 0.7,
  'w': 0.2
}

refNodeNames = {
  'i': {
    'depNode1Name': 'i',
    'depNode2Name': 'is',
    'resNodeName' : 'pi'
  },
  'c': {
    'depNode1Name': 'c',
    'depNode2Name': 'cs',
    'resNodeName' : 'pc'
  },
  'w': {
    'depNode1Name': 'w',
    'depNode2Name': 'ws',
    'resNodeName' : 'pw'
  },
  'r': {
    'depNode1Name': 'o',
    'depNode2Name': 'ts',
    'resNodeName' : 'pr'
  },
  'o': {
    'depNode1Name': 'i',
    'depNode2Name': 'c',
    'resNodeName' : 'po'
  },
  'ts': {
    'depNode1Name': 'c',
    'depNode2Name': 'w',
    'resNodeName' : 'pts'
  }
}

refProbValues = {
  'i': [
    {'i': True,  'is': True, 'pi': 0.6}
  ],
  'c': [
    {'c': True,  'cs': True, 'pc': 0.7}
  ],
  'w': [
    {'w': True,  'ws': True, 'pw': 0.2}
  ],
  'o': [
    {'i': True,  'c': True,  'po': 0.7},
    {'i': True,  'c': False, 'po': 0.4},
    {'i': False, 'c': True,  'po': 0.5},
    {'i': False, 'c': False, 'po': 0.1}
  ],
  'ts': [
    {'c': True,  'w': True,  'pts': 0.6},
    {'c': True,  'w': False, 'pts': 0.05},
    {'c': False, 'w': True,  'pts': 0.5},
    {'c': False, 'w': False, 'pts': 0.1}
  ],
  'r': [
    {'o': True,  'ts': True,  'pr': 0.2},
    {'o': True,  'ts': False, 'pr': 0.4},
    {'o': False, 'ts': True,  'pr': 0.5},
    {'o': False, 'ts': False, 'pr': 0.8}
  ]
}

def generateBooleanForSample(node, sampleVal, depNode1Val, depNode2Val):
  result = False
  nodeNames = refNodeNames[node]
  for nodeValue in refProbValues[node]:
    if(nodeValue[nodeNames['depNode1Name']] == depNode1Val 
    and nodeValue[nodeNames['depNode2Name']] == depNode2Val):

      # If the random value sent to the method is less than the value mentioned in the ref, it is a positive case. Else negative.
      if(sampleVal <= nodeValue[nodeNames['resNodeName']]):
        result = True
        break;
  return result

class Sample(object):
  def __init__(self, i, c, w, o, t, r):
    self.i = i
    self.c = c
    self.w = w
    self.o = o
    self.t = t
    self.r = r