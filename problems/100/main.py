import numpy as np
from itertools import count

# Quite the beautiful solution in my opinion, and I hope to perhaps write up a
# solution to this sometime later.
# If we write out the problem algebraically, and expand some things, we can
# express the problem as a solution to a negative Pell equation. Using matrices
# to iterate through this recurrence (this part was probably not needed due to
# how fast the recurrence grows), we can easily find our specified solution.

R = np.array([
    [3, 4],
    [2, 3]
], dtype=np.uint64)

T_0 = np.array([
    [1],
    [1]
], dtype=np.uint64)

for n in count():
    output = np.matmul(np.linalg.matrix_power(R, n), T_0)
    D = int(output[0][0])
    N = int(output[1][0])
    b_plus_r = (D + 1) // 2
    if b_plus_r >= 10 ** 12:
        b = (N + 1) // 2
        r = (1 - 2 * b + D) // 2
        print(f"(blue, red): {(b, r)}")
        break
