s = "AbC12dE"
count = sum(1 for ch in s if 'A' <= ch <= 'Z')
print(count) 