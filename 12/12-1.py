# ---------- Bifurcation of sine map and Lyapunov exponents ----------
import numpy as np
import matplotlib.pyplot as plt

def sine_map(r, x):
    return r * np.sin(np.pi * x)

n = 100000
xmin = 0.0
xmax = 1.0
r = np.linspace(xmin, xmax, n)

iterations = 1000
last = 100
x = 1e-5 * np.ones(n)
fx_1st = []  # store the 1st derivative of fx

for i in range(iterations):
    fx_1st.append(r * np.pi * np.cos(np.pi * x))
    x = sine_map(r, x)
    #display the bifurcation diagram
    if i>=(iterations- last):
        plt.scatter(r, x, c='k', s=0.05, alpha=0.1)

plt.xlim(xmin, xmax)
plt.title('Bifurcation diagram')
plt.grid()
plt.show()

# Lyapunov exponent
lambd = np.sum(np.log(np.abs(fx_1st)), axis=0) / iterations
plt.scatter(r, lambd, color=np.where(lambd>0, 'red','black'), s=0.1, alpha=0.1)

plt.xlim(xmin, xmax)
plt.title('Lyapunov exponent')
plt.grid()
plt.show()

# indices = [i for i, (a, b) in enumerate(zip(lambd, lambd[1:])) if a < 0 and b > 0]
# np.set_printoptions(threshold=np.inf)
# print(r[indices])
# # find the Bifurcation points is r=[0.31830318, 0.71754718, 0.83213832, 0.85831858, 0.86396864, 0.86517865]