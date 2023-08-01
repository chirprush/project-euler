import numpy as np
from itertools import count

def u(n):
    return sum((-1 * n) ** i for i in range(11))

def op(k):
    coefficients = np.array(
        [[i ** j for j in range(k)] for i in range(1, k + 1)]
    )
    values = np.array(
        [u(i) for i in range(1, k + 1)]
    )
    polynomial = np.dot(np.linalg.inv(coefficients), values)

    for n in count(k + 1):
        ns = np.array([n ** i for i in range(k)])
        result = round(np.dot(polynomial, ns))

        if u(n) != result:
            return result

print(sum(op(i) for i in range(1, 11)))
