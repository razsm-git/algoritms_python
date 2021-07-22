# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input("Введите число n: "))
sum = 1
start = 1
for i in range(n-1):
    result = start / -2
    sum = sum + result
    start = result

print(f"Сумма {n} элементов: {sum}")

