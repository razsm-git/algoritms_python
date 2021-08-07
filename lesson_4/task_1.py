# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

from time import time


def revert_for(num):
    long = len(str(num))
    result = []
    while long != 0:
        result.append((str(num))[long-1])
        long -= 1
    return result


def revert_func(num):
    return ''.join(reversed(str(num)))


number = 454651556456609834564849413213218155555555555555555555555555555**128
start_time = time()
revert_for(number)
end_time = time()
first_var = f'Время выполнения первого варианта: {end_time - start_time}'
revert_func(number)
end_time_2 = time()
second_var = f'Время выполнения второго варианта: {end_time_2 - end_time}'
print(first_var, second_var)


# Видно, что время на выполнение первого варианта программы затрачено намного больше, чем на второй вариант.
# timeit не стал применять, так ка для функций считаю его не удобным. Но потренировался на
# других примерах в его применении.
