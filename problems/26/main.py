from sympy.ntheory import factorint, primerange
from math import prod

class PairGenerator:
    def __init__(self, maxes):
        self.maxes = maxes
        self.M = len(maxes)
        self.N = prod(i + 1 for i in maxes)
        self.values = [0] * self.M

    def __iter__(self):
        return self

    def __next__(self):
        self.values[0] += 1

        for i in range(1, self.M):
            if self.values[i - 1] > self.maxes[i - 1]:
                self.values[i - 1] = 0
                self.values[i] += 1

        if (self.values[-1] > self.maxes[-1]):
            raise StopIteration()

        return self.values[:]

def discrete_log10(p):
    # p is the modulus
    factors = factorint(p - 1)
    generator = PairGenerator(list(factors.values()))
    bases = list(factors.keys())

    value = p - 1
    for factorization in generator:
        n = prod(bases[i] ** exp for i, exp in enumerate(factorization))
        if pow(10, n, p) == 1:
            value = min(value, n)

    return value

values = []
for p in primerange(3, 1000):
    values.append((p, discrete_log10(p)))

print(max(values, key=lambda pair: pair[1]))
