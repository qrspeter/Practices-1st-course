# plot Raman specra of reduced graphene oxide and another samples. Normalize data.

import numpy as np
import matplotlib.pyplot as plt

csv_dir = './csv/'

arr = np.loadtxt(csv_dir + 'raman_Ag_2_dye_2_1week.txt', delimiter='\t')
plt.plot(arr[:,0],arr[:,1]/np.max(arr[:,1]))
arr = np.loadtxt(csv_dir + 'raman_NPl_glass_10s_5a_P10_488nm.txt', delimiter='\t')
plt.plot(arr[:,0],arr[:,1]/np.max(arr[:,1]))
arr = np.loadtxt(csv_dir +'raman_NP_ITO_10s_5a_P10_488nm.txt', delimiter='\t')
plt.plot(arr[:,0],arr[:,1]/np.max(arr[:,1]))

plt.title('Raman spectrum')
plt.xlabel(r'wavelength, $cm^{-1}$', fontsize=14)
plt.ylabel('интенсивность, отн.ед.', fontsize=14)
plt.show()


    