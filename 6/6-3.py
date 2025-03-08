# ------------------------ Gauss-Seidel method ------------------------
import numpy as np
A_b = np.array([[1.3, 6.3, -3.5, 2.8, 1.8],
                [5.6, 0.9, 8.1, -1.3, 16.6],
                [7.2, 2.3, -4.4, 0.5, 15.1],
                [1.5, 0.4, 3.7, 5.9, 36.9]
                ]) # define the augmented matrix
B = np.zeros((4,4))
g = np.zeros(4)

# preprocess the matrix to make the diagonal elements dominant(to avoid divergence)
for i in range(0,4):
    max = A_b[i][i]
    max_index = i
    for j in range(i,4):
        if A_b[j][i] > max:
            max = A_b[j][i]
            max_index = j
    if max_index != i:
        A_b[[i,max_index]] = A_b[[max_index,i]] # swap the rows
print('The matrix after preprocessing is:\n', A_b)

# calculate the B matrix and g vector
for i in range(0,4):
    for j in range(0,4):
        if i != j:
            B[i][j] = -A_b[i][j]/A_b[i][i]
    g[i] = A_b[i][4]/A_b[i][i]
print('B matrix is:\n', B)
print('g vector is:\n', g)

# Jacobi method
x = np.zeros(4)
x_new = np.zeros(4)
for i in range(0,4):
    x_new[i] = np.dot(B[i],x) + g[i] # calculate the new x vector at first
n = 1
while(np.abs(x_new - x) > 0.00001).any():
    x[:] = x_new # update the x vector
    for i in range(0,4):
        x_new[i] = np.dot(B[i],x) + g[i] # calculate the new x vector
    # print(x_new)
    n += 1
print(f'Jacobi method: the number of iterations is {n}')
print(f'Jacobi method: the solution to the equations is [x1, x2, x3, x4] = {x_new}')

# Gauss-Seidel method
x = np.zeros(4)
x_new = np.zeros(4)
for i in range(0,4):
    x_new[i] = g[i]
    for j in range(0,i):
        x_new[i] += B[i][j] * x_new[j]
    for j in range(i,4):
        x_new[i] += B[i][j] * x[j] # calculate the new x vector at first
n = 1
while(np.abs(x_new - x) > 0.00001).any():
    x[:] = x_new # update the x vector
    for i in range(0,4):
        x_new[i] = g[i]
        for j in range(0,i):
            x_new[i] += B[i][j] * x_new[j]
        for j in range(i,4):
            x_new[i] += B[i][j] * x[j] # calculate the new x vector
    # print(x_new)
    n += 1
print(f'Gauss-Seidel method: the number of iterations is {n}')
print(f'Gauss-Seidel method: the solution to the equations is [x1, x2, x3, x4] = {x_new}')
