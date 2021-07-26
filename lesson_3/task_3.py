# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
# p.s. присутствует выделение цветом

import numpy as np
from termcolor import colored

list_1 = list(np.random.permutation(np.arange(0, 100))[:10])

print(f"Изначальный список: {list_1}")
min_i = list_1.index(min(list_1))
max_i = list_1.index(max(list_1))
var = list_1[min_i]
list_1[min_i], list_1[max_i] = list_1[max_i], var

print("Изменённый список: ", end=' ')
for num, i in enumerate(list_1):
    if num == min_i:
        if num == (len(list_1) - 1):
            print(colored(i, 'red'), end=']')
        elif num == 0:
            print(f"[{colored(i, 'red')}", end=', ')
        else:
            print(colored(i, 'red'), end=', ')
    elif num == max_i:
        if num == (len(list_1) - 1):
            print(colored(i, 'red'), end=']')
        elif num == 0:
            print(f"[{i}", end=', ')
        else:
            print(colored(i, 'red'), end=', ')
    elif num == 0:
        print(f"[{i}", end=', ')
    elif num == (len(list_1) - 1):
        print(i, end='] ')
    else:
        print(i, end=', ')


