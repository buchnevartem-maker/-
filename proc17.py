def roots_count(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        return 2
    if d == 0:
        return 1
    return 0

for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())
    print(roots_count(a, b, c))