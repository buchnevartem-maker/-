def sort_dec3(a, b, c):
    return tuple(sorted((a, b, c), reverse=True))

for _ in range(2):
    a, b, c = map(int, input().split())
    print(*sort_dec3(a, b, c))
