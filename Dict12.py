n = int(input())
d = {}
for i in range(n):
    k = input()
    v = input()
    d[k] = v

rev = {}
for k in d:
    rev[d[k]] = k

for value in rev:
    print(value, rev[value])