inp = ''.join(input().split('0')[1:-1])
print(inp)

ascii = set()
for character in inp:
    ascii_val = ord(character)
    print(character, ascii_val)
    ascii.add(ascii_val)

if (len(ascii) < 5):
    print("Za malo roznych znakow")
else:
    print(sorted(ascii)[-5])
