# Read three fluorescence spectra of carbon dots from files (2_3k_water_5_cd.txt, 1_3k_water_28_cd.txt, 2_3k_water_10_cd.txt) and plot a graph.

import numpy as np
import matplotlib.pyplot as plt
path = './csv/'
sour = ['2_3k_water_5_cd.txt', '1_3k_water_28_cd.txt', '2_3k_water_10_cd.txt']
for i in sour:
    arr = np.loadtxt(path + i, skiprows = 2, delimiter='\t')
    plt.plot(arr[:,0],arr[:,1])

plt.title('Raman spectrum')
plt.xlabel(r'wavelength, $cm^{-1}$', fontsize=14)
plt.ylabel('интенсивность, отн.ед.', fontsize=14)
plt.show()


    