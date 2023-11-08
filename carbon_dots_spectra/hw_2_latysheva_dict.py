import matplotlib.pyplot as plt
import numpy as np

path = './csv/'
file_end = '_AS15.2.txt'

low_limit_nm = 400 # nm

def find_max_index(arr, limit):
    max_index = np.argmax(arr[limit:,1])
    return max_index + limit + arr[0,0]

samples = {
'acetone' : ('Acetone', 0.355),
'chcl3': ('CHCl$_3$', 0.309),
'etoh': ('EtOH', 0.654),
'toluene': ('Toluene', 0.099),
'h2o': ('H$_2$O', 1.0),
}

data = []
for i in samples:
    data.append(np.loadtxt(path + i + file_end, skiprows = 2, delimiter = '\t'))
    plt.plot(data[-1][:,0],data[-1][:,1], label=samples[i][0])

plt.title('abs spectra')
plt.xlabel('Wavelength  nm', fontsize=14)
plt.ylabel('Abs',fontsize=14)
plt.legend()
plt.show()

low_limit = 0
while data[0][low_limit,0] < low_limit_nm:
    low_limit += 1

maxl = [find_max_index(i, low_limit) for i in data]

for n, i in enumerate(samples):
    plt.scatter(samples[i][1], maxl[n], s=50, label=samples[i][0])

pol = [samples[i][1] for i in samples]

appr = np.polyfit(pol, maxl,1)
x_pol = np.linspace(0, 1, 100)
plt.plot(x_pol, np.polyval(appr, x_pol), label = 'fit')

plt.title('polarity and maximums')
plt.xlabel('Polarity', fontsize=14)
plt.ylabel('Abs maximum',fontsize=14)
plt.legend()
plt.show()
