#!/usr/bin/python

import random

NUM_GENES = 2 # useful, antic

RANDOM_FITNESS = 1
SURVIVING = 0.5

GENE_FITNESSES = [0.1, 0]

N = 1000
T = 1000

class Member:
  def __init__(self, genes=None):
    self.genes = genes or [0]*NUM_GENES

class Population:
  def __init__(self, gene_ratios):
    self.members = [Member() for i in range(N)]
    for i in range(N):
      for j in range(NUM_GENES):
        self.members[i].genes[j] = 1 if random.random() < gene_ratios[j] else 0

  def mix(self, x, y):
    return Member([1 if random.random() <= (x.genes[j]+y.genes[j])/2.0 else 0 for j in range(NUM_GENES)])

  def step(self):
    fitnesses = [random.random()*RANDOM_FITNESS + sum([GENE_FITNESSES[j] * self.members[i].genes[j] for j in range(NUM_GENES)]) for i in range(N)]
    keys = range(N)
    keys.sort(lambda x, y: int(round(fitnesses[y] - fitnesses[x])))
    keys = keys[:int(SURVIVING*N)]
    reps = [self.members[i] for i in keys]
    self.members = [self.mix(random.choice(reps), random.choice(reps)) for i in range(N)]

  def report(self):
    g_freq = [sum([m.genes[j] for m in self.members])/float(N) for j in range(NUM_GENES)]
    #for m in self.members: print m.genes
    print 'gene frequencies:', g_freq

#

p = Population([0.5, 0.5])
for i in range(T):
  print i,
  p.report()
  p.step()

