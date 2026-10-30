M, N = map(int, input().split())
Q = int(input())
nums = [int(input()) for _ in range(N)]
matrix = [[nums[j] * (Q ** i) for j in range(N)] for i in range(M)]
for row in matrix:
    print(*row)