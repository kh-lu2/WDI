"""
                                               .--.
                                               `.  \
                                                 \  \
                                                  .  \
                                                  :   .
                                                  |    .
                                                  |    :
                                                  |    |
  ..._  ___                                       |    |
 `."".`''''""--..___                              |    |
 ,-\  \             ""-...__         _____________/    |
 / ` " '                    `""""""""                  .
 \                                                      L
 (>                                                      \
/                                                         \
\_    ___..---.                                            L
  `--'         '.                                           \
                 .                                           \_
                _/`.                                           `.._
             .'     -.                                             `.
            /     __.-Y     /''''''-...___,...--------.._            |
           /   _."    |    /                ' .      \   '---..._    |
          /   /      /    /                _,. '    ,/           |   |
          \_,'     _.'   /              /''     _,-'            _|   |
                  '     /               `-----''               /     |
                  `...-'                                       `...-'
"""

# wczytanie dwoch liczb
n, m = map(float, input("Wpisz dwie liczby oddzielone spacja: ").split())

# czy obie sa rowne 0
if n < 0 and m < 0:
    print("Dwie liczby sa mniejsze od 0")
    exit()

if n < 0:
    n = -n

if m < 0:
    m = -m

print(f"{n} + {m} = {n + m}")
print(f"{n} - {m} = {n - m}")
print(f"{n} * {m} = {n * m}")
if n * m == 10:
    print("Yay!")

if m == 0:
    print("Nie mozna dzielic przez 0!")
else:
    print(f"{n} / {m} = {n / m}")
    
print(f"{n}^2 = {n ** 2}, {m}^2 = {m ** 2}")
print(f"sqrt({n}) = {n ** 0.5}, sqrt({m}) = {m ** 0.5}")