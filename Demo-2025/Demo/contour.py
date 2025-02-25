##################################3

# Plot a 3D contour

##################################3

import numpy as np
import matplotlib.pyplot as plt

# define Z 
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

# set parameters
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

# plot a coutour
plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X,Y), 8, colors='black')
plt.clabel(C, inline=1, fontsize=10)

plt.title("Contour Plot")
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Contour.png',dpi=120)
plt.show()
