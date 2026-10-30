# ================================================
# МОДУЛЬ DUNGEON
# Правила боя, покупки, цены и карточки врагов.
# Выбор врага через random.choice остаётся в game.py.
# random импортируется здесь только для самотеста.
# ================================================

import random

prices = {"зелье": 10, "масло": 15, "эликсир": 40}

enemy_stats = {
    "скелет":       {"hp": 45, "damage": 6, "loot": 25},
    "упырь":        {"hp": 30, "damage": 4, "loot": 15},
    "паук":         {"hp": 20, "damage": 3, "loot": 10},
    "летучая мышь": {"hp": 12, "damage": 2, "loot": 5},
}


def hero_hit(strike_n, damage, crit_damage):
    """Урон героя в удар strike_n; возвращает пару (hit, crit).
    damage и crit_damage приходят параметрами.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus, damage, crit_damage):
    """Бой с enemy до гибели одного из двоих.
    Карточка врага берётся из enemy_stats по имени: нужны ключи
    hp, damage, loot. bonus — надбавка к урону героя.
    damage и crit_damage — правила урона героя.
    Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot).
    """
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    print(f"Вы спускаетесь по ступеням. Из темноты появляется {enemy}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n, damage + bonus, (damage + bonus) * 2)
        enemy_hp -= hit
        line = f"Раунд {round_n}: вы наносите {hit:.1f} урона"
        if crit:
            line += " — критический!"
        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = stats["damage"]
            hero_health -= blow
            line += f" Здоровье врага: {enemy_hp:.1f}. Враг бьёт в ответ на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy_hp <= 0
    if won:
        loot = stats["loot"]
    else:
        loot = 0
    return rounds, won, hero_health, loot


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
    rounds, won, hp, loot = fight("скелет", 100, 0, 20.5, 41.0)
    print(f"self-test: {len(rounds)} rounds, won={won}, loot={loot}")