FILENAME = "ascii_codes.txt"

def read_file (filename):
    codes = {}
    with open(filename, 'r') as file:
        for line in file:
            char, code = line[0], line[1:]
            codes[char] = int(code)
    return codes

def compare(user_codes, flag):
    inp = input()
    user_res, pyt_res = '', ''
    for char in inp:
        user_res = user_res + str(user_codes[char]) + " "
        pyt_res = pyt_res + str(ord(char)) + " "

    if (flag == "check"):
        print("okej" if user_res == pyt_res else "zle kody")
        return
    # flag == "print"
    print(f"{user_res}\n{pyt_res}")

def manage(filename, flag):
    user_codes = read_file(filename)
    compare(user_codes, flag)

def flag_check(flag):
    return flag == "check" or flag == "print"

def main():
    cnt = int(input("ile sprawdzen: "))
    for _ in range(0, cnt):
        flag = ''
        while not flag_check(flag):
            flag = input("wpisz poprawna flage (check lub print): ") 
        manage(FILENAME, flag)

main()