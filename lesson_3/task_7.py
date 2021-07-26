# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

list_1 = [9, 2, 3, 1, 3, 8, 5, 4, 13, 7, 2, 12, 6, 6, 0, 4, 1, 11, 18, 19, 14, 10, 17, 15]

min_1 = 0
min_2 = 0

while True:
    min_i = min(list_1)
    count_i = list_1.count(min_i)
    if count_i > 1:
        min_1 = min_i
        min_2 = min_i
        break
    else:
        min_1 = min_i
        list_1.remove(min_i)
        min_i = min(list_1)
        min_2 = min_i
        break
print(f"В массиве {list_1} минимальные элементы: {min_1},{min_2}")
