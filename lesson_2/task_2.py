# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# P.S. ноль входит в ряд натуральных чисел и является чётным.

number = input("Введите натуральное число: ")
even_num = 0
not_even_num = 0
for i in number:
    try:
        number = int(number)
        if int(i) % 2 == 0:
            even_num += 1
        else:
            not_even_num += 1
    except (TypeError, ValueError):
        print("Вы ввели не число!")
        break
print(f"Кол-во чётных чисел: {even_num}, кол-во не чётных чисел: {not_even_num}")