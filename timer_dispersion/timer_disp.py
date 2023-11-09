# Calculate average and dispersion for data from a timer in file.

filename = 'time.txt'

def load_data():
    with open(filename,'r',encoding='utf8') as fin:
        f = fin.readlines()
        n = len(f)
        lst = []
        for i in f:
            lst.append(float(i.strip()))
        return lst
        
def av(f):
    s = 0
    for i in f:
        s = s + i
    return s / len(f)
   
    
def sigma(f):
    n=len(f)
    summ=0
    aver=av(f)
    for i in f:
        summ+=(i-aver)**2
    return(((1)/(n-1)*summ)**0.5)
       

lst=load_data()
print(f"Среднее равнo {av(lst):.3f}")
print(f"Среднее отклонениe равнo {sigma(lst):.3f}")