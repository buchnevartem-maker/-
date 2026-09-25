# Begin18 (СЛОЖНОЕ). Даны три точки A, B, C на числовой оси.
# Точка C расположена между A и B. Найти произведение длин отрезков AC и BC.
a = float(input())
b = float(input())
c = float(input())
ac = c - a
bc = b - c
print(ac * bc)
