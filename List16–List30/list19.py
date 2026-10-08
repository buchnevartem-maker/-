strings = input().split()

sorted_by_len = sorted(strings, key=len)
longest = max(strings, key=len)

print(*sorted_by_len)
print(longest)