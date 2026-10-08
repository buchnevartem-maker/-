age_str = input()
try:
    age = int(age_str)
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
    print(f"Принято: {age}")
except ValueError as e:
    print(f"Отклонено: {e}")