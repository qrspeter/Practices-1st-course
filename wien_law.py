import math 
b = 0.0029

def wienconv(t): 
    if t <= 0 or t >= 10e6:
        return math.nan ## NaN
    rez = b/t*10**6
    return rez

c = True

while c:
    t = int(input('Введите температуру тела в К: '))
    l = wienconv(t)
    c = math.isnan(l)

print(f'Длина волны максимума излучения {l:.2f} мкм')