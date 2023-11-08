import numpy as np
spectra1 = np.loadtxt('18 Si photodiode_003_001.arc_data', delimiter='\t')
spectra2 = np.loadtxt('18 Si photodiode_003_002.arc_data', delimiter='\t')
spectra3 = np.loadtxt('18 Si photodiode_003_003.arc_data', delimiter='\t')
spectra4 = np.loadtxt('18 Si photodiode_003_004.arc_data', delimiter='\t')

spectraAv = (spectra1+spectra2+spectra3+spectra4)/4

import matplotlib.pyplot as plt
plt.plot(spectraAv[:,0], spectraAv[:,1], label = 'Average')

plt.xlabel('Wavelength, nm', fontsize = 18)
plt.ylabel('Intensity, a.u.', fontsize = 18)
plt.legend(loc = 'upper right')

plt.show()