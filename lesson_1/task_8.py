year = int(input("Введите год для проверки: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} год високосный")
else:
    print(f"{year} год не високосный")
