filename = 'lists_test_h.txt'

x = [x for x in range(10)]
y = [0.2*x for x in range(10)]

with open(filename, 'w') as fout:
    
    for i in x:
        fout.write(str(i))
        if i != len(x) - 1:
            fout.write(',')        
    fout.write('\n')
    
    for i in y:
        fout.write(str(i) + (i != len(y) - 1) * ',')           
    fout.write('\n')

    
with open(filename, 'r') as fin:
    f = fin.readlines()

x_new = f[0].strip().split(',')
y_new = f[1].strip().split(',')

print(f)
print(x_new)

