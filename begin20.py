# Begin20 (СЛОЖНОЕ). Найти расстояние между двумя точками
# (x1, y1) и (x2, y2) на плоскости: sqrt((x2−x1)² + (y2−y1)²).
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)
