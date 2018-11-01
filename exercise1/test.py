import numpy as np
import pylab as plt

S = np.loadtxt("sample.txt")
Y = S[0]
print Y.shape[0]



plt.plot([1,2,3,4,5], 'go')
plt.show()
