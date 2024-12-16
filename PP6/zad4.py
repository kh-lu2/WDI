import time

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


def Fib3(n, fib_dict):
    if n == 1 or n == 2:
        return 1

    if n in fib_dict:
        return fib_dict[n]

    fib_dict[n] = Fib3(n - 1, fib_dict) + Fib3(n - 2, fib_dict)
    return fib_dict[n]

def fib3(n):
    fib_dict = {1: 1, 2: 1}
    return Fib3(n, fib_dict)


with open('M.txt', 'r') as file:
    m = int(file.readline())


print("Format:\n M:  [  iter  ] [  rec   ] [rec+dict]")
for i in range(1, m + 1):
    start, end = [], []
    for j in range(1, 4):
        start.append(time.perf_counter())
        globals()[f"fib{j}"](i)
        end.append(time.perf_counter())
    
    iter_time = end[0] - start[0]
    rec_time = end[1] - start[1]
    rec_dict_time = end[2] - start[2]

    print(f"{i:2}:  [{iter_time:0.6f}] [{rec_time:0.6f}] [{rec_dict_time:0.6f}]")
