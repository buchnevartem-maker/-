M, N = map(int, input().split())
matrix = [[5 * j for j in range(1, N + 1)] for _ in range(M)]
for row in matrix:
    print(*row)