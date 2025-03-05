# ------------------ Fitting of the Cosmic Microwave Background Radiation ------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k
from scipy.optimize import curve_fit

df = pd.read_csv('cmb-data.txt', sep=r'\s+', engine='python', header=None) # read the file 
v_data, I_data = df[0], df[1] # get the data in CGS
h_cgs, c_cgs, k_cgs = h*1e7, c*1e2, k*1e7 # convert the units of constants to CGS

def Bv(v, T): # define the Blackbody radiation spectrum function
    return 2*h_cgs*v**3*c_cgs**2 / (np.exp(h_cgs*c_cgs*v / (k_cgs*T)) - 1) # get the result in CGS

p0 = [3.0]
popt, pcov = curve_fit(Bv, v_data, I_data, p0=p0) # fit the data points with the function above
t_CMB = popt[0]
print(f'The temperature of CMB is {t_CMB:.4f} K')

vv = np.linspace(min(v_data), max(v_data), 1000)
plt.figure(figsize=(10,6))
plt.plot(v_data, I_data, 'r+') # plot the data points
plt.plot(vv, Bv(vv, *popt), 'b-') # plot the Bv fit
plt.xlabel('v/(cm^-1)')
plt.ylabel('I/(erg s^-1 cm^-2 sr^-1)')
plt.legend(['Data points', f'Bv fit(T={t_CMB:.4f}K)'])
plt.show()
