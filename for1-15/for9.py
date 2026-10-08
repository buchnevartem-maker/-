A = int(input("Введите A: "))
B = int(input("Введите B: "))

sum_sq = 0
for x in range(A, B + 1):
    sum_sq += x * x

print("Сумма квадратов:", sum_sq)