import random

print("Wprowadz dwie liczby oddzielone ENTERem, a potem symbol odpowiedniego dzialania \n + -> dodawania" 
      "\n - -> odejmowania \n * -> mnozenia \n / -> dzielenia \n # -> pierwiastkowania (x ty pierwiastek z y) \n"
      " ^ -> potegowanie (x to ytej potegi) \n x -> losowanie liczby z zakresu)")


while 69:
    x = int(input())
    y = int(input())
    d = input()

    match d:
        case "+":
            print(f"{x} + {y} = {x + y}")
        case "-":
            print(f"{x} - {y} = {x - y}")
        case "*":
            print(f"{x} * {y} = {x * y}")
        case "/":
            if y == 0:
                print("Nie mozna dzielic przez 0!")
            else:
                print(f"{x} / {y} = {x / y}")
        case "#":
            print(f"{x} # {y} = {y ** (1.0/x)}")
        case "^":
            print(f"{x} ^ {y} = {x ** y}")
        case "x":
            if x > y:
                print("Zly zakres")
            else:
                print(f"Liczba losowa z zakresu [{x}, {y}]: {random.uniform(x, y)}")
        case _:
            print("Nie znam takiej operacji")

    e = input("Czy chcesz wprowadzic nowe dane (T/N)? ")
    while e != "T" and e != "N":
        e = input("Nie wiem co to znaczy. Wpisz jeszcze raz (T/N) ")
    if e == "N":
        exit()


