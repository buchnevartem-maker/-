def rect_ps(x1, y1, x2, y2):
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    return 2 * (w + h), w * h

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    p, s = rect_ps(x1, y1, x2, y2)
    print(p, s)