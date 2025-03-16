# ------------------ Classic Damped Oscillator ------------------
import numpy as np
import matplotlib.pyplot as plt

n = 1000
h = 100/n
t = np.linspace(0, 100, n, endpoint=False)
k = 0.1
w = 1.0
delta = np.sqrt(4*w**2 - k**2)/2

phi = np.zeros(n) # dphi/dt = chi
chi = np.zeros(n) # dchi/dt = -k/chi - w**2*phi
phi[0] = 1.0
chi[0] = 0.0 # initial conditions

# 4th order Runge-Kutta method
for i in range(n-1):
    kphi1 = chi[i]
    kchi1 = -k*chi[i] - w**2*phi[i]
    kphi2 = chi[i] + kchi1*h/2
    kchi2 = -k*(chi[i] + kchi1*h/2) - w**2*(phi[i] + kphi1*h/2)
    kphi3 = chi[i] + kchi2*h/2
    kchi3 = -k*(chi[i] + kchi2*h/2) - w**2*(phi[i] + kphi2*h/2)
    kphi4 = chi[i] + kchi3*h
    kchi4 = -k*(chi[i] + kchi3*h) - w**2*(phi[i] + kphi3*h)
    phi[i+1] = phi[i] + (kphi1 + 2*kphi2 + 2*kphi3 + kphi4)*h/6
    chi[i+1] = chi[i] + (kchi1 + 2*kchi2 + 2*kchi3 + kchi4)*h/6

# determine whether there is phi<0, which means the appearance of an oscillation term
print('Is there any oscillation?:',(phi < 0).any())
# after adjusting the parameters, we found that when k>=2, the oscillation term disappears

# analytical solution
y = np.exp(-k/2*t)*(phi[0] * np.cos((delta)*t) + (chi[0]+k*phi[0]/2)/delta * np.sin(delta*t))

# plot the result
plt.plot(t, phi, 'o', c='red', markersize = 3.0)
plt.plot(t, y, 'b-')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(['Numerical result', 'Analytical result'])
plt.title('Classic Damped Oscillator')
plt.grid()
plt.show()

