# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

from numpy import mean
num = int(input("Введите кол-во предприятий: "))
org = {}
for i in range(num):
    name = input("Введите имя организации: ")
    profit_1 = int(input("Прибыль за первый квартал: "))
    profit_2 = int(input("Прибыль за второй квартал: "))
    profit_3 = int(input("Прибыль за третий квартал: "))
    profit_4 = int(input("Прибыль за четвёртый квартал: "))
    org[name] = profit_1 + profit_2 + profit_3 + profit_4
average_profit = round(mean(list(org.values())), 2)
print(f"Средняя годовая прибыль всех предприятий: {average_profit}")

for key, val in org.items():
    if val > average_profit:
        print(f"Прибыль организации {key} выше средней за год.")
    elif val == average_profit:
        print(f"Прибыль организации {key} равна средней за год.")
print('-' * 40)
for key, val in org.items():
    if val < average_profit:
        print(f"Прибыль организации {key} меньше средней за год.")
