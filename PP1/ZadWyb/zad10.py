a, b, c = map(int, input("Wprowadz trzy liczby calkowite: ").split())

if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
    print("Liczby nie sa calkowite")
    exit()

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

print(f"NWD tych liczb to {gcd(a, gcd(b, c))}")