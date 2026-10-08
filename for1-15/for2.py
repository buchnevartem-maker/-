A = int(input("Введите A: "))
B = int(input("Введите B: "))

numbers = list(range(A, B + 1))
for x in numbers:
    print(x)

N = len(numbers)
print("Количество чисел:", N)