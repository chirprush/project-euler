accum = 0

with open("nums") as file:
    for line in file:
        i = int(line)
        accum += i

print(accum)
