a_str = input()
b_str = input()

try:
    a = int(a_str)
    b = int(b_str)
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")