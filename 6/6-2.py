# ------------------------ LU Decomposition ------------------------
import numpy as np
A = np.array([[1.3, 6.3, -3.5, 2.8],
                [5.6, 0.9, 8.1, -1.3],
                [7.2, 2.3, -4.4, 0.5],
                [1.5, 0.4, 3.7, 5.9]
                ]) # define the coefficient matrix
b = np.array([1.8, 16.6, 15.1, 36.9])
L = np.zeros((4,4))
U = np.diag(np.ones(4))

# calculate the L and U matrices
for k in range(0,4):
    for i in range(k,4):
        L[i,k] = A[i,k] - np.dot(L[i, 0:k],U[0:k, k])
    for j in range(k+1,4):
        U[k,j] = (A[k,j] - np.dot(L[k,0:k],U[0:k,j]))/L[k,k]
print('The L matrix is:\n', L)
print('The U matrix is:\n', U)

# solve L·y = b
y = np.zeros(4)
for i in range(0,4):
    y[i] = (b[i] - np.dot(L[i,0:i],y[0:i]))/L[i,i] # forward substitution
print('The y vector is:\n', y)

# solve U·x = y
x = np.zeros(4)
for i in range(3,-1,-1):
    x[i] = (y[i] - np.dot(U[i, i+1:4], x[i+1:4]))/U[i,i] # back substitution
    
print(f'LU Decomposition: the solution to the equations is [x1, x2, x3, x4] = {x}')
