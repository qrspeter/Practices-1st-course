primary = 100
r = 5.0
n = 7
amount = primary * (1+r/100)**n
print(amount)

print(f"{amount=:.2f}")

print(f"After {n} years, 100 EUR has grown to {amount:.2} EUR.")
print(f"After {n} years, 100 EUR has grown to {amount:.2f} EUR.")
print(f"After {n} years, 100 EUR has grown to {amount:.2e} EUR.")
print(f"After {n} years, 100 EUR has grown to {amount:.2g} EUR.")
'''
import math
round_to_n = lambda x, n: x if x == 0 else round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))
print(round_to_n(2342.343, 5))
'''