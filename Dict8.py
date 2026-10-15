n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

v = int(input())
found = False
for value in d.values():
    if value == v:
        found = True
print(found)