from dictionary import getAptProbability, getStaticNodeProbability, eventOccurence
import random

print ('============== Monte Carlo Inference of Bayesian Network With Sampling ===================')
iterations = 1000
# newIterations = 0
totalProbability = 0
for x in range(0, iterations):
  i = random.choice(eventOccurence)
  c = random.choice(eventOccurence)
  w = random.choice(eventOccurence) 
  ts = c & w
  o = i & c
  print('Iteration ' + str(x + 1) + ' ---------------------------------------------------------')
  print("i: " + str(i) + " c: " + str(c) + " w: " + str(w) + " ts: " + str(ts) + " o: " + str(o))

  pr = getAptProbability('r', o, ts)
  po = getAptProbability('o', i, c)
  pts = getAptProbability('ts', c, w)
  pi = getStaticNodeProbability('i')
  pc = getStaticNodeProbability('c')
  pw = getStaticNodeProbability('w')

  print(" pi: " + str(pi) + " pc: " + str(pc) + " pw: " + str(pw) + " po: " + str(po) + " pts: " + str(pts) + " pr: " + str(pr))
  if(i == c == w == True):
    totalProbability += (pi * pc * pw * po * pts * pr)
    # newIterations += 1

  print('Iteration ' + str(x + 1) + ' ends ------------------------------------------------------')

print ("totalProbability: " + str(totalProbability));
avgProabililty = totalProbability / iterations
# avgProabililty = totalProbability / newIterations
print ("average: " + str(avgProabililty))


# 20 Iterations - average: 0.004872
# 0.0010584 0.00091728 0.00102312 

# 100 Iterations - 