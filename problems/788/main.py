from math import comb

mod = 1_000_000_007

def d(n):
    if (n % 2 == 0):
        m = n // 2
        T = 9 * pow(10, n, mod) // 2 % mod
    else:
        m = (n - 1) // 2
    total = 0
    for k in range(m + 1, n + 1):
        total += (comb(n, k) % mod) * pow(9, n - k, mod)
    total = 9 * total % mod
    if (n % 2 == 0):
        print(T, total)
    return total

def D(n):
    total = 0
    for k in range(1, n + 1):
        print(k)
        total += d(k) % mod
    return total % mod

# Too slow :(
print(D(2022))

# I ended up using Mathematica, but it feels like it's cheating almost lol
