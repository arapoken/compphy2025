# ----------------- 2-D Ising model simulation -----------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

seed = 89
beta = 0.1
J = 1.0
L = 20
nsteps = 500000  # maxium simulation steps
np.random.seed(seed)

S = np.random.choice([1,-1],size=(L+2,L+2))  # randomize the initial configuration
S[0][:], S[:][0], S[L+1][:], S[:][L+1] = 0, 0, 0, 0  # set S=0 at the boundary 

energies = []
spins = []

# simulation
for _ in range(nsteps):
    
    # choose a spin at a random position
    i,j = np.random.randint(1, L+1), np.random.randint(1, L+1)

    # calculate the local energy cost of a random flip occuring at S_ij
    neighbours = S[i-1][j] + S[i][j-1] + S[i+1][j] + S[i][j+1]
    delta_E = 2 * J * S[i][j] * neighbours
    
    # Metropolis–Hastings algorithm
    if delta_E < 0 or np.random.rand() < np.exp(-delta_E * beta):
        S[i][j] = - S[i][j]

    # store the data each 1000 steps
    if _ % 1000 == 0:
        E_total = 0.0
        # energy of the current configuration
        for i in range(1, L+1):
            for j in range(1, L+1):
                E_total += -J * S[i][j] * (S[i+1][j] + S[i][j+1])
                # only calculate interaction with right and bottom spins to avoid double counting        
        energies.append(E_total)
        spins.append(np.sum(S[1:-1, 1:-1]))

# print the result
print(f'Total spin at equilibrium: S = {np.sum(S[1:-1][1:-1])}')
print(f'Total energy at equilibrium: E = {E_total}')

# plot the result
plt.plot(range(len(energies)), energies, 'b-',label='Total energy of the system')
plt.ylabel('E / J')
plt.xlabel('t / *1000 steps')
plt.legend()
plt.savefig(f'E_beta={beta}_seed={seed}.png')
plt.show()

plt.plot(range(len(spins)), spins, 'r-',label='Total spin of the system')
plt.ylabel('S ')
plt.xlabel('t / 1000 steps')
plt.legend()
plt.savefig(f'S_beta={beta}_seed={seed}.png')
plt.show()

# animation
S = np.random.choice([1,-1],size=(L+2,L+2))  # randomize the initial configuration
def simulate(S):
    for _ in range(nsteps):
        i,j = np.random.randint(1, L+1), np.random.randint(1, L+1)
        neighbours = S[i-1][j] + S[i][j-1] + S[i+1][j] + S[i][j+1]
        delta_E = 2 * J * S[i][j] * neighbours
        if np.random.rand() < np.exp(-delta_E * beta):
            S[i][j] = - S[i][j]
        if _ % 1000 == 0:
            yield S  # store the frame each 1000 steps

fig, ax = plt.subplots(figsize=(6, 6))
cax = ax.matshow(S[1:-1, 1:-1], cmap='coolwarm', vmin=-1, vmax=1)
cbar = fig.colorbar(cax, ax=ax)
cbar.set_ticks([1, -1])
cbar.set_ticklabels(['Up', 'Down'])
ax.set_xticks([])
ax.set_yticks([])  # hide x and y axis

def update(S):
    cax.set_data(S[1:-1, 1:-1])  # update the grid data without boundary
    return [cax]

ani = FuncAnimation(fig, update, simulate(S), interval=10, blit=True)
plt.show()
