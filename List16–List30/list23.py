A = list(map(int, input().split()))

result = sorted(A, key=abs, reverse=True)
print(*result)