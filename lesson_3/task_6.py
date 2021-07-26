# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import numpy as np


def list_sum(list):
    summary = 0
    for i in list:
        summary += i
    return summary


list_1 = list(np.random.permutation(np.arange(-5, 20))[:30])
print(list_1)
min_i = min(list_1)
max_i = max(list_1)
if list_1.index(min_i) < list_1.index(max_i):
    list_1 = list_1[(list_1.index(min_i)) + 1:list_1.index(max_i)]
    print(f"Минимальный элемент: {min_i}, максимальный элемент: {max_i}")
    print(f"Элементы между: {list_1}")
    print(f'Сумма элементов между минимальным и максимальным значениями: {list_sum(list_1)}')
else:
    list_1 = list_1[(list_1.index(max_i)) + 1:list_1.index(min_i)]
    print(f"Минимальный элемент: {min_i}, максимальный элемент: {max_i}")
    print(f"Элементы между: {list_1}")
    print(f'Сумма элементов между максимальным и минимальным значениями: {list_sum(list_1)}')