n = int(input())
d = {}
for i in range(n):
    k = input()
    v = input()
    d[k] = v

k = input()
if k in d:
    print(d[k])
else:
    print("нет такого ключа")