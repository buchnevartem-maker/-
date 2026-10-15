n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

v = int(input())

to_delete = []
for k in d:
    if d[k] < v:
        to_delete.append(k)

for k in to_delete:
    del d[k]

print(len(d))