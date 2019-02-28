import random
import re

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

my_file = open("normal3.txt", "w", encoding="utf-8")
print("\nФайл успешно открыт")

random_digits = ""
for _ in range(2501):
    random_digits += str(random.randint(0, 10))

my_file.write(random_digits)
my_file.close()

print("\n2500-значное число успешно записано в файл.")

my_file = open("normal3.txt", "r", encoding="utf-8")

line = my_file.read()
my_file.close()

result = re.findall(r"[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+", line)

longest_seq = []
# максимальное значение k = длинне строки. Например, если бы строка состояла только из 1111
for k in range(0, len(line) + 1):
    # ищем самую длинную последовательность цифр в списке result и добавляем в longest_seq
    longest_seq = [el for el in result if len(el) > k] #
    # если она есть, ищем дальше
    if longest_seq:
        continue
    # если ее нет, в предыдущей итерации мы нашли максимальную последовательность одинаковых цифр
    else:
        longest_seq = [el for el in result if len(el) > k - 1]
        break

longest_seq = list(set(longest_seq)) # избавляемся от дубликатов

print(f"\nСамая длинная последовательность одинаковых цифр в 2500-значном числе:\n{longest_seq}")
