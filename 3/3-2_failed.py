# ---------------Iterative method to solve Spherical Bessel function---------------


# This is a FAILED attempt to plot the downward iteration, 
# because an iteration from j100 and j101 brings a large number of calling
# up to 2^{100-n} times(j_n+1 and j_n+2, twice a time) to get a j_n value.


# prepare for the packages
import numpy as np
import matplotlib.pyplot as plt

'''---------------------Upward Iteration---------------------'''
# define the function j0,j1 and iterative relation for the higher order
def jn(n, x):
    if n == 0:
        return np.sin(x)/x
    elif n == 1:
        return np.sin(x)/x**2 - np.cos(x)/x
    else:
        return ((2*n-1)/x)*jn(n-1, x) - jn(n-2, x)

'''---------------------Downward Iteration---------------------'''
# define the function j100,j101 and iterative relation for the lower order
def kn(n, x):
    if n == 100 or n == 101:
        return 1.0
    elif 0 <= n < 100:
        return ((2*n+3)/x)*kn(n+1, x) - kn(n+2, x)
    else:
        return 'Invalid n'

# calculate multiple factor for the downward iteration over the real value of j0
x = np.linspace(0.0, 20.0, 100)
A = kn(0,x[1])/jn(0,x[1]) 

# create a figure and a set of subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 4)) 

# the fisrt subplot
axes[0].plot(x, jn(2,x), label='j2')
axes[0].plot(x, jn(5,x), label='j5')
axes[0].plot(x, jn(10,x), label='j10')
axes[0].set_title('Upward method')
axes[0].set_xlabel('x')
axes[0].set_ylabel('jn(x)')
axes[0].legend()

# the second subplot
axes[0].plot(x, kn(2,x)/A, label='j2')
axes[0].plot(x, kn(5,x)/A, label='j5')
axes[0].plot(x, kn(10,x)/A, label='j10')
axes[0].set_title('Downward method')
axes[0].set_xlabel('x')
axes[0].set_ylabel('jn(x)')
axes[0].legend()

# adjust the layout and show the plot
plt.tight_layout()
plt.show()
