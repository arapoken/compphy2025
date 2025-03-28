# ------- Simulated annealing method to find the global minimum -------
import numpy as np
import matplotlib.pyplot as plt

T0 = 500  # suitable initial temperature
tau = 10000
t = np.linspace(0, 1000, 100000)
T = T0 * np.exp(-t / tau)  # cooling function

x = np.linspace(0, 50, 1000)
f = np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x)

index = np.random.randint(0, len(x))  # initial index
f_min = f[index]

for i in range(len(T)):

    # randomize the move step
    step = max(int(20*T[i]/T0), 1)

    if np.random.rand() < 0.5:
        new_index = min(index + step, len(x)-1)  # avoid index out of bounds
        delta_d = f[new_index]-f[index]  # right-move
    else:
        new_index = max(index - step, 0)  # avoid index out of bounds
        delta_d = f[new_index]-f[index]  # left-move

    if np.random.rand() < np.exp(-delta_d / T[i]):  # Metropolis
        index = new_index

    if f_min > f[index]:  # store the historical minimum
        f_min = f[index]
        x_min = index

print(f'The global minimum is f({x[x_min]:.3f})={f_min:.3f}')

# visualize the annealing process
plt.plot(x, f, label='f(x)')
plt.scatter(x[x_min], f_min, c='r', label=f'global minimum: f({x[x_min]:.3f})={f_min:.3f}')
plt.title('Simulated annealing searching')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
