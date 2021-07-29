# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import numpy as np

list_1 = list(np.random.permutation(np.arange(-100, 20))[:20])

print(list_1)
min_i = min(list_1)
print(f'Максимально отрицательное число {min_i} находится под индексом {list_1.index(min_i)}.')
