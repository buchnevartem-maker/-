price_per_kg = float(input("Цена за 1 кг: "))
start = 1.2
step = 0.2

i = 0
while True:
    kg = start + i * step
    if kg > 2.0 + 1e-9:     
        break
    cost = price_per_kg * kg
    print(f"{kg:.1f} кг: {cost}")
    i += 1
