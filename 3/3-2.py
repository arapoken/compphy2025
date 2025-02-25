# ---------------Iterative method to solve Spherical Bessel function---------------
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

# plot the spherical bessel function
x = np.linspace(0.0, 20.0, 100)
plt.plot(x, jn(2, x), label='j2')
plt.plot(x, jn(5, x), label='j5')
plt.plot(x, jn(10, x), label='j10')
plt.xlabel('x')
plt.ylabel('jn(x)')
plt.legend()
plt.show()

'''---------------------Downward Iteration---------------------'''
# define the function j100,j101 and iterative relation for the lower order
def kn(n, x):
    if n == 100 or n == 101:
        return 1.0
    elif 0 <= n < 100:
        return ((2*n+3)/x)*jn(n+1, x) - jn(n+2, x)
    else:
        return 'Invalid n!!!!!'
    
# calculate multiple factor for the downward iteration over the real value of j0
A = kn(0,x[1])/jn(0,x[1]) 

# plot the spherical bessel function
x = np.linspace(0.0, 20.0, 100)
plt.plot(x, kn(2, x)/A, label='j2')
plt.plot(x, kn(5, x)/A, label='j5')
plt.plot(x, kn(10, x)/A, label='j10')
plt.xlabel('x')
plt.ylabel('jn(x)')
plt.legend()
plt.show()

# issues unsolved:
# 1. The downward iteration is not working properly
# 2. The value at x=0 is not defined