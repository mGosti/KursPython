import random
from random import randint
def join_text(*args):
    print("-".join(args))

text = ["la", "la", "mi", "do"]

join_text(*text)

def write_up(**kwargs):
    for a,b in kwargs.items():
        print(f"{a} = {b}")

write_up(
    first_name="Mikołaj",
    age=134
)

def list_generator(number_of_items):
    list = []
    while len(list) < number_of_items:
        list.append(random.randint(0,100))
    return list

list_1 = list_generator(5)
list_2 = list_generator(3)

print(list_1)
print(list_2)

list_3 = (*list_1,*list_2)
print(list_3)

dict_1 = {
    "a":1,
    "b":2,
    "c":3
}

dict_2 = {
    "x" : 99,
    "y" : 0
}

dict_3 = {**dict_1, **dict_2}
write_up(**dict_3)


