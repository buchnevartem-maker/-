# Begin23. Переместить A→B, B→C, C→A.
a = float(input())
b = float(input())
c = float(input())
temp = a
a = c
c = b
b = temp
print(a)
print(b)
print(c)
