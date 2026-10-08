strings = input().split()

lengths = (len(s) for s in strings)
lengths_list = list(lengths)
total_len = sum(lengths_list)

print(*lengths_list)
print(total_len)