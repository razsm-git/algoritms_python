#  2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
#  Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

n1 = 5
n2 = 6

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2
bit_left = n1 << 2
bit_right = n1 >> 2

print(f"OR: {bit_or}")
print(f"AND: {bit_and}")
print(f"XOR: {bit_xor}")
print(f"bit_left for {n1}: {bit_left}")
print(f"bit_right for {n1}: {bit_right}")

