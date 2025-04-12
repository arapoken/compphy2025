import time
import numpy as np
from mpi4py import MPI

import os
current_path = os.path.dirname(__file__)
os.chdir(current_path)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set the colormap
plt.rcParams['image.cmap'] = 'gnuplot'

# physics parameters
a = 0.5                   # Diffusion constant
timesteps = 100000        # Total Number of time-steps
image_interval = 4000     # Time interval to save png files

# Grid spacings
dx = 0.01
dy = 0.01
dx2 = dx**2
dy2 = dy**2

# For stability, set dt = 0.1* largest interval possible
dt = 0.1*dx2*dy2 / ( 2*a*(dx2+dy2) )

# MPI globals
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Up/down neighbouring MPI ranks
up = rank - 1
if up < 0:
    up = MPI.PROC_NULL
down = rank + 1
if down > size - 1:
    down = MPI.PROC_NULL

# heat equation evolve
def evolve(u, u_previous, a, dt, dx2, dy2):
    u[1:-1, 1:-1] = u_previous[1:-1, 1:-1] + a * dt * ( \
            (u_previous[2:, 1:-1] - 2*u_previous[1:-1, 1:-1] + \
             u_previous[:-2, 1:-1]) / dx2 + \
            (u_previous[1:-1, 2:] - 2*u_previous[1:-1, 1:-1] + \
                 u_previous[1:-1, :-2]) / dy2 )
    u_previous[:] = u[:]

# read the initial temperature field from file
def init_fields(filename):
    field = np.loadtxt(filename)
    field0 = field.copy() 
    return field, field0

# plot the time evolution of heat map
def write_field(field, step):
    plt.figure(figsize=(10,10))
    plt.gca().clear()
    plt.imshow(field,vmin=0, vmax=100)
    plt.colorbar()
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step),dpi=300)
    plt.clf()

# exchange between down and up sections
def exchange(field):
    # send down, receive from up
    sbuf = field[-2,:]
    rbuf = field[0,:]
    comm.Sendrecv(sbuf, dest=down, recvbuf=rbuf, source=up)
    # send up, receive from down
    sbuf = field[1,:]
    rbuf = field[-1,:]
    comm.Sendrecv(sbuf, dest=up, recvbuf=rbuf, source=down)

# iterate the time step, gather and write the field map when at the interval
def iterate(field, local_field, local_field0, timesteps, image_interval):
    for m in range(1, timesteps+1):
        exchange(local_field0)
        evolve(local_field, local_field0, a, dt, dx2, dy2)
        # print the map at interval
        if m % image_interval == 0:
            comm.Gather(local_field[1:-1,:], field, root=0)
            if rank == 0:
                write_field(field, m)

# main function
def main():

    # initial time 
    t0 = time.time()

    # read the initial temperature field
    if rank == 0:
        field, field0 = init_fields('bottle.dat')
        shape = field.shape
        dtype = field.dtype
        comm.bcast(shape, 0)  # broadcast dimensions
        comm.bcast(dtype, 0)  # broadcast data type
    else:
        field = None
        shape = comm.bcast(None, 0)
        dtype = comm.bcast(None, 0)

    # error when shape not divided by size
    if shape[0] % size:
        raise ValueError('Number of rows in the temperature field (' \
                + str(shape[0]) + ') needs to be divisible by the number ' \
                + 'of MPI tasks (' + str(size) + ').')

    # number of rows for each MPI process
    n = int(shape[0] / size) 
    print("process#: ",size,"  ,shape: ",shape[0],"   ,n: ", n)

    # number of columns in the field
    m = shape[1]
    buff = np.zeros((n, m), dtype)
    comm.Scatter(field, buff, 0)  # scatter the data

    local_field = np.zeros((n + 2, m), dtype)  # need two ghost rows!
    local_field[1:-1,:] = buff                 # copy data to non-ghost rows
    local_field0 = np.zeros_like(local_field)  # array for previous time step

    # Fix outer boundary ghost layers to account for aperiodicity
    if True:
        if rank == 0:
            local_field[0,:] = local_field[1,:]
        if rank == size - 1:
            local_field[-1,:] = local_field[-2,:]
    local_field0[:] = local_field[:]

    # Plot/save initial field
    if rank == 0:
        write_field(field, 0)

    # Iterate
    iterate(field, local_field, local_field0, timesteps, image_interval)
    t1 = time.time()

    # Plot/save final field
    comm.Gather(local_field[1:-1,:], field, root=0)

    t1 = time.time()
    if rank == 0:
        write_field(field, timesteps)
        print("Running time: {0}".format(t1-t0))

if __name__ == '__main__':
    main()
