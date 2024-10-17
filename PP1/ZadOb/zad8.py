import random

n = int(input("Wprowadz liczbe calkowita nieujemna: "))

if n == 0:
    exit()

print(" " * (n - 1) + "X")
for i in range(1, n):
    blank = n - 1 - i
    row = " " * blank + "*" * (2 * i + 1)

    id = random.randrange(0, 2 * i + 1) + blank
    row = row[:id] + "o" + row[id + 1:]

    print(row)

print(" " * (n - 1) + "U")