def shift_right3(a, b, c):
    return c, a, b 

for _ in range(2):
    a, b, c = map(int, input().split())
    print(*shift_right3(a, b, c))