import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from data_set import DataSet
from laplace import Laplace
from randomized_response import RandomizedResponse

def draw_privacy_loss(histagram1, histagram2, N=1000, e=0.5):
  integer_data1 = [int(x) for x in histagram1]
  integer_data2 = [int(x) for x in histagram2]

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
  ax.set_title('Epsilon is ' + str(e) + ', N  = ' + str(N)) # + ", Privacy loss = " + str(privacy_loss))
  ax.set_xticks(index + bar_width / 2)
  ax.set_xticklabels(keys)
  ax.legend()
  fig.tight_layout()
  plt.show()

def draw_accuracy(data_list, qD, N=1000, e=0.5, beta=0.05):
  laplace_alpha = (1.0 / (N * e)) * np.log(1 / beta)
  print laplace_alpha
  laplace_errors = [(qD - r) for r in data_list]

  rr = RandomizedResponse()
  rr_errors, rr_alpha = rr.compute_accuacy(D0, 1000)

  f, axarr = plt.subplots(2, sharex=False)

  axarr[0].set_title('Laplace')
  axarr[0].axhline(0, color='r')
  alpha_line_lp = axarr[0].axhline(laplace_alpha, color='r')
  axarr[0].axhline(-laplace_alpha, color='r')
  axarr[0].set_xlabel('Nth run')
  axarr[0].set_ylabel('Error')
  axarr[0].legend([alpha_line_lp], ['alpha = {:.6f}'.format(laplace_alpha)])
  axarr[0].plot(laplace_errors, 'go')

  axarr[1].set_title('Randomized Response')
  axarr[1].axhline(0, color='g')
  alpha_line_rr = axarr[1].axhline(rr_alpha, color='r')
  axarr[1].axhline(-rr_alpha, color='r')
  axarr[1].set_xlabel('Nth run')
  axarr[1].set_ylabel('Error')
  axarr[1].legend([alpha_line_rr],['alpha = '+'{:.6f}'.format(rr_alpha)])
  axarr[1].plot(rr_errors, 'go')

  plt.title(
    'BETA = ' + str(beta) +
    'Epsilon = ' + str(e) +
    'N = ' + str(N)
  )

  plt.show()

D0 = DataSet()
D0.create_from_csv('./adult.csv')
D1 = DataSet()
D1.copy_from_dataset(D0)
D1.records.pop() # eliminate one element

laplace = Laplace()
D0_histagram_data, qD0 = laplace.do_mechanism(D0, 1000)
D1_histagram_data, qD1 = laplace.do_mechanism(D1, 1000)

# parameters are all laplace's parameter
draw_privacy_loss(D0_histagram_data, D1_histagram_data, 1000, e=0.5)
draw_accuracy(D0_histagram_data, qD0)
