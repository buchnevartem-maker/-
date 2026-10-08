A = list(map(int, input().split()))
avg = sum(A) / len(A)

greater_than_avg = (x for x in A if x > avg)

print(*greater_than_avg)
print(avg)