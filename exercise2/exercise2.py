import time
import collections
import numpy as np
import matplotlib.pyplot as plt

def create_dataset(ncandidates, total_votes, weights=[]):
    # D = np.random.random_integers(1, ncandidates, total_votes).tolist()
    if not weights:
        weights = [1.0 / ncandidates for _ in range(ncandidates)]
    candidates = range(1, ncandidates + 1)
    D = np.random.choice(candidates, total_votes, p=weights).tolist()
    D_ = D[:]

    k = np.random.randint(0, total_votes)
    while D_[k] == D[k]:
        D_[k] = np.random.randint(1, ncandidates + 1)

    return D, D_

def expmech(D, qD, e):
    b = 1.0 / (len(D) * e)
    return qD + np.random.exponential(scale=b)

def report_noisy_max(D, U, epsilon):
    results = [expmech(D, u, epsilon) for u in U]
    return np.argmax(results)

def score(D, r):
    n = len(D)
    frequency = sum([1 for x in D if x == r])
    return 1.0 * (frequency - n) / n

def generate_probabilities(D, u, R, epsilon):
    results = [np.exp((epsilon * u(D, r)) / 2.0) for r in R]
    # print(results)
    total = sum(results)

    return [1.0 * x / total for x in results]

def privacy_loss():
    e = 0.5
    ncandidates = 1000
    total_votes = 10000
    R = list(range(1, ncandidates + 1))
    D, D_ = create_dataset(ncandidates, total_votes)
    p = generate_probabilities(D, score, R, e)
    p_ = generate_probabilities(D_, score, R, e)

    draw_probability(p)
    ratios = [np.log(1.0 * rd / rd_) for rd, rd_ in zip(p, p_)]
    plt.plot(ratios)
    plt.show()

def draw_probability(p):
  counter_hash = collections.Counter(p)
  keys = sorted(counter_hash.keys())
  y = []
  print keys
  for key in keys:
    y.append(counter_hash[key])

  print y

  # plt.axis([0, 6, 0, 20])
  plt.plot(keys, y, 'ro')
  plt.show()


def accuracy():
    e = 15.0
    beta = 0.1
    iterations = 10000
    u = score
    ncandidates = 4             # do not change!
    total_votes = 100
    weights = [0.1, 0.05, 0.8, 0.05]
    R = list(range(1, ncandidates + 1))
    alpha = (2.0 / e) * np.log(len(R) / beta)
    print('alpha = {}'.format(alpha))
    D, D_ = create_dataset(ncandidates, total_votes, weights)
    p = generate_probabilities(D, u, R, e)
    print(p)
    opt = max([u(D, r) for r in R])
    print(opt)
    count = 0
    diffs = []
    for _ in range(iterations):
        # print(np.random.choice(R, p=p))
        diff = opt - u(D, np.random.choice(R, p=p))
        if abs(diff) >= alpha:
            count += 1
        diffs.append(diff)
    print('beta = {}'.format(beta))
    print(1.0 * count / iterations)
    plt.plot(diffs, 'go')
    plt.axhline(alpha, color='r')
    plt.axhline(alpha, color='r')
    plt.xlabel('Nth run')
    plt.ylabel('error')
    plt.show()

if __name__ == '__main__':
    #Exponential Mechanism
    privacy_loss()
    # accuracy()

    # #Report One-Sided Noisy Arg Max
    # e = 0.5
    # beta = 0.1
    # iterations = 10000
    # u = score
    # ncandidates = 4             # do not change!
    # total_votes = 100000
    # weights = [0.1, 0.05, 0.8, 0.05]
    # R = list(range(1, ncandidates + 1))
    # D, D_ = create_dataset(ncandidates, total_votes, weights)
    # start_rnm = time.time()
    # U = [u(D, r) for r in R]
    # noisy_max = report_noisy_max(D, U, e)
    # print('RNM running time = {:.5f}s'.format(time.time() - start_rnm))
    # start_exp = time.time()
    # p = generate_probabilities(D, u, R, e)
    # exp_result = np.random.choice(R, p=p)
    # print('EXP running time = {:.5f}'.format(time.time() - start_exp))
