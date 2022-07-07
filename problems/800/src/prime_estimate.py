# Gives a rough estimate for the range of primes that we need
from math import log2
from itertools import count

H1 = lambda p, q: p * log2(q) + q * log2(p)
maximum_bound = 800800 * log2(800800)

for i in count(3):
    if H1(2, i) >= maximum_bound:
        print(i)
        break
