import random
from helper import generateBooleanForSample, weightedSample
print ('===== Monte Carlo Inference of Bayesian Network - Weighted Sampling =====')
iterations = 1000
samples = []

for x in range(0, iterations):
  # Generate Random Nos for each of the node.
  i = 0.6
  c = 0.7
  w = round(random.random(), 2)
  o = round(random.random(), 2)
  t = round(random.random(), 2)
  r = round(random.random(), 2)

  # Get the value whether it is a positive event(true) or a negative event(false) based on the random value generated above.
  iss = True #generateBooleanForSample('i', i, True, True)
  cs = True #generateBooleanForSample('c', c, True, True)
  ws = generateBooleanForSample('w', w, True, True)
  os = generateBooleanForSample('o', o, iss, cs)
  ts = generateBooleanForSample('ts', t, cs, ws)
  rs = generateBooleanForSample('r', i, os, ts)

  weight = i * c * r
  # store all samples in an array.
  samples.append(weightedSample(iss, cs, ws, os, ts, rs, weight))

numerator = 0
denominator = 0
for x in samples:
  if(x.i == True and x.c == True and x.r == True and x.t == True):
    numerator += x.weight

  if(x.i == True and x.c == True and x.r == True):
    denominator += x.weight

print('numerator: ' + str(numerator))
print('denominator: ' + str(denominator))

finalProbability = numerator / float(denominator)
print('final probability: ' + str(finalProbability))