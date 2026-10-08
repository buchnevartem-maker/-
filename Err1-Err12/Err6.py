s = input()
idx_str = input()

try:
    idx = int(idx_str)
    print(s[idx])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")