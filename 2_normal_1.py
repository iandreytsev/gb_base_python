import math
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list1 = [2, -5, 8, 9, -25, 25, 4, 16, 81, 0]
new_list = []


for element in list1:
    if element >= 0:
        new_element = math.sqrt(element)
        if new_element.is_integer():
            new_list.append(int(new_element))

print(new_list)

input("Нажмите enter, чтобы продолжить")







