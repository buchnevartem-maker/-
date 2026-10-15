n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    d[name] = [price, qty]

total = 0
best_name = None
best_cost = None
for name in d:
    cost = d[name][0] * d[name][1]
    total += cost
    if best_cost is None or cost > best_cost:
        best_cost = cost
        best_name = name

print(total)
print(best_name)