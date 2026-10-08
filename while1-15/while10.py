n = int(input())
p = 1
k = 0
while p * 3 < n:  
    p *= 3
    k += 1
print(k)
