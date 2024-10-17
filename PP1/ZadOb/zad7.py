n = int(input("Wprowadz dwie liczby oddzielone enterem: "))
m = int(input())

assert isinstance(n, int)
assert isinstance(m, int)
assert n <= m

if m - n + 1 <= 20:
    print(' '.join(map(str, range(n, m + 1))))
else:
    mid = (n + m) // 2
    if (n + m) % 2:
        print(' '.join(map(str, range(mid - 2, mid + 4))))
    else:
        print(' '.join(map(str, [i for i in range(mid - 3, mid + 4) if i != mid])))     
    