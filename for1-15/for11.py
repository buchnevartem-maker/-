N = int(input("Введите N: "))

total = 0
for k in range(N, 2 * N + 1):
    total += k * k

print("Результат:", total)