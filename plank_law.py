import matplotlib.pyplot as plt
import numpy as np

h = 6.6*10**-34
k = 1.38*10**-23
c = 3*10**8

sourses = [('Lamp', 2800), ('Human', 313), ('Lamp', 2400), ('Нагретая железка', 870)]
lam_min, lam_max = 500*10**-9, 25000*10**-9

def plank(lam, t):
    b = (2*h*c**2/lam**5)*(1/(np.exp(h*c/(lam*k*t)) - 1))
    return b
lam = np.linspace(lam_min, lam_max, 100)

for i in sourses:
    b = plank(lam, i[1])
    plt.plot(lam, b/b.max(), label = f'{i[0]}: {i[1]}K')


plt.title('Спектр излучения')
plt.xlabel('Длина волны, м', fontsize = 18)
plt.ylabel('Яркость, норм.', fontsize = 18)
plt.legend()
plt.savefig('spectra.png')
plt.show()

