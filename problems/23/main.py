from sympy.ntheory import factorint
from math import prod

N = 28123

def is_abundant(n):
    factors = factorint(n)
    divisor_sum = prod((p ** (e + 1) - 1) // (p - 1) for p, e in factors.items())
    return divisor_sum > 2 * n

abundants = set()

for i in range(1, N + 1):
    if is_abundant(i):
        abundants.add(i)

print("Calculated abundants")

total = 0

for n in range(1, N + 1):
    print(n)
    ok = False
    for i in abundants:
        if i > n:
            break
        if (n - i) in abundants:
            ok = True
            break
    if not ok:
        total += n

print(total)
