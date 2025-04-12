import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['image.cmap'] = 'gnuplot'

# heat equation evolve
def evolve(u, u_previous, a, dt, dx2, dy2):

    n, m = u.shape
    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) / dx2 + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) / dy2 )
    u_previous[:] = u[:]

# iterate the evolution
def iterate(field, field0, a, dx, dy, timesteps, image_interval):

    dx2 = dx**2
    dy2 = dy**2

    # For stability, dt = 0.1 * the largest interval possible
    dt = 0.1*dx2*dy2 / ( 2*a*(dx2+dy2) )    

    for m in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)

# read the initial temperature field 
def init_fields(filename):
    field = np.loadtxt(filename)
    field0 = field.copy()
    return field, field0

# plot the heat field map
def write_field(field, step):

    plt.figure(figsize=(10, 10))
    plt.gca().clear()
    plt.imshow(field)
    plt.colorbar()
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step),dpi=300)
    plt.clf()


