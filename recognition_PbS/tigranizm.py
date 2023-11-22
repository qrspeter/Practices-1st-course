import numpy as np
import matplotlib.pyplot as plt

lmin = 1000
lmax = 1700
step = 5 

arr = np.loadtxt('./csv/PbS1060 +iso on glass drop.arc_data')
normarr = np.array(arr[:,1]/np.max(arr[:,1]))
x = np.arange(lmin, lmax, step)
interp = np.interp(x, arr[:,0], normarr, left=0, right=0)

plt.plot(x, interp)
plt.show()
print(interp)