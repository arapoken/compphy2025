# ------------ Electron wave packets in infinitely deep potential wells ------------ 
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, m_e

N = 1000
L, sigma, k = 1e-8, 1e-10, 5e10
hx = L / N
ht = 1e-18
nsteps = 2000
x = np.linspace(0, L, N+1)
t = np.linspace(0, nsteps*ht, nsteps+1)
psi = np.exp(-(x-L/2)**2/(2*sigma**2)) * np.exp(1j*k*x) # Initial wave packet
psi[0], psi[-1] = 0+0j, 0+0j # Boundary condition
phi = psi[1:-1].copy() # Wave function without boundary points

# Crank-Nicolson method
A = np.zeros((N-1, N-1), dtype=complex)
B = np.zeros((N-1, N-1), dtype=complex)
for i in range(N-1):
    A[i,i] = 1+1j*ht*hbar/(2*m_e*hx**2)
    B[i,i] = 1-1j*ht*hbar/(2*m_e*hx**2)
    if i != N-2:
        A[i,i+1] = -1j*ht*hbar/(4*m_e*hx**2)
        B[i,i+1] = 1j*ht*hbar/(4*m_e*hx**2)
    if i != 0:
        A[i,i-1] = -1j*ht*hbar/(4*m_e*hx**2)
        B[i,i-1] = 1j*ht*hbar/(4*m_e*hx**2)

# Time evolution
time_points = [0,300,500,800,2000]
prob_data = []
real_data = []
imag_data = []

for step in range(nsteps+1):
    phi = np.linalg.solve(A, np.dot(B, phi)) # A * phi(t+ht) = B * phi(t)
    psi[1:-1] = phi # Update the wave packet
    if step in time_points: # Check the time points
        prob_data.append(np.abs(psi)**2)
        real_data.append(np.real(psi).copy())
        imag_data.append(np.imag(psi).copy())

# Plot the result
fig, ax = plt.subplots(3,1, figsize=(10,8))
colors = ['blue', 'green', 'red', 'purple', 'orange']
prob_max = np.max(prob_data)
real_max = np.max(real_data)
imag_max = np.max(imag_data)

for i in range(len(time_points)):
    ax[0].plot(x,prob_data[i],color=colors[i], label=f't={time_points[i]}ht')
    ax[1].plot(x,real_data[i],color=colors[i], label=f't={time_points[i]}ht')
    ax[2].plot(x,imag_data[i],color=colors[i], label=f't={time_points[i]}ht')

ax[0].set_xlim(0, L)
ax[0].set_ylim(0,1.1*prob_max)
ax[0].set_xlabel('Position (m)')
ax[0].set_ylabel('Probability')
ax[0].legend()

ax[1].set_xlim(0, L)
ax[1].set_ylim(-1.1*real_max,1.1*real_max)
ax[1].set_xlabel('Position (m)')
ax[1].set_ylabel('real Psi(x)')
ax[1].legend

ax[2].set_xlim(0, L)
ax[2].set_ylim(-1.1*imag_max,1.1*imag_max)
ax[2].set_xlabel('Position (m)')
ax[2].set_ylabel('imag Psi(x)')
ax[2].legend

plt.savefig('8-1.png')
plt.show()
