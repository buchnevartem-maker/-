A = list(map(int, input().split()))
D = int(input())

count = A.count(D)
try:
    idx = A.index(D)
except ValueError:
    idx = -1

print(count)
print(idx)