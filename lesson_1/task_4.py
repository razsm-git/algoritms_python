# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.

import random


def is_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


print(
    "Введите границы для генерирования случайного целого числа, случайного вещественного числа или случайного символа: ")
x1 = input("Нижняя граница диапозона: ")
x2 = input("Верхняя граница диапозона: ")
list1 = [x1, x2]
result = None

if list1[0].isdigit() and list1[1].isdigit():
    temp = list(map(int, list1))
    result = random.randint(temp[0], temp[1])
elif is_float(list1[0]) and is_float(list1[1]):
    temp = list(map(float, list1))
    result = round(random.uniform(temp[0], temp[1]), 2)
elif list1[0].isalpha() and list1[1].isalpha():
    var = list(map(ord, list1))
    result = chr(int(random.random() * (var[1] - var[0] + 1) + var[0]))

print(f"Результат: {result}")
