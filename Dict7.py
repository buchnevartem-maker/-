n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

best_key = None
best_val = None
for k in d:
    if best_val is None or d[k] > best_val:
        best_key = k
        best_val = d[k]
print(best_key)