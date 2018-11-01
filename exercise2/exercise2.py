import time
import collections
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def create_dataset(ncandidates, total_votes, weights=[]):
  if not weights:
    weights = [1.0 / ncandidates for _ in range(ncandidates)]
  candidates = range(1, ncandidates + 1)
  D = np.random.choice(candidates, total_votes, p=weights).tolist()
  D1 = D[:]

  k = np.random.randint(0, total_votes)
  while D1[k] == D[k]:
    D1[k] = np.random.randint(1, ncandidates + 1)

  return D, D1

def expmech(D, qD, e):
  b = 1.0 / (len(D) * e)
  return qD + np.random.exponential(scale=b)

def score(D, r):
  n = len(D)
  frequency = sum([1 for x in D if x == r])
  return 1.0 * (frequency - n) / n

def generate_probabilities(D, u, R, epsilon):
  results = [np.exp((epsilon * u(D, r)) / 2.0) for r in R]
  total = sum(results)
  return [1.0 * x / total for x in results]

def privacy_loss():
  e = 0.5
  ncandidates = 1000
  total_votes = 10000
  R = list(range(1, ncandidates + 1))
  D, D1 = create_dataset(ncandidates, total_votes)
  p = generate_probabilities(D, score, R, e)
  p1 = generate_probabilities(D1, score, R, e)

  draw_probability(p)
  draw_probability_bar(p, p1)

def draw_probability_bar(p, p1):
  integer_data1 = [int(x) for x in p]
  integer_data2 = [int(x) for x in p1]

  counting_data1 = Counter(integer_data1)
  counting_data2 = Counter(integer_data2)

  data1_bar = []
  data2_bar = []
  keys = sorted(set(counting_data1.keys() + counting_data2.keys()))


  for key in keys:
    data1_bar.append(counting_data1[key])
    data2_bar.append(counting_data2[key])

  fig, ax = plt.subplots()
  index = np.arange(len(keys))
  bar_width = 0.2
  opacity = 0.4
  error_config = {'ecolor': '0.3'}
  rects1 = ax.bar(index, tuple(data1_bar), bar_width,
                  alpha=opacity, color='b',
                  error_kw=error_config,
                  label='D')

  rects2 = ax.bar(index + bar_width, tuple(data2_bar), bar_width,
                  alpha=opacity, color='r',
                  error_kw=error_config,
                  label='D\'')
  ax.set_xlabel('Couting result')
  ax.set_ylabel('Times')
  ax.set_xticks(index + bar_width / 2)
  ax.set_xticklabels(keys)
  ax.legend()
  fig.tight_layout()
  plt.show()


def draw_probability(p):
  counter_hash = collections.Counter(p)
  keys = sorted(counter_hash.keys())
  y = []
  for key in keys:
    y.append(counter_hash[key])

  plt.plot(keys, y, 'ro')
  plt.show()

def accuracy():
    e = 15
    beta = 0.1
    iterations = 10000
    u = score
    ncandidates = 4
    total_votes = 100
    weights = [0.1, 0.05, 0.8, 0.05]
    R = list(range(1, ncandidates + 1))
    alpha = (2.0 / e) * np.log(len(R) / beta)
    D, D1 = create_dataset(ncandidates, total_votes, weights)
    p = generate_probabilities(D, u, R, e)
    opt = max([u(D, r) for r in R])
    count = 0
    diffs = []
    for _ in range(iterations):
      diff = opt - u(D, np.random.choice(R, p=p))
      if abs(diff) >= alpha:
          count += 1
      diffs.append(diff)
    print('beta = {}'.format(beta))
    print(1.0 * count / iterations)
    plt.title(
      'BETA = ' + str(0.5) +
      ' Epsilon = ' + str(e) +
      ' N = ' + str(iterations)
    )
    plt.plot(diffs, 'go')
    plt.axhline(alpha, color='r')
    plt.axhline(alpha, color='r')
    plt.xlabel('Nth run')
    plt.ylabel('error')
    plt.show()

if __name__ == '__main__':
    # Exponential Mechanisms
    privacy_loss()
    accuracy()