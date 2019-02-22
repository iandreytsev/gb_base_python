import math


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def vector_len(an, am):
    v_len = math.sqrt((am[0] - an[0]) ** 2 + (am[1] - an[1]) ** 2)
    return v_len


def enter_coord():
    ax = int(input("Введите x для точки А: "))
    ay = int(input("Введите y для точки A: "))
    bx = int(input("Введите x для точки B: "))
    by = int(input("Введите y для точки B: "))
    cx = int(input("Введите x для точки С: "))
    cy = int(input("Введите y для точки С: "))
    dx = int(input("Введите x для точки D: "))
    dy = int(input("Введите y для точки D: "))

    a = [ax, ay]
    b = [bx, by]
    c = [cx, cy]
    d = [dx, dy]

    return a, b, c, d


cords = enter_coord()

a = cords[0]
b = cords[1]
c = cords[2]
d = cords[3]

print(f"\nТочка А = {a}\nТочка B = {b}\nТочка С = {c}\nТочка D = {d}\n")

breakpoint

ab = vector_len(a, b)
ac = vector_len(a, c)
ad = vector_len(a, d)
ba = vector_len(b, a)
bd = vector_len(b, d)
bc = vector_len(b, c)
cd = vector_len(c, d)

if ab == cd and bc == ad:
    print("\nТочки являются вершинами параллелограмма")

elif bc == ad and bd == ac:
    print("\nТочки являются вершинами параллелограмма")

else:
    print("\nТочки не являются вершинами параллелограмма")

