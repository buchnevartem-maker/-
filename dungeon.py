# ================================================
# МОДУЛЬ DUNGEON
# Правила боя, покупки, цены и карточки врагов.
# Классы Hero и Enemy, сохранение через to_dict и from_dict.
# Выбор врага через random.choice остаётся в game.py.
# ================================================

import random

prices = {"зелье": 10, "масло": 15, "эликсир": 40}

enemy_stats = {
    "скелет":       {"hp": 45, "damage": 6, "loot": 25},
    "упырь":        {"hp": 30, "damage": 4, "loot": 15},
    "паук":         {"hp": 20, "damage": 3, "loot": 10},
    "летучая мышь": {"hp": 12, "damage": 2, "loot": 5},
}


class Hero:
    """Герой подземелья: характеристики, урон и методы трат."""

    def __init__(self, name, health, strength, agility, endurance):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.damage = 10 + strength * 1.5
        self.crit_damage = self.damage * 2
        self.stamina = health // 10 + endurance

    def __str__(self):
        return f"{self.name}: health {self.health}, damage {self.damage:.1f}, stamina {self.stamina}"

    def strike(self, n):
        if n % 3 == 0:
            return self.crit_damage, True
        return self.damage, False

    def spend_stamina(self, cost):
        if self.stamina >= cost:
            self.stamina -= cost
            return False
        self.health -= cost - self.stamina
        self.stamina = 0
        return True

    def heal(self, amount, cap):
        self.health = min(self.health + amount, cap)

    def to_dict(self):
        return {"name": self.name, "health": self.health,
                "stamina": self.stamina, "strength": self.strength,
                "agility": self.agility, "endurance": self.endurance}

    @staticmethod
    def from_dict(data):
        hero = Hero(data["name"], data["health"], data["strength"],
                    data["agility"], data["endurance"])
        hero.stamina = data["stamina"]
        return hero


class Enemy:
    """Враг, построенный из карточки словаря enemy_stats."""

    def __init__(self, name, stats):
        self.name = name
        self.hp = stats["hp"]
        self.damage = stats["damage"]
        self.loot = stats["loot"]


def fight(enemy, hero, bonus=0):
    """Бой с enemy до гибели одного из двоих.
    enemy — объект Enemy, hero — объект Hero.
    bonus — надбавка к урону героя.
    Печатает строки раундов.
    Возвращает (rounds, won, loot).
    """
    rounds = []
    round_n = 0
    print(f"Вы спускаетесь по ступеням. Из темноты появляется {enemy.name}!")
    while enemy.hp > 0 and hero.health > 0:
        round_n += 1
        hit, crit = hero.strike(round_n)
        hit += bonus
        enemy.hp -= hit
        line = f"Раунд {round_n}: вы наносите {hit:.1f} урона"
        if crit:
            line += " — критический!"
        if enemy.hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = enemy.damage
            hero.health -= blow
            line += f" Здоровье врага: {enemy.hp:.1f}. Враг бьёт в ответ на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy.hp <= 0
    if won:
        loot = enemy.loot
    else:
        loot = 0
    return rounds, won, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


if __name__ == "__main__":
    test_hero = Hero("Тест", 100, 7, 5, 4)
    test_enemy = Enemy("скелет", enemy_stats["скелет"])
    rounds, won, loot = fight(test_enemy, test_hero)
    print(f"self-test: {len(rounds)} rounds, won={won}, loot={loot}")