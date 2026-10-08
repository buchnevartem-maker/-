A = list(map(int, input().split()))
avg = sum(A) / len(A)

greater = [x for x in A if x > avg]
print(*greater)
print(len(greater))