# Begin12 (СЛОЖНОЕ). Даны катеты прямоугольного треугольника a и b.
# Найти гипотенузу c = sqrt(a² + b²) и периметр P = a + b + c.
a = float(input())
b = float(input())
c = (a ** 2 + b ** 2) ** 0.5
perimeter = a + b + c
print(c)
print(perimeter)
