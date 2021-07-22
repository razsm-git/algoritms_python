# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

x1 = '4654894'
x2 = '50231954'
x3 = '0023157'
x4 = '433998012'
x5 = '1112555561'


def max_num(x):
    summs = 0
    for i in x:
        summs = summs + int(i)
    return summs


result = max(max_num(x1), max_num(x2), max_num(x3), max_num(x4), max_num(x5))
print(result)
