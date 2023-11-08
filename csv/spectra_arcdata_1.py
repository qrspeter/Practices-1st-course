import numpy as np
spectra1 = np.loadtxt('WingsMPA_633ex_1mmslit.arc_data', delimiter='\t')
spectra3 = np.loadtxt('WingsEDT_633ex_3mmslit.arc_data', delimiter='\t')

import matplotlib.pyplot as plt
plt.plot(spectra1[:,0], spectra1[:,1], label = '1mm')
plt.plot(spectra3[:,0], spectra3[:,1], label = '3mm')

plt.xlabel('Wavelength, nm', fontsize = 18)
plt.ylabel('Intensity, a.u.', fontsize = 18)
plt.legend(loc = 'upper right')


plt.show()