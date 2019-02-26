# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков
# Выполнить поворот (транспонирование) матрицы

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# 1 способ:
r_matrix1 = [list(el) for el in zip(*matrix)]

# 2 cпособ:
r_matrix2 = list(map(list, zip(*matrix)))

print(f"\nПервый способ: {r_matrix1}")
print(f"\nВторой способ: {r_matrix2}")
