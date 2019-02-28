# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """Сортирует принимаемый список по возврастанию"""
    n = len(origin_list)
    for iteration in range(0, n - 1):
        # -1, чтобы не получить ошибку out of range, - iteratiоn, чтобы не доходить до
        for i in range(0, n - 1 - iteration):
            if origin_list[i] <= origin_list[i + 1]:
                continue
            else:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]

    print(origin_list)


list1 = [88, 14, -234, 0, 23423, -131, 6, 1, 0]
sort_to_max(list1)
