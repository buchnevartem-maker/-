M, N = map(int, input().split())
D = int(input())
nums = [int(input()) for _ in range(M)]
matrix = [[nums[i] + j * D for j in range(N)] for i in range(M)]
for row in matrix:
    print(*row)