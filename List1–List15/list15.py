A = list(map(int, input().split()))

selected = A[::2]          
print(sum(selected))