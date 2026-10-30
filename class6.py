class Inventory:
    def __init__(self):
        self.items = {}
    def add(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty
    def total(self):
        return sum(self.items.values())

inv = Inventory()
inv.add("potion", 2)
inv.add("oil", 3)
inv.add("potion", 1)
print(inv.total())