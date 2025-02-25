# ----------------------Liu Hui's pi Algorithm----------------------
# prepare for the nessasary packages
from math import pi,sqrt

# initialize the variables
r = 0.5
k = 6
l_i = r
l_o = 2*r/sqrt(3)


# loop while the accuracy is not enough
while(k*l_i < pi < k*l_o and (k*l_o - k*l_i) > 1e-11):
    
    # the inscribed polygon iteration
    h = sqrt(r**2-(l_i/2)**2)
    delta = r-h
    l_i = sqrt((l_i/2)**2+delta**2)

    # the circumscribed polygon iteration
    H = sqrt((l_o/2)**2+r**2)
    Delta = H-r
    l_o = 2*((l_o/2)**2-Delta**2)/l_o

    # update the value of k
    k = 2*k

# print the result
print('k =',k)
print(f'Lower limit   = {k*l_i:.12f}')
print(f'Approximation = {k*(l_i+l_o)/2:.12f}')
print(f'Upper limit   = {k*l_o:.12f}')