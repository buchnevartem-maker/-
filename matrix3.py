M, N = map(int, input().split())
nums = [int(input()) for _ in range(M)]
matrix = [[nums[i] for _ in range(N)] for i in range(M)]
for row in matrix:
    print(*row)