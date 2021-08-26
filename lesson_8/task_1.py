# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

my_str = 'python algorithms'
search = 'th'

sha_obj = hashlib.sha256(search.encode('utf8')).hexdigest()
print(f'Source hash: {sha_obj}')

for i in range(len(my_str) - len(search) + 1):
    current_sha = hashlib.sha256(my_str[i:len(search) + i].encode('utf8')).hexdigest()
    if sha_obj == current_sha:
        print(f"Match. String {search} - hash {current_sha}")
