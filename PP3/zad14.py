import random
import string

key_len = 3
max_dict_size = 7
max_list_size = 3
max_number = 10

my_dict = {
    ''.join(random.choices(string.ascii_letters + string.digits, k=key_len)): 
    [random.randint(1, max_number) for _ in range(random.randint(1, max_list_size))] 
    for _ in range (random.randint(1, max_dict_size))
    }

sort_dict = dict(sorted(my_dict.items(), key=lambda item: sum(item[1])))
sum_dict = {key: sum(val) for key, val in sort_dict.items()}
print(my_dict)
print(sort_dict)
print(sum_dict)
