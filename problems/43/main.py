# Very ugly, but it gets the job done :thumbsup:

#    988 885 855 553 539 390 901
# -> 988         553         901
def paste_together(numbers):
    return f"{numbers[0]:03}{numbers[3]:03}{numbers[6]}"

numbers = []

for d17 in range(0, 999 // 17 + 1):
    for d13 in range(0, 999 // 13 + 1):
        if (17 * d17 // 10) != (13 * d13 % 100):
            continue
        for d11 in range(0, 999 // 11 + 1):
            if (13 * d13 // 10) != (11 * d11 % 100):
                continue
            for d7 in range(0, 999 // 7 + 1):
                if (11 * d11 // 10) != (7 * d7 % 100):
                    continue
                for d5 in range(0, 999 // 5 + 1):
                    if (7 * d7 // 10) != (5 * d5 % 100):
                        continue
                    for d3 in range(0, 999 // 3 + 1):
                        if (5 * d5 // 10) != (3 * d3 % 100):
                            continue
                        for d2 in range(0, 999 // 2 + 1):
                            if (3 * d3 // 10) != (2 * d2 % 100):
                                continue
                            numbers.append(paste_together([2 * d2, 3 * d3, 5 * d5, 7 * d7, 11 * d11, 13 * d13, 17 * d17]))

total = 0
for n in numbers:
    if len(set(n)) != 9:
        continue
    missing_digit = int(list(set("1234567890").difference(n))[0])
    total += int(n) + missing_digit * 1_000_000_000
    print(n)

print("Total:", total)
