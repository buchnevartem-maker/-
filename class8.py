class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def to_dict(self):
        return {"name": self.name, "health": self.health, "damage": self.damage}
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["health"], data["damage"])

h = Hero("Anya", 100, 15)
data = h.to_dict()
h2 = Hero.from_dict(data)
print(h2.health)