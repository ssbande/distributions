import random

p_i = 0.6
p_c = 0.7
p_w = 0.2 

p_o_ixc = 0.7
p_ts_cxw = 0.6 
p_r_oxts = 0.2

eventOccurence = [True, False]

refNodeNames = {
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

staticNodeProbability = {
  'i': 0.6,
  'c': 0.7,
  'w': 0.2
}

refProbValues = {
  'r': [
    {'o': True,  'ts': True,  'pr': 0.2},
    {'o': True,  'ts': False, 'pr': 0.4},
    {'o': False, 'ts': True,  'pr': 0.5},
    {'o': False, 'ts': False, 'pr': 0.8}
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
  ]
}

def getStaticNodeProbability(node):
  return staticNodeProbability[node]

def getAptProbability(node, depNode1Val, depNode2Val):
  probability = 0
  nodeNames = refNodeNames[node]
  for nodeValue in refProbValues[node]:
      if(nodeValue[nodeNames['depNode1Name']] == depNode1Val 
      and nodeValue[nodeNames['depNode2Name']] == depNode2Val):
        probability = nodeValue[nodeNames['resNodeName']]
        break;
  return probability
    
      

    
    
