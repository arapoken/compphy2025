
# Plot a scatter plot 

import numpy as np
import matplotlib.pyplot as plt

# set parameters
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
Z = 1/np.pi*np.e**(-(Y*Y+X*X)/2)

# plot a scatter graph
plt.scatter(X,Y, s=75, c=Z, alpha=.5)
plt.title("Scatter Gaussian")
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.savefig('Scatter.png',dpi=120)
plt.show()
