import numpy as np

#numpy.random.normal

m, sigma = 0, 0.1 # mean và standard deviation
s = np.random.normal(m, sigma, size=15)
print("s = ", s)