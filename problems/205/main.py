import numpy as np

dice4 = [1 / 4 for i in range(4)]
dice6 = [1 / 6 for i in range(6)]

X = dice4[:]
Y = dice6[:]

for i in range(8):
    X = np.convolve(X, dice4)

for i in range(5):
    Y = np.convolve(Y, dice6)

X = [0, 0, 0] + list(X)
Y = list(Y)

total = 0
for i in range(len(X)):
    total += X[i] * sum(Y[j] for j in range(i))

print(round(total, 7))
