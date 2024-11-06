inp = input()
uni_litery = list(filter(lambda char: char.isalpha() and inp.count(char) == 1, set(inp)))

print(uni_litery)
print(inp)