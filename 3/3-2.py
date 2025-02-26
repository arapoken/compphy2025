# ---------------Iterative method to solve Spherical Bessel function---------------
# prepare for the packages
import numpy as np
import matplotlib.pyplot as plt

'''---------------------Upward Iteration---------------------'''
# define the function j0,j1 and the boundary condition
x = np.linspace(0.0, 20.0, 100)
x_nonzero = x[1:] # avoid the zero division
j = np.zeros((11, 100)) # create a 2D array to store the value of jn
j[0][1:] = np.sin(x_nonzero)/x_nonzero
j[1][1:] = np.sin(x_nonzero)/x_nonzero**2 - np.cos(x_nonzero)/x_nonzero
j[0][0] = 1.0
j[1][0] = 0.0

# calculate the higher order of jn by Upward Iteration
for n in range(2, 11):
    j[n][1:] = ((2*n-1)/x_nonzero)*j[n-1][1:] - j[n-2][1:]
    j[n][0] = 0.0

'''---------------------Downward Iteration---------------------'''
# define the function j100,j101 and the boundary condition
k = np.zeros((102, 100)) # create a 2D array to store the value of kn
k[100][1:] = np.ones(99)
k[101][1:] = np.ones(99)
k[100][0] = 0.0
k[101][0] = 0.0

# calculate the lower order of kn by Downward Iteration
for n in range(99, -1, -1):
    k[n][1:] = ((2*n+3)/x_nonzero)*k[n+1][1:] - k[n+2][1:]
    k[n][0] = 0.0 if n != 0 else 1.0

# calculate multiple factor and normalize the value of kn
A = k[0][1:]/j[0][1:]
k_norm = np.zeros((100, 100))
for n in range(0, 100):
    k_norm[n][1:] = k[n][1:]/A
    k_norm[n][0] = 0.0 if n != 0 else 1.0

'''---------------------Plot the result---------------------'''
# create a figure and a set of subplots
fig, axes = plt.subplots(1,2, figsize=(10,4)) 
# the fisrt subplot
axes[0].plot(x, j[2], label='j2')
axes[0].plot(x, j[5], label='j5')
axes[0].plot(x, j[10], label='j10')
axes[0].set_title('Upward Iteration')
axes[0].set_xlabel('x')
axes[0].set_ylabel('jn(x)')
axes[0].set_ylim(-1,1)
axes[0].grid()
axes[0].legend()
# the second subplot
axes[1].plot(x, k_norm[2], label='j2')
axes[1].plot(x, k_norm[5], label='j5')
axes[1].plot(x, k_norm[10], label='j10')
axes[1].set_title('Downward Iteration')
axes[1].set_xlabel('x')
axes[1].set_ylabel('jn(x)')
axes[1].set_ylim(-1,1)
axes[1].grid()
axes[1].legend()
# adjust the layout and show the plot
plt.tight_layout()
plt.show()
