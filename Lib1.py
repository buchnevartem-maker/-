import dungeon
hp, won = dungeon.fight("skeleton", 100)
gold = dungeon.buy(dungeon.prices["potion"], 100)
print(dungeon.prices)