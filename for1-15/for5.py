price_per_kg = float(input("Цена за 1 кг: "))

for i in range(1, 11):         
    kg = i * 0.1               
    cost = price_per_kg * kg
    print(f"{kg:.1f} кг: {cost}")