import random

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

my_list = []
n = None

# сделаем так, чтобы компьютер принимал ввод только целого положительного числа
while True:
    n = input("Cколько случайных элементов вы хотите добавить в список?: ")
    if n.isdigit():  # проверка на то, что в ввденной строке присутствуют только цифры.
        n = int(n)
        break
    else:
        print("Введите положительное целое число")

for i in range(n):
    my_list.append(random.randint(-100, 100))

print("Вывожу новый список:", my_list)

input("\nНажмите enter, чтобы продолжить")

