import numpy as np
dk1 = np.loadtxt('p56_351_42mkJ_50Hz_5min_ddab2mkl.asc', comments='*', skiprows=10, delimiter=' ')
dk2 = np.loadtxt('p56_351_42mkJ_50Hz_5min_ddab64mkl.asc', comments='*', skiprows=10, delimiter=' ')


dk1[:,0] = dk1[:,0]/10**6
dk2[:,0] = dk2[:,0]/10**6


import matplotlib.pyplot as plt
plt.plot(dk1[:,0], dk1[:,1], label = r'2$\mu$l')
plt.plot(dk2[:,0], dk2[:,1], label = r'64$\mu$l')


# от приложения стилей ничего не меняется, хотя в своеи я порядок цветов поменял...
# или надо файлы поместить в папку стилей?
# а то меняешь толшину линий, засечки - никакого изменения
#plt.style.use('style_peter.mplstyle')
#plt.style.use('signature.mplstyle')
#plt.style.use('.\example.mplstyle')

plt.xlabel('Time (ms)', fontsize = 18)
plt.ylabel('Intensity (a.u.)', fontsize = 18)
plt.legend(loc = 'upper right')

# 

plt.show()