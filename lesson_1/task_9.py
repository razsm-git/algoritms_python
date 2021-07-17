# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

x1 = int(input("Первое число: "))
x2 = int(input("Второе число: "))
x3 = int(input("Третье число: "))
list1 = [x1, x2, x3]
list2 = [min(list1), max(list1)]
result = None
if x1 not in list2:
    result = x1
elif x2 not in list2:
    result = x2
else:
    result = x3
print(result)
