price_per_kg = float(input("Цена за 1 кг: "))

for kg in range(1, 11):
    cost = price_per_kg * kg
    print(f"{kg} кг: {cost}")