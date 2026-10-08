A = list(map(int, input().split()))

positives = (x for x in A if x > 0)
pos_list = list(positives)

print(*pos_list)
print(len(pos_list))