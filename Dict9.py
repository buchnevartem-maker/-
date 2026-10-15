n = int(input())
d1 = {}
for i in range(n):
    k = input()
    v = input()
    d1[k] = v

m = int(input())
d2 = {}
for i in range(m):
    k = input()
    v = input()
    d2[k] = v

common = None
for k in d2:
    if k in d1:
        common = k
        break

d1.update(d2)
print(len(d1))
print(d1[common])