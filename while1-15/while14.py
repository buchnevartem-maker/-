a = float(input())
s = 1.0  
k = 1
while s + 1 / (k + 1) < a:
    k += 1
    s += 1 / k
print(k, s)
