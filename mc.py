import random
from helper import generateBooleanForSample, Sample
print ('==================== Monte Carlo Inference of Bayesian Network =========================')
iterations = 100
samples = []

for x in range(0, iterations):
  # Generate Random Nos for each of the node.
  i = round(random.random(), 2)
  c = round(random.random(), 2)
  w = round(random.random(), 2)
  o = round(random.random(), 2)
  t = round(random.random(), 2)
  r = round(random.random(), 2)

  # Get the value whether it is a positive event(true) or a negative event(false) based on the random value generated above.
  iss = generateBooleanForSample('i', i, True, True)
  cs = generateBooleanForSample('c', c, True, True)
  ws = generateBooleanForSample('w', w, True, True)
  os = generateBooleanForSample('o', o, iss, cs)
  tss = generateBooleanForSample('ts', t, cs, ws)
  rs = generateBooleanForSample('r', i, os, tss)

  # store all samples in an array.
  samples.append(Sample(iss, cs, ws, os, tss, rs))

# P(I) = no of positive I / total Samples
plusI = len([x for x in samples if x.i == True]) 

# P(C) = no of positive C / total Samples
plusC = len([x for x in samples if x.c == True])

# P(W) = no of positive W / total Samples
plusW = len([x for x in samples if x.w == True])

# P(O) = no of positive Os with positive I and positive C / total no of samples having positive Is and positive Cs
plusO = len([x for x in samples if x.o == True and x.c == True and x.i == True])

# P(T) = no of positive Ts with positive C and positive W / total no of samples having positive Cs and positive Ws
plusT = len([x for x in samples if x.t == True and x.c == True and x.w == True])

# P(R) = no of positive Rs with positive O and positive T / total no of samples having positive Os and positive Ts
plusR = len([x for x in samples if x.r == True and x.o == True and x.t == True])

# calculating totals for all the nodes.
totalICW = len(samples)
totalOIC = len([x for x in samples if x.i == True and x.c == True])
totalTCW = len([x for x in samples if x.c == True and x.w == True])
totalROT = len([x for x in samples if x.o == True and x.w == True])

# print("P(I) = " + str(plusI) + " / " + str(totalICW) )
# print("P(C) = " + str(plusC) + " / " + str(totalICW) )
# print("P(W) = " + str(plusW) + " / " + str(totalICW) )
# print("P(O) = " + str(plusO) + " / " + str(totalOIC) )
# print("P(T) = " + str(plusT) + " / " + str(totalTCW) )
# print("P(R) = " + str(plusR) + " / " + str(totalROT) )

pi = 0 
pc = 0
pw = 0
po = 0
pt = 0
pr = 0

if(totalICW != 0):
  pi = plusI / float(totalICW)
  pc = plusC / float(totalICW)
  pw = plusW / float(totalICW)

if(totalOIC != 0):
  po = plusO / float(totalOIC)

if(totalTCW != 0):
  pt = plusT / float(totalTCW)

if(totalROT != 0):
  pr = plusR / float(totalROT)

print("pi: " + str(pi))
print("pc: " + str(pc))
print("pw: " + str(pw))
print("po: " + str(po))
print("pt: " + str(pt))
print("pr: " + str(pr))

finalProbability = pi*pc*pw*po*pt*pr

print('final: ' + str(finalProbability))

