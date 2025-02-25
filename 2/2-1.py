# ------------------Earth's magnetic field distribution------------------
# prepare for the necessary packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# initialize the variables
RE, B0, theta0 = 6.37, 3.12e-5, 11.5/180*np.pi
x = np.linspace(-40,40,1000)
y = np.linspace(-40,40,1000)
X,Y = np.meshgrid(x,y)

# define the functions in Magnetic-axis coordinate system
def r(x,y):
    return np.ma.sqrt(x**2 + y**2)
def theta(x,y):
    return np.arctan(x/y)-theta0
def Br(x,y):
    return -2*B0*(RE/r(x,y))**3*np.cos(theta(x,y))
def Bt(x,y):
    return -B0*(RE/r(x,y))**3*np.sin(theta(x,y))

# calculate the magnetic field in Rotation-axis coordinate system
def Bx(x,y):
    return Br(x,y)*np.sin(theta(x,y)+theta0)+Bt(x,y)*np.cos(theta(x,y)+theta0)
def By(x,y):
    return Br(x,y)*np.cos(theta(x,y)+theta0)-Bt(x,y)*np.sin(theta(x,y)+theta0)

# plot the magnetic field distribution
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
'''Mask the neighborhood at origin and plot the Earth'''
mask = (X - 0)**2 + (Y - 0)**2 < RE**2
X_masked = np.ma.masked_where(mask,X)
Y_masked = np.ma.masked_where(mask,Y)
Earth = Circle((0,0),RE,color='blue')
ax.add_artist(Earth)
'''Plot the steamlines of the field'''
color = 2*np.log(np.hypot(Bx(X_masked,Y_masked),By(X_masked,Y_masked)))
ax.streamplot(X,Y, Bx(X_masked,Y_masked),By(X_masked,Y_masked), color=color, linewidth=1,
              cmap=plt.cm.inferno, density=2, arrowstyle='->', arrowsize=1.5)
ax.set_xlim(-40,40)
ax.set_ylim(-40,40)
ax.set_aspect('equal')
plt.savefig('MagneticField.png')
plt.show()
