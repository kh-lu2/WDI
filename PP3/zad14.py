import random
import string

key_len = 10
max_dict_size = 7
max_list_size = 3
max_number = 10

my_dict = {
    ''.join(random.choices(string.ascii_letters + string.digits, k=key_len)): 
    [random.randint(1, max_number) for _ in range(random.randint(1, max_list_size))] for _ in range (random.randint(1, max_dict_size))
    }
sort_dict = dict(sorted(my_dict.items(), key=lambda pair: sum(pair[1])))
sum_dict = {key: sum(val) for key, val in sort_dict.items()}
print(my_dict)
print(sort_dict)
print(sum_dict)

print(f"czy dobrze posortowano: {'tak' if all(x <= y for x, y in zip(list(sum_dict.values())[:-1], list(sum_dict.values())[1:])) else 'nie'}")