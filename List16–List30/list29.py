A = list(map(int, input().split()))
K = int(input())

top_k = sorted(A, reverse=True)[:K]
print(*top_k)