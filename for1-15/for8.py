A = int(input("Введите A: "))
B = int(input("Введите B: "))

product = 1
for x in range(A, B + 1):
    product *= x

print("Произведение:", product)