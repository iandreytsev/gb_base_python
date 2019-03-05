import math


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        # вычисляем стороны треугольника (находим длинну векторов)
        self.ab = round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)
        self.bc = round(math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)), 2)
        self.ac = round(math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2)), 2)

    def perimeter(self):
        p = self.ab + self.bc + self.ac
        return round(p, 2)

    def square(self):
        half_p = self.perimeter() / 2  # находим полупериметр
        # для нахождения площадь используем формулу Герона
        s = math.sqrt(half_p * (half_p - self.ab) * (half_p - self.bc) * (half_p - self.ac))
        return round(s, 2)

    def height(self):
        h = 2 * self.square() / self.ac
        return round(h, 2)


# получаем координаты точек от пользователя
ax = int(input("Введите x для точки А: "))
ay = int(input("Введите y для точки A: "))
bx = int(input("Введите x для точки B: "))
by = int(input("Введите y для точки B: "))
cx = int(input("Введите x для точки С: "))
cy = int(input("Введите y для точки С: "))

print(f"""
Координаты точки А: {ax, ay}
Координаты точки B: {bx, by}
Координаты точки C: {cx, cy}
""")

figure = Triangle(ax, ay, bx, by, cx, cy)

print(f"Периметр треугольника  ABC = {figure.perimeter()}")
print(f"Площадь треугольника  ABC = {figure.square()}")
print(f"Высота треугольника ABC = {figure.height()}")
