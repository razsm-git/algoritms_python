import math
from time import time


def without_eratosthenes(n):
    list_1 = [2]
    count = 1
    number = 3
    while count < n:
        a = True
        for x in list_1:
            if number % x == 0:
                a = False
                break
        if a:
            count += 1
            list_1.append(number)
        number += 1
    return list_1[-1]

# Сложность квадратичная O(n**n)


start_1 = time()
print(without_eratosthenes(10000))
end_1 = time()
print(f'Затрачено без Эратосфена: {end_1 - start_1}')


def with_eratosthenes(i):
    i_max = count_func(i)
    list_1 = [_ for _ in range(2, i_max)]
    len_list = len(list_1)
    for number in list_1:
        if number != 0:
            for j in range(number, len_list, number):
                list_1[j] = 0
    result = [x for x in list_1 if x != 0]
    return result[-1]


def count_func(i):
    counts = 0
    current_num = i
    while counts <= i:
        counts = current_num / math.log(current_num)
        current_num += 1
    return current_num

# Сложность логарифмическая O(n*log(n))

start_2 = time()
print(with_eratosthenes(10000))
end_2 = time()
print(f'Затрачено c Эратосфеном: {end_2 - start_2}')

# Опытным путём удалось выяснить, что с Эратосфеном времени на исполнение кода уходит меньше
