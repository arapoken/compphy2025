# ------------------ Quantum Harmonic Oscillator ------------------
import numpy as np
import matplotlib.pyplot as plt

N = 3000
h = 7/N
x = np.linspace(0, 7, N, endpoint=False)
n = 15 # quantum number

u = np.zeros(N) # du/dx = v
v = np.zeros(N) # dv/dx = (x**2 - 2*n -1)*u

if n % 2 == 0:
    u[0] = 1.0
    v[0] = 0.0 # even boundary conditions
else:
    u[0] = 0.0
    v[0] = 1.0 # odd boundary conditions

# 4th order Runge-Kutta method
for i in range(N-1):
    ku1 = v[i]
    kv1 = (x[i]**2 - 2*n - 1)*u[i]
    ku2 = v[i] + 0.5*h*kv1
    kv2 = ((x[i] + 0.5*h)**2 - 2*n - 1)*(u[i] + 0.5*h*ku1)
    ku3 = v[i] + 0.5*h*kv2
    kv3 = ((x[i] + 0.5*h)**2 - 2*n - 1)*(u[i] + 0.5*h*ku2)
    ku4 = v[i] + h*kv3
    kv4 = ((x[i] + h)**2 - 2*n - 1)*(u[i] + h*ku3)
    u[i+1] = u[i] + (ku1 + 2*ku2 + 2*ku3 + ku4)*h/6
    v[i+1] = v[i] + (kv1 + 2*kv2 + 2*kv3 + kv4)*h/6

x = np.hstack((-np.flip(x), x)) # x axis extension
if n % 2 == 0:
    u = np.hstack((np.flip(u), u)) # even extension
else:
    u = np.hstack((-np.flip(u), u)) # odd extension

# plot the quantum harmonic oscillator
plt.plot(x, u, 'b-')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Quantum Harmonic Oscillator (n='+str(n)+')')
plt.grid()
plt.show()

# classical oscillator probability density
rho = 1 / (np.pi * np.sqrt(2*n+1-x[(2*n+1-x**2) > 0]**2)) # np.pi for normalization
u_2 = np.square(u) / np.sum(h*np.square(u)) # np.sum for normalization

# plot the comparison between quantum and classical harmonic oscillators
plt.plot(x, u_2, 'b-')
plt.plot(x[(2*n+1-x**2) > 0], rho, 'r-')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.legend(['Quantum situation','Classical situation'])
plt.title('Harmonic Oscillator Probability (n='+str(n)+')')
plt.ylim(0.0, 1.1*np.max(u_2))
plt.grid()
plt.show()