# ----------------- 2-D Ising model simulation -----------------
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

beta = 1.0
J = 1.0
L = 20
nsteps = 100000  # maxium simulation steps

fig, ax = plt.subplots(1,2, figsize=(10,4))

current_time = int(time.time())
np.random.seed(current_time)
seeds = np.random.randint(0, 1e4, size=5)
colors = ['blue', 'green', 'red', 'purple', 'orange']

for idx, seed in enumerate(seeds):
    np.random.seed(seed)
    S = np.random.choice([1,-1],size=(L+2,L+2))  # randomize the initial configuration
    S[0][:], S[:][0], S[L+1][:], S[:][L+1] = 0, 0, 0, 0  # boundary condition

    energies = []
    spins = []

    # simulation
    for _ in range(nsteps):
        
        # randomly choose a spin
        i,j = np.random.randint(1, L+1), np.random.randint(1, L+1)

        # calculate the local energy cost of a random flip
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
    print(f'When beta = {beta}, seed = {seed}:')
    print(f'Total energy at equilibrium: E = {E_total}')
    print(f'Total spin at equilibrium: S = {np.sum(S[1:-1][1:-1])}')
    
    ax[0].plot(range(len(energies)), energies, color=colors[idx], label=f'seed = {seed}')
    ax[1].plot(range(len(spins)), spins, color=colors[idx], label=f'seed = {seed}')

ax[0].set_ylabel('E / J')
ax[0].set_xlabel('t / 1000 steps')
ax[0].set_title(f'Total energy when beta={beta}')
ax[0].legend()
ax[1].set_ylabel('S')
ax[1].set_xlabel('t / 1000 steps')
ax[1].set_title(f'Total spin when beta={beta}')
ax[1].legend()

plt.tight_layout()
plt.savefig(f'10-1_beta={beta}_T={1/beta:.1f}.png')
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

ani = FuncAnimation(fig, update, simulate(S), interval=100, blit=True)
plt.show()
