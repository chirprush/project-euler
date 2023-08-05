N = 200

values = [0] * (N + 1)
values[0] = 1

C = [1, 2, 5, 10, 20, 50, 100, 200]

for n in range(1, N + 1):
    for a in C:
        if n - a >= 0:
            values[n] += values[n - a]

print(values)
print(values[N])
