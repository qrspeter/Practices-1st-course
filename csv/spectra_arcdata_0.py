import matplotlib.pyplot as plt

spectra = []
with open('WingsMPA_633ex_1mmslit.arc_data', 'r', encoding='cp1251') as fin:
    for line in fin:
        if line[0] != '#':
            if line == '\n':
                continue

            now = line.strip().split('\t')
            spectra.append(list(map(float, now)))

# тоже работающий вариант
# import numpy as np
# xy = np.array(spectra) # https://www.geeksforgeeks.org/how-to-plot-list-of-x-y-coordinates-in-matplotlib/
# x, y = xy.T
# plt.plot(x, y)

x, y = zip(*spectra) # https://www.delftstack.com/howto/matplotlib/how-to-plot-list-of-coordinates-in-matplotlib/
plt.plot(x, y)
plt.show()
