# ---------------------Leibniz formula for pi----------------------
# prepare for the nessasary packages
from math import sqrt
from sympy import N,pi

# initialize the variables
z = 1/sqrt(3)
k = 0
f = 0

# loop while the accuracy is not enough
while(abs(6*f-pi) > 1e-15):
    f = f + (-1)**k * z**(2*k+1) / (2*k+1)
    k = k+1

# print the result
print('k =',k)
print(f'the Leibniz  pi = {6*f:.16f}')
print(f'the standard pi = {N(pi,50)}')