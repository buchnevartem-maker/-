# Begin19 (СЛОЖНОЕ). Даны координаты двух противоположных вершин
# прямоугольника (x1, y1), (x2, y2). Стороны параллельны осям.
# Найти периметр и площадь.
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
width = abs(x2 - x1)
height = abs(y2 - y1)
perimeter = 2 * (width + height)
area = width * height
print(perimeter)
print(area)
