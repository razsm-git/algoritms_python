from random import randint

list_nums = [randint(0, 100) for _ in range(31)]
print(f"Изначальный список: {list_nums}")

for i in list_nums:
    min_count = 0
    max_count = 0
    for j in list_nums:
        if i > j:
            min_count += 1
        if i < j:
            max_count += 1
    if min_count == max_count:
        print(f"Медиана найдена: {i}")
