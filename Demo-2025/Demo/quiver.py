
# Plot vortex example

import numpy as np
import matplotlib.pyplot as plt

# set parameters
x = np.arange(0,2*np.pi+2*np.pi/20,2*np.pi/20)
y = np.arange(0,2*np.pi+2*np.pi/20,2*np.pi/20)

X,Y = np.meshgrid(x,y)
u = np.sin(X)*np.cos(Y)
v = -np.cos(X)*np.sin(Y)

# plot quiver
plt.quiver(X,Y,u,v)
plt.title("Quiver Four Votex")
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Quiver_Votex.png',dpi=120)
plt.show()
