# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list1 = [1, 4, 6, 3, 5, 10, 66, 16, 28, 31, 7, 9]
new_list = []

for element in list1:
    if element % 2 == 0:
        new_element = element / 4
    else:
        new_element = element * 2

    new_list.append(new_element)

print(new_list)

input("Нажмите enter, чтобы продолжить")


