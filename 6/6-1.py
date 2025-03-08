# ------------------------ Gaussian Elimination ------------------------
import numpy as np

A_b = np.array([[1.3, 6.3, -3.5, 2.8, 1.8],
                [5.6, 0.9, 8.1, -1.3, 16.6],
                [7.2, 2.3, -4.4, 0.5, 15.1],
                [1.5, 0.4, 3.7, 5.9, 36.9]
                ]) # define the augmented matrix

for i in range(0,4):
    if A_b[i,i] == 0:
        for j in range(i+1,4):
            if A_b[j,i] != 0:
                A_b[[i,j]] = A_b[[j,i]] # swap the rows
                break
    for j in range(i+1,4):
        A_b[j] = A_b[j] - (A_b[j,i]/A_b[i,i])*A_b[i] # perform the row operations


x = np.zeros(4)
for i in range(3,-1,-1):
    x[i] = (A_b[i,4] - np.dot(A_b[i,0:4],x))/A_b[i,i] # back substitution

print(f'Gaussian Elimination: the solution to the equations is [x1, x2, x3, x4] = {x}')