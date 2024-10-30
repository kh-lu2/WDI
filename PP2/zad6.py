s = ''.join(input().split('0')[1:-1])
print(s)

ascii = set()
for i in range(0, len(s)):
    print(s[i], ord(s[i]))
    ascii.add(ord(s[i]))

if (len(ascii) < 5):
    print("Za malo roznych znakow")
else:
    print(sorted(ascii)[-5])
