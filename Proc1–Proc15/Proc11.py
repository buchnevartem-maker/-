def minmax(x, y):
    return (x, y) if x < y else (y, x)

A, B, C, D = map(int, input().split())

mn1, mx1 = minmax(A, B)
mn2, mx2 = minmax(C, D)
overall_min, _ = minmax(mn1, mn2)
_, overall_max = minmax(mx1, mx2)

print(overall_min, overall_max)