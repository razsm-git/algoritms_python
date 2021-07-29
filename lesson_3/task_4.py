# 4. Определить, какое число в массиве встречается чаще всего.

import numpy as np
list_1 = [69, 99, 9, 25, 15, 13, 96, 95, 18, 94, 22, 31, 64, 90, 23, 50, 87, 54, 74, 33, 18, 11, 62, 0, 42, 24, 57, 1, 18, 71]


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return f"Число {k} встречается {v} раз(а)"


counts = {}
for i in list_1:
    var = list_1.count(i)
    try:
        if var > counts[i]:
            counts[i] = var
    except KeyError:
        counts[i] = var
print(get_key(counts, max(counts.values())))
