def shift_left3(a, b, c):
    return b, c, a

for _ in range(2):
    a, b, c = map(int, input().split())
    print(*shift_left3(a, b, c))