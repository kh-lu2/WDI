def fib1(n):
    if n == 1 or n == 2:
        return 1
    
    a, b, c, step = 1, 1, 2, 3
    while step < n:
        a, b = b, c
        c = a + b
        step = step + 1

    return c

def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


fib_dict = {1: 1, 2: 1}
def fib3(n):
    if n == 1 or n == 2:
        return 1

    if n in fib_dict:
        return fib_dict[n]

    fib_dict[n] = fib3(n - 1) + fib3(n - 2)
    return fib_dict[n]


for i in range(1, 10):
    print(f"{fib1(i)} {fib2(i)} {fib3(i)}")


