from numpy import random
import numpy as np
import matplotlib.pyplot as plt

def filter(arr, n):
    assert n % 2 == 1, "n must be odd"
    assert n < len(arr), "n > len(arr)"

    num_begin, num_end = (n-1)//2, len(arr) - (n-1)//2 - 1
    filter_arr = np.full_like(arr,0)
    for i in range(len(arr)):#range(num_1, num_2 + 1):
        if i < num_begin:
            filter_arr[i] = np.sum(arr[:i + (n - 1)//2]) + arr[0]*((n-1)//2 - i)
        elif i > num_end: 
            filter_arr[i] = np.sum(arr[i - (n -1)//2:]) + arr[-1]*(len(arr) - i + (n -1)//2)
        else:
            filter_arr[i] = np.sum(arr[i-num_begin:i+num_begin + 1])
    return filter_arr/n
    
random.seed(1)
rand = random.random((42))
plt.plot(rand, label='original')
n = 5
plt.plot(filter(rand, n), label=f'{n=}')
n += 2
plt.plot(filter(rand, n), label=f'{n=}')
plt.legend()
plt.show()



