# -------------- Simulated generation of fern plants --------------
import numpy as np
import matplotlib.pyplot as plt

# define the transfer matrix and the shift vector
A = np.array(
    [[[0, 0], [0, 0.16]],
    [[0.85, 0.04], [-0.04, 0.85]],
    [[0.2, -0.26], [0.23, 0.22]],
    [[-0.15, 0.28], [0.26, 0.24]]]
    )
b = np.array([[0, 0], [0, 1.6], [0, 1.6], [0, 0.44]])

x = np.array([0,0])  # initialize the first point
points = []

# iteration to generate point sets
nsteps = 100000
for _ in range(nsteps):
    # randomly choose transfer matrix
    random_num = np.random.rand()
    if random_num < 0.01:
        x_new = np.dot(A[0], x) + b[0]
    elif random_num <0.86:
        x_new = np.dot(A[1], x) + b[1]
    elif random_num <0.93:
        x_new = np.dot(A[2], x) + b[2]
    else:
        x_new = np.dot(A[3], x) + b[3]
    x = x_new
    points.append(x_new)
points = np.array(points)

# plot the plants
fig, ax = plt.subplots()
ax.scatter(points[:, 0], points[:, 1], s=0.1, color='green')
ax.set_aspect(0.6)  # adjust aspect ratio
plt.show()
