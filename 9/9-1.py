# ----------- Random walk simulation -----------
import numpy as np
import matplotlib.pyplot as plt

N = int(1e6)
pl = 1/6
pr = 3/6
po = 2/6
nsteps = 100

positions = np.zeros(N)  #initial positions

for i in range(nsteps):
    random_num = np.random.rand(N)  # random number generation
    positions[random_num < pl] -= 1  # left move
    positions[(pl <= random_num) & (random_num < pl+pr)] += 1  # right move

print(f'simulational mean value: {np.mean(positions)}')
print(f'simulational standard error: {np.sqrt(np.var(positions))}')

# theoretically it is a normal distribution according to the central limit theorem
x = np.linspace(positions.min(), positions.max(), 1000)
mu = nsteps/3
sigma = np.sqrt(5*nsteps/9)
norm_pdf = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))
print(f'theoretical mean value: {mu}')
print(f'theoretical standard error: {sigma}')

# plot the result of both simulation and theory
plt.hist(positions, bins=50, density=True, alpha=0.8, label=f'Simulation: t={nsteps}s')  # density=True to make it normalized
plt.plot(x, norm_pdf, 'r-', lw=2, label=f'Theory: N({mu:.2f}, {sigma:.2f}^2)')
plt.xlabel('Position')
plt.ylabel('Probability Density')
plt.title('Random Walk Simulation')
plt.legend()
plt.show()