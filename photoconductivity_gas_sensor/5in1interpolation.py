import numpy as np
import matplotlib.pyplot as plt
path = './csv/'
name = "I_T_rGO_IPA_p"
ext = ".txt"
kolv = 5
lst = []
for i in range(kolv):
    arr = np.loadtxt(path + name + str(i + 1) + ext, delimiter = ',')
    lst.append(arr)
    
x = np.arange(0, 1411, 2)
pol = []
for i in lst:
    y_interp = np.interp(x, i[:,0], i[:,1])
    pol.append(y_interp)

summ = 0
for i in pol:
    summ += i
arf = summ / kolv
plt.plot(x, arf)
plt.xlabel('Время, с', fontsize=14)
plt.ylabel('Ток, А', fontsize=14)
plt.show()


    