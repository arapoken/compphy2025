# -------------------Lagrange interpolation method-------------------
# prepare for the necessary modules
import numpy as np
import matplotlib.pyplot as plt

# define the original function f(x)
u, sigma = 50, 15
x_0, x_n = 5.0, 95.0
X = np.linspace(x_0, x_n, 1000)
def f(x):
    return np.exp(-(x-u)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))

# prepare the interpolation points (x_i, y_i)
n = 4
x = np.zeros(n+1)
y = np.zeros(n+1)
for i in range(0,n+1):
    x[i] = x_0 + i*(x_n-x_0)/n
    y[i] = f(x[i])

# define the lagrange term l_k(x)
def lagrange(t, k):
    prod = 1
    for j in range(n+1):
        if j != k:
            prod *= (t - x[j])/(x[k] - x[j])
    return prod

# sum over the terms and get the Lagrange interpolation function P_n(x)
sum = np.zeros(1000)
for k in range(0, n+1):
    for i in range(0, 1000):
        sum[i] += lagrange(X[i], k)*y[k]

# plot the original function and the interpolation function
plt.plot(X, f(X), 'b', label='f(x)')
plt.plot(X, sum, 'r', label='Lagrange interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

# plot the error of the interpolation function
plt.plot(X, np.abs(sum-f(X)), 'g', label='Error')
plt.legend()
plt.xlabel('x')
plt.ylabel('|f(x)-P_n(x)|')
plt.grid()
plt.show()

# find the smallest n to satisfy the error < 0.0005
error = np.abs(sum-f(X)).max()
while(error >= 0.0005):
    n += 1
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    for i in range(0,n+1):
        x[i] = x_0 + i*(x_n-x_0)/n
        y[i] = f(x[i])
    sum = np.zeros(1000)
    for k in range(0, n+1):
        for i in range(0, 1000):
            sum[i] += lagrange(X[i], k)*y[k]
    error = np.abs(sum-f(X)).max()
print('The smallest n =', n)

# At the time, plot the error of the interpolation function
plt.plot(X, np.abs(sum-f(X)), 'g', label='Error (n=10)')
plt.legend()
plt.xlabel('x')
plt.ylabel('|f(x)-P_n(x)|')
plt.grid()
plt.ylim(0, 0.0005)
plt.show()
