PIN = 6969
saldo = 0

def verification():
    return PIN == int(input("Podaj PIN: "))


print("Witaj w bankomacie. Mozesz sprawdzac saldo (1), wplacac (2) i wyplacac (3) pieniadze oraz wyjsc z programu (0)")
action = int(input("Od czego zaczynamy? "))
while action:
    match action:
        case 1:
            if verification():
                print(f"Twoje saldo wynosi {saldo}")
            else:
                print("Zly PIN")
        case 2:
            if verification():
                wplata = int(input("Ile chcesz wplacic? "))
                if (wplata < 0):
                    print("Nie mozna wplacic kwoty ujemnej")
                else:
                    saldo = saldo + wplata
            else:
                print("Zly PIN")
        case 3:
            if verification():
                wyplata = int(input("Ile chcesz wyplacic? "))
                if wyplata < 0:
                    print("Nie mozna wyplacic kwoty ujemnej")
                elif wyplata > saldo:
                    print("Nie masz tyle na koncie!")
                else:
                    saldo = saldo - wyplata
            else:
                print("Zly PIN")
        case _:
            print("Nie ma takiej operacji")
        
    action = int(input("Co chcesz zrobic w kolejnym kroku? "))
