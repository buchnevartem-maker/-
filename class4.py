class Potion:
    def __init__(self, name, price, heal):
        self.name = name
        self.price = price
        self.heal = heal
    def describe(self):
        return f"{self.name}: {self.price} gold, +{self.heal} health"

p = Potion("Small potion", 10, 10)
print(p.describe())