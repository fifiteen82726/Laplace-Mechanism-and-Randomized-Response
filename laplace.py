import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


class Laplace:
  def __init__(self):
    self.threshold_query_result = 0

  def threshold_query(self, dataset):
    # income <=50 && education-num > 12
    count = 0
    for i in dataset.records:
      if i[4] > 13 and i[14] == '<=50K':
        count += 1

    self.threshold_query_result = count
    return count

  def do_mechanism(self, D, n=100, e=0.5):
    qD = self.threshold_query(D)
    result = []
    for i in range(0, n):
      noisy_result = self.lapmech(D, qD, e)
      result.append(noisy_result)

    return result, qD

  def lapmech(self, D, qD, e):
    b = 1.0 / (len(D.records) * e)
    return qD + np.random.laplace(scale=b)
