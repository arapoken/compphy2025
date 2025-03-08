# ------------------ Blackbody radiation spectrum ------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ------------------(1) Numerical differentiation ------------------
c1, c2 = 1.0, 1.44e4
x_0, x_n, n = 1e-5, 5, 500
h = (x_n - x_0) /n
x = np.zeros(n+1)
for i in range(0, n+1):
    x[i] = x_0 + i*h

def B(x, t):    # define the Blackbody spectral radiance function
    return c1 /x**5 /(np.exp(c2/ (x*t)) - 1)
    
# find the extre points
T = np.linspace(2000, 6000, 500)
B_1st = np.zeros(len(x))
x_extre = np.zeros(len(T))
for j in range(0, len(T)): 
    t = T[j]

    # 5-points first derivative of B(x,t) at x_i including boundary points
    B_1st[0] = (4*B(x[1],t)-3*B(x[0],t)-B(x[2],t)) / (2*h)
    B_1st[1] = (4*B(x[2],t)-3*B(x[1],t)-B(x[3],t)) / (2*h)
    B_1st[n-1] = (3*B(x[n-1],t)+B(x[n-3],t)-4*B(x[n-2],t)) / (2*h)
    B_1st[n] = (3*B(x[n],t)+B(x[n-2],t)-4*B(x[n-1],t)) / (2*h)
    for i in range(2, n-1):
        B_1st[i] = (B(x[i-2],t)-8*B(x[i-1],t)+8*B(x[i+1],t)-B(x[i+2],t)) / (12*h)

    # determine the first point when derivative changes from positive to negative as an extreme point
    index_extre = [i for i in range(0, len(B_1st)) if B_1st[i-1] > 0 and B_1st[i] < 0]
    x_extre[j] = x[index_extre[0]]

plt.plot(x, B(x,2500),'m-')    # plot the spectral function at some fixed T
plt.plot(x, B(x,3500),'g-') 
plt.plot(x, B(x,4500),'c-') 
plt.plot(x, B(x,6000),'b-') 
plt.plot(x_extre, B(x_extre,T), 'r--')  # plot the extremum points in different temperature
plt.xlabel('wavelength(um)')
plt.ylabel('Spectral Intensity')
plt.legend(['T=2500K', 'T=3500K', 'T=4500K','T=6000K',
            'the extremum points in different temperature'])
plt.title('Blackbody radiation distribution')
plt.grid(True)
plt.show()

# plot the 1st derivative of B_lambda at T=6000K
plt.plot(x, B_1st, 'r--')
plt.xlabel('wavelength(um)')
plt.ylabel('1st derivative of B')
plt.title('the derivative of B changing with lambda at T=6000K')
plt.grid(True)
plt.show()

# choose a proper fitting function of lambda and temperature
def lambda_extre(T, A):
    return A/T
p0 = [3000.0]
popt, pcov = curve_fit(lambda_extre, T, x_extre, p0=p0)
print(f'Wien\'s displacement law: λ_max·T={popt[0]:.4f} um·K')

# plot the extremum point changing with T
plt.plot(T, x_extre, 'o', markersize=1.0, c='black')
plt.plot(T, lambda_extre(T, *popt), 'r-')
plt.xlabel('Temperature(K)')
plt.ylabel('wavelength(um) of extremum point')
plt.legend(['Data points', '1/x fit'])
plt.title('the wavelength of extremum point changing with T')
plt.grid(True)
plt.show()

# ------------------(2) Numerical Integral ------------------

a, b, m = 0.3, 0.8, 50
h = (b-a)/(2*m)
x_simpson = np.linspace(a, b, 2*m+1) # define the integral interval
B_simpson = B(x_simpson, 5000) # define the function to be integrated

sum = 0
for i in range(0, m):
    sum += h/3*(B_simpson[2*i]+4*B_simpson[2*i+1]+B_simpson[2*i+2]) # Simpson's rule
print(f'The integral of B_lambda from 0.3um to 0.8um at T=5000K is {sum:.4f} um^{-4}')