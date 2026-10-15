n = int(input())
d = {}
for i in range(n):
    k = input()
    v = input()
    d[k] = v

k = input()
print(d.get(k, 0))