# ----------- 10-D hypersphere volume -----------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

N = 10000
n_trials = 10
V_si = np.zeros(n_trials)

for i in range(n_trials):  # perform multiple independent trials
    count = 0
    for j in range(N):
        random_point = np.random.rand(10)
        if(np.sum(random_point**2)<1):
            count += 1  # detect if the random point is in hypersphere
    V_si[i] = (2**10)*count/N  # simulation result in a single trial

mu = np.mean(V_si) # the mean value of n trials
var = np.var(V_si) # the variance of n trials
V_th = np.pi**5/gamma(6)  # theoretical result
error = np.abs(mu - V_th)

print(f'When total throws is {N}, after {n_trials} trials')
print('The simulation resulut is', mu)
print('The theoretical result is', V_th)
print('The error of the integration is', error)
print('The variance of multiple trials is', var)
