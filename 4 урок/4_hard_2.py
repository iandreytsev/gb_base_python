import re
import random

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:


number = ""
for _ in range(1001):
    number += str(random.randint(0, 10))

result = re.findall(r"\d{5}", number)

result = list(set(result))  # избавляеся от дубликатов

multiply_seq = []
# достаем из списка послед из 5 цифр, и перемножаем их друг с другом
for seq in result:
    multiply = int(seq[0]) * int(seq[1]) * int(seq[2]) * int(seq[3]) * int(seq[4])
    multiply_seq.append(multiply)  # добавляем их в новый список с уже полученными произведениями

# находим наибольшее из них
max_multiply_seq = max(multiply_seq)

print(f"\nНаибольшая последовательность из 5 цифр в 1000-значном числе равна: {max_multiply_seq}")
