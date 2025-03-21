
# plot a 3D graph

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# set paraemters
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# plot function
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.set_zlim(-2,2)
ax.set_zlabel('Z')
plt.title("3D Plot")
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Plot3D.png',dpi=120)
plt.show()
