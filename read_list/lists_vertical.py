# Make a "vertical" 2D array (with 2 columns), write it to a file, read and print.

filename = 'lists_test_v.txt'

x = [x for x in range(10)]
y = [0.2*i for i in x]

with open(filename, 'w') as fout:


    for i, a in enumerate(x):
        fout.write(str(x[i]) + ',' + str(y[i]))
        fout.write('\n')
   
    
with open(filename, 'r') as fin:
    f = fin.readlines()
    
n = len(f)
x_2, y_2 = [None]*n, [None]*n
for i, a in enumerate(f):
    x_2[i], y_2[i] = list(map(float,a.strip().split(',')))
print(x_2)
print(y_2)


