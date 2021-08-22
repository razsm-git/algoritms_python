# 4. Определить, какое число в массиве встречается чаще всего.
# Windows 10 x64 python 3.8
from sys import getsizeof
import numpy as np
list_1 = [69, 99, 9, 25, 15, 13, 96, 95, 18, 94, 22, 31, 64, 90, 23, 50, 87, 54, 74, 33, 18, 11, 62, 0, 42, 24, 57, 1, 18, 71] # 296


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return f"Число {k} встречается {v} раз(а)"


counts = {} # 1176
for i in list_1:
    var = list_1.count(i) # 28
    try:
        if var > counts[i]:
            counts[i] = var
    except KeyError:
        counts[i] = var
print(get_key(counts, max(counts.values())))

# Было выделено 1500 Байт памяти



# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

list_1 = [9, 2, 3, 1, 3, 8, 5, 4, 13, 7, 2, 12, 6, 6, 0, 4, 1, 11, 18, 19, 14, 10, 17, 15] # 248

min_1 = 0 # 24
min_2 = 0 # 28

while True:
    min_i = min(list_1) # 28
    count_i = list_1.count(min_i)
    if count_i > 1:
        min_1 = min_i
        min_2 = min_i
        break
    else:
        min_1 = min_i
        list_1.remove(min_i)
        min_i = min(list_1)
        min_2 = min_i
        break
print(f"В массиве {list_1} минимальные элементы: {min_1},{min_2}")

# Было выделено 328 Байт памяти