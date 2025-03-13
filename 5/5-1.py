# ------------------ Search for gaussian signal in the background ------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, 'higgs-data.txt')

df = pd.read_csv(file_path, sep=', ', engine='python', header=None) # read the file 
x_data, y_data = df[0], df[1]

def func(x, A, B, C, D, E): # define the sum function
    BG = A*np.exp(-x/B)
    SN = C/(D*np.sqrt(2*np.pi))*np.exp(-(x-E)**2/(2*D**2))
    return BG+SN
def BG(x, A, B): # define the background function
    return A*np.exp(-x/B)
def SN(x, C, D, E): # define the signal function
    return C/(D*np.sqrt(2*np.pi))*np.exp(-(x-E)**2/(2*D**2))

p0 = [max(y_data), 1.0, max(y_data)/2, 1.0, np.median(x_data)] # set initial parameters 
popt, pcov = curve_fit(func, x_data, y_data, p0=p0) # fit the data points with the function above
print(popt)
print(pcov)

xx = np.linspace(min(x_data), max(x_data), 1000)
plt.plot(x_data, y_data, 'o', c='black') # plot the total data points
plt.plot(xx, func(xx, *popt), 'r-') # plot the BG+SN fit
plt.plot(xx, BG(xx, *popt[:2]), 'r--') # plot the BG fit
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data points', 'BG+SN fit', 'BG fit'])
plt.show()

plt.plot(x_data, y_data - BG(x_data, *popt[:2]), 'o', c='black') # plot the signal data points
plt.plot(xx, SN(xx, *popt[2:]), 'r-') # plot the SN Gaussian fit
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data points','SN fit'])
plt.show()