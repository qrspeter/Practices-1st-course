# Make a random data and apply polynomial approximation with different degree.


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10)
y = np.random.rand(10)
poly = np.polyfit(x,y, deg=2)
plt.plot(x, np.polyval(poly, x), color='red', linewidth=1, label = 'fit')
plt.plot(x,y, 'b*', linewidth=1, label = 'data')
plt.legend()
plt.show()
   