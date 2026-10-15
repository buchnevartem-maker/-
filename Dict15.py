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

ignored = 0
for k in d2:
    if k in d1:
        ignored += 1
    else:
        d1[k] = d2[k]

print(len(d1))
print(ignored)