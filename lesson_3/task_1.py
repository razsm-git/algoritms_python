# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

numbers = list(range(2, 100, 1))
condition = list(range(2, 10, 1))
count_num = {}
for i in numbers:
    for j in condition:
        if i % j == 0:
            try:
                count_num[j] += 1
            except KeyError:
                count_num[j] = 1
print(count_num)
