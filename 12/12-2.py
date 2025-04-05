# -------------- Epidemic Model --------------
import numpy as np
import matplotlib.pyplot as plt

global l,k
l = 0.01  # death rate of ill people
k = 1e-9  # k in [1e-7, 1e-9] corresponding to kx-l in [>0(unstable), <0(stable)]

x0, y0, z0=1e6, 1 ,0  # initial conditions
dt = 0.01
t_max = 1000
t = np.arange(0, t_max, dt)

x = np.zeros(len(t))
y = np.zeros(len(t))
z = np.zeros(len(t))
x[0], y[0], z[0] = x0, y0, z0

def update(x, y):
    dxdt = - k * x * y
    dydt = k * x * y - l * y
    dzdt = l * y
    return dxdt, dydt, dzdt

# Runge-Kutta method
for i in range(1, len(t)):
    k1_x, k1_y, k1_z = update(x[i-1], y[i-1])
    k2_x, k2_y, k2_z = update(x[i-1] + 0.5 * dt * k1_x, y[i-1] + 0.5 * dt * k1_y)
    k3_x, k3_y, k3_z = update(x[i-1] + 0.5 * dt * k2_x, y[i-1] + 0.5 * dt * k2_y)
    k4_x, k4_y, k4_z = update(x[i-1] + dt * k3_x, y[i-1] + dt * k3_y)
    
    x[i] = x[i-1] + 1/6 * dt * (k1_x + 2*k2_x + 2*k3_x + k4_x)
    y[i] = y[i-1] + 1/6 * dt * (k1_y + 2*k2_y + 2*k3_y + k4_y)
    z[i] = z[i-1] + 1/6 * dt * (k1_z + 2*k2_z + 2*k3_z + k4_z)

# plot the result
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='healthy', color='blue')
plt.plot(t, y, label='ill', color='red')
plt.plot(t, z, label='dead', color='green')
plt.xlabel('t')
plt.ylabel('population')
plt.legend()
plt.title(f'Evolution of population under the Epidemic Model when k={k}')
plt.grid(True)
plt.show()
