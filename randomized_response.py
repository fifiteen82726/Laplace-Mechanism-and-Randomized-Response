import random
import numpy as np
import matplotlib.pyplot as plt
import math
from collections import defaultdict
from data_set import DataSet

E = math.e

class RandomizedResponse:
  def threshold_query(self, record):
    # income <=50 && education-num > 12
    if record[4] > 13 and record[14] == '<=50K':
      return 1
    else:
      return 0

  def do_randomize(self, D, probability):
    sum_total = 0
    for d in D.records:
      if random.random() < probability:
        sum_total += self.threshold_query(d)
      else:
        sum_total += (1 - self.threshold_query(d))

    return float(sum_total) / float(len(D.records))

  def do_randomized_mechenism(self, dataset, run_times, epsilon):
    result = []
    probability = float(E ** epsilon) / float(1 + (E ** epsilon))

    for i in range(run_times):
      result.append(self.do_randomize(dataset, probability))

    return result

  def get_qD(self, D):
    count = 0
    for i in D.records:
      if i[4] > 13 and i[14] == '<=50K':
        count += 1
    return float(count) / float(len(D.records))

  def compute_accuacy(self, D, N=100, e=0.5, beta=0.05):
    c1 = 1 / (1 + E ** e)
    c2 = (1 + E ** e) / ((E ** e) - 1)
    c3 = math.sqrt(math.log(2 / beta) / (2*N))
    alpha = c2 * c3
    qD = self.get_qD(D)
    data_list = self.do_randomized_mechenism(D, N, e)
    errors = [(qD - r) for r in data_list]

    return errors, alpha


D0 = DataSet()
D0.create_from_csv('./adult.csv')
rr = RandomizedResponse()
errors, alpha = rr.compute_accuacy(D0)
