# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import deque

first = input('Введите первое число: ')
second = input('Введите второе число: ')
list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


def sum_numbers(x, y):
    if len(x) > len(y):
        x, y = y, x
    y = y[::-1]
    third = []
    j = -1
    k = 0
    for i in y:
        one = list_of_numbers.index(i)
        two = list_of_numbers.index(x[j])
        third.append(list_of_numbers[(one + two + k) % 16])
        if (one + two) >= 15:
            k = 1
        else:
            k = 0
        j -= 1
        if j == -len(x) - 1:
            break

    diff = len(y) - len(x)

    if diff:
        for _ in y[-diff:]:
            third.append(list_of_numbers[(list_of_numbers.index(y[-diff]) + k) % 16])
            if list_of_numbers.index(y[-diff]) + 1 >= 15:
                k = 1
            else:
                k = 0
        if k == 1:
            third.append('1')

    return third[::-1]


def mul_numbers(x, y):
    x_decimal = 0
    y_decimal = 0
    result = deque()
    len_x = len(x)
    for i in range(len_x):
        x_decimal += list_of_numbers.index(x[len_x - i - 1]) * (16 ** i)

    len_y = len(y)

    for i in range(len_y):
        y_decimal += list_of_numbers.index(y[len_y - i - 1]) * (16 ** i)

    result_decimal = x_decimal * y_decimal
    while result_decimal != 0:
        var = result_decimal % 16
        result_decimal = result_decimal // 16
        result.appendleft(list_of_numbers[var])

    return list(result)


print(f"Сумма чисел {first} и {second} = {sum_numbers(first,second)}")
print(f"Произведение чисел {first} и {second} = {mul_numbers(first,second)}")
