M, N = map(int, input().split())
matrix = [[int(input()) for _ in range(N)] for _ in range(M)]
for j in range(0, N, 2):
    for i in range(M):
        print(matrix[i][j])