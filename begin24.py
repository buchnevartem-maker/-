# Begin24. Переместить A→C, C→B, B→A.
a = float(input())
b = float(input())
c = float(input())
temp = a
a = b
b = c
c = temp
print(a)
print(b)
print(c)
