from math import log, floor, ceil

n = 10 ** 4
m = 10 ** 16
p = 1234567891

# The euler totient function evaluated on n = p - 1
tot = 329040288

def reduce_modulo_prime(a, b, p, tot):
    # Our number is of the form a^(2^b) and we're going to reduce it modulo p,
    # using Euler's theorem (the congruence exponentiation one, not any of the
    # other thousands)
    #
    # m = 2 ** (b % tot)
    # print(m, m % (p - 1))
    # return a ** (m % (p - 1))
    # It turns out the builtin pow function is actually kinda goated let's go
    m = pow(2, b, tot)
    return pow(a, m, p)

if __name__ == "__main__":
    shortcut = True

    if shortcut:
        starting = [floor(log(n, b)) for b in range(2, n + 1)]
        log_normalized = [0] * len(starting)
        S = sum(starting)

        for i, c in enumerate(starting):
            starting[i] = c + (m - S) // len(starting)
            log_normalized[i] = starting[i] + log(log(i + 2, 2), 2)

        steps_left = m - sum(starting)
    else:
        starting = [1] * (n - 1)
        log_normalized = [log(i, 2) for i in range(2, n + 1)]
        steps_left = m


    # print(starting)
    # print("Steps left:", steps_left)

    for i in range(steps_left):
        index = log_normalized.index(min(log_normalized))
        starting[index] += 1
        log_normalized[index] += 1
        # log_normalized[index] = starting[index] * log(index + 2, 2)
        
        # print(f"Round {i + 1}")
        # print(" ", starting)
        # print(" ", log_normalized)

    # print(starting)
    # print(sum(i ** (2 ** starting[i - 2]) for i in range(2, n + 1)) % p)
    print(sum(reduce_modulo_prime(i, starting[i - 2], p, tot) for i in range(2, n + 1)) % p)
