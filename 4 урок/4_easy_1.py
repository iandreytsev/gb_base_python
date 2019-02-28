import random
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1_g = [random.randint(-20, 20) for _ in range(10)]
list2_g = [el ** 2 for el in list1_g]

print(f"\nДан список: {list1_g} ")
print(f"\nВозведем каждый элемент данного списка в квадрат: {list2_g}")


