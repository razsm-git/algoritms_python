# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

x = 5
y = 4
list_1 = []

for str in range(1, y+1):
    var = input(f"Введите данные {str} строки матрицы через пробел: ").split()
    list_1.append(var)

column_min = []
for i in list_1:
    a = 0
    for j in i:
        j = int(j)
        print(f"{j:02}", end=' ')
        a += j
    print(' |', a)

# Поиск минимальных/максимальных элементов
col = 0
while col != x:
    temp_list = []
    for i in list_1:
        for num, j in enumerate(i):
            if num == col:
                temp_list.append(j)
    column_min.append(min(temp_list))
    col += 1
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {max(column_min)}")
