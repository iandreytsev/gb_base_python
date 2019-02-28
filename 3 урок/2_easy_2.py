# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# способ №1. С помощью цикла while

list1 = ["яблоко", "банан", "киви", 2, 56, "оружие", "обучение", "удалить", "яблоко"]
list2 = ["яблоко", "киви", 2, "оружие", "секрет", "самосознание", "удалить"]

i = 0
while i < len(list1):
    if list1[i] in list2:
        list1.pop(i)
    else:
        i += 1
print(list1)

input("\nНажмите enter, чтобы перейти ко второму способу\n")

# способ №2. С помощью цикла for in

list1 = ["яблоко", "банан", "киви", 2, 56, "оружие", "обучение", "удалить", "яблоко"]
list2 = ["яблоко", "киви", 2, "оружие", "секрет", "самосознание", "удалить"]
copy_list1 = list1[:]

for element in copy_list1:
    if element in list2:
        list1.remove(element)

print(list1)

input("\nНажмите enter, чтобы выйти")



