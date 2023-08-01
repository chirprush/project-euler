n = 11
m = 101

numbers = list(range(2, n + 1))
squaring = [0] * (n - 1)

print("Round 0")
print("  " + str(numbers))
print("  " + str(squaring))

print()

for i in range(m):
    index = numbers.index(min(numbers))

    numbers[index] **= 2
    squaring[index] += 1

    # if index == n - 2:
    # print(f"Round {i + 1}")
    # print("  " + str(numbers))
    # print("  " + str(squaring))
    # print()
print(squaring)
