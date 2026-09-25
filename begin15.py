# Begin15 (СЛОЖНОЕ). Дана площадь S круга.
# Найти диаметр D и длину L: R = sqrt(S/π), D = 2·R, L = 2·π·R. π = 3.14.
s = float(input())
pi = 3.14
r = (s / pi) ** 0.5
d = 2 * r
l = 2 * pi * r
print(d)
print(l)
