# ---------------------Multi-slit Diffraction----------------------
# prepare for the nessasary packages

import numpy as np
import matplotlib.pyplot as plt
from math import pi

# initialize the variables, d>~a>λ, N>1
a, d, lambd, N, I_0 = 0.2, 0.5, 0.05, 4, 1
sin_theta = np.linspace(-0.2, 0.2,500)

# caculate the intensity of light
U = pi/lambd*a*sin_theta
V = pi/lambd*d*sin_theta
I = I_0 * np.sin(U)**2/U**2 * np.sin(N*V)**2/V**2

# plot the intensity curve with sinθ
plt.plot(sin_theta,I,linestyle='-')
plt.title('the light intensity I changes with sinθ')
plt.xlabel('sinθ')
plt.ylabel('I/I0')
plt.legend()
plt.grid(True)
plt.savefig('1-3.png')
plt.show()
