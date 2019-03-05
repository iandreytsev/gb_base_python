import math


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.ab = round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)
        self.bc = round(math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)), 2)
        self.cd = round(math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2)), 2)
        self.da = round(math.sqrt(((x4 - x1) ** 2) + ((y4 - y1) ** 2)), 2)
        self.ac = round(math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2)), 2)  # диагональ трапеции
        self.bd = round(math.sqrt(((x4 - x2) ** 2) + ((y4 - y2) ** 2)), 2)  # диагональ трапеции

    def perimeter(self):
        p = self.ab + self.bc + self.cd + self.da
        return round(p, 2)

    def height(self):
        # находим высоту по формуле 4х сторон
        h = math.sqrt(self.ab ** 2 - (
                (((self.da - self.bc) ** 2) + self.ab ** 2 - self.cd ** 2) / (2 * (self.da - self.bc))) ** 2)
        return round(h, 2)

    def square(self):
        s = (self.bc + self.da) / 2 * self.height()
        return round(s, 2)

    def equality_check(self):
        if self.ac == self.bd:
            return "Трапеция ABCD является равнобокой"
        else:
            return "Трапеция ABCD не является равнобокой"


# получаем координаты точек от пользователя
print("\nДля трапеции ABCD")
ax = int(input("Введите x для точки А: "))
ay = int(input("Введите y для точки A: "))
bx = int(input("Введите x для точки B: "))
by = int(input("Введите y для точки B: "))
cx = int(input("Введите x для точки С: "))
cy = int(input("Введите y для точки С: "))
dx = int(input("Введите x для точки D: "))
dy = int(input("Введите y для точки D: "))

print(f"""
Координаты точки А: {ax, ay}
Координаты точки B: {bx, by}
Координаты точки C: {cx, cy}
Координаты точки D: {dx, dy}
""")

figure = Trapeze(ax, ay, bx, by, cx, cy, dx, dy)

print(figure.equality_check())
print(f"Периметр трапеции  ABCВ = {figure.perimeter()}")
print(f"Площадь трапеции ABCD = {figure.square()}")
print(f"Высота трапеции ABCD = {figure.height()}")
