# Fit the fluorescence decay of PbS quantum dots with exponential function using numpy only.
# Find the decay constant.

import numpy as np
import matplotlib.pyplot as plt


x_data = np.array([0,13,26,41,55,81,123,166]) 
y_data = np.array([35,27,20,13,9,6,2,1])

fit = np.polyfit(x_data, np.log(y_data), 1)

print(f'fitted parameters are {fit}') # [-0.02190002  3.51918842]

y = np.exp(fit[1]) * np.exp(fit[0]*x_data)
decay_t = np.abs(1/fit[0])

plt.plot(x_data, y_data, "o", label = 'data')
plt.plot(x_data, y, label = rf'$\tau$ = {decay_t:.1f}')
plt.legend()
plt.yscale('log')
plt.show()