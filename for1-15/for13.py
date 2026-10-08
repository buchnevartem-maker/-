N = int(input("Введите N: "))

result = 0.0
for i in range(1, N + 1):
    value = 1.0 + i * 0.1   
    if i % 2 == 1:            
        result += value
    else:                      
        result -= value

print("Результат:", result)