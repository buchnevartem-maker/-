A = float(input("Введите A: "))
N = int(input("Введите N: "))

power = 1.0
for _ in range(N):
    power *= A

print("A^N:", power)