import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,20)
y = np.random.rand(20)
poly = np.polyfit(x,y, deg=2)
plt.plot(x, np.polyval(poly, x), color='red', label = 'fit')
plt.plot(x,y, 'b*', label = 'data')
plt.legend()
plt.show()
