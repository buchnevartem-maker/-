s = input()
idx = int(input())

try:
    print(s[idx])
except IndexError:
    print("Нет такого символа")