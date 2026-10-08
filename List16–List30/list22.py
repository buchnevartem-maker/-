A = list(map(int, input().split()))
D = int(input())

multiplied = (x * D for x in A)
count_eq_D = A.count(D)

print(*multiplied)
print(count_eq_D)