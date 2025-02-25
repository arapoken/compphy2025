# ---------------------Sunspot historical data----------------------
# prepare for the necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the data
data = pd.read_csv('SunSpot.txt', delim_whitespace=True, header=None)
data.columns = ['Year', 'Month', 'Day', 'DecimalYear', 'Spot', 'Std', 'Obs']
data_filtered = data.loc[data['Spot'] != -1]
print(data_filtered)

# plot the sunspots number changing with time
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)

ax.plot(data_filtered['DecimalYear'], data_filtered['Spot'], 'k-')
ax.set_xlabel('Year')
ax.set_ylabel('Sunspot number')
plt.savefig('Sunspot.png')
plt.show()
