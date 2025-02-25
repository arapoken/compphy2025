
# Plot a histogram of random number

import numpy as np
import matplotlib.pyplot as plt

# parameters
mu = 100
sigma = 10
x = np.random.normal(mu, sigma, size=100000)

# plot a histogram
plt.hist(x, bins=60,range=(40,160))
plt.title('Gaussian Distribution Historgram')
plt.xlabel('X')
plt.ylabel('Counts')
plt.savefig('Hist.png')
plt.show()
