# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
letters = ''
counts = 0
x = 10

for i in range(32, 128):
    add = f"{i} - {chr(i)}; "
    if counts < x:
        letters += add
        counts += 1
    else:
        print(letters)
        letters = add
        counts = 0
        x = 9
print(letters)
