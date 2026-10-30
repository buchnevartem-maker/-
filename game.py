# ================================================
# ИГРА ЗАБРОШЕННАЯ ШАХТА
# Автор: Артем Бучнев
# Дата:  октябрь 2026
# Этап 15: Файлы и JSON. Выход и прерывание сохраняют
# забег в save.json, следующий запуск спрашивает,
# продолжить ли. Гибель стирает сохранение.
# Решение: при продолжении формуляр не перепечатывается,
# состояние показывает строка статуса после первого действия.
# Решение: random.choice остаётся в game.py, dungeon.py
# импортирует random только для самотеста.
# Решение: боевой эликсир копит надбавку до конца забега,
# каждая покупка добавляет +2 к урону за штуку.
# Решение: bonus прибавляется к обычному урону до удвоения
# критом — критический удар с эликсиром бьёт вдвое сильнее.
# Решение: при равных ударах врага max берёт первый
# из равных — устойчивость сортировки, осознанный выбор.
# ================================================

import random
import os
import json
import dungeon

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

title = "ЗАБРОШЕННАЯ ШАХТА"
frame = "=" * (len(title) + 6)
print(frame)
print(f"   {title}   ")
print(frame)
print()

loaded = None
if os.path.exists("save.json"):
    print("Найдено сохранение. Продолжить забег? (да/нет)")
    answer = input().strip().lower()
    if answer in ("да", "yes", "д"):
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Сохранение повреждено. Начинаем новый забег.")
            loaded = None

if loaded is None:
    
    print("Как зовут героя?")
    hero_name = input()
    print(f"Добро пожаловать, {hero_name}!")
    print("Ты стоишь у входа в заброшенную шахту. Оттуда тянет могильным холодом и угольной пылью.")
    print()

    print("Настройка героя.")
    print("Здоровье, сила, ловкость, удача — по одному числу в строке:")
    while True:
        try:
            health = int(input())
            strength = int(input())
            agility = int(input())
            luck = int(input())
            if health <= 0:
                raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
            if strength < 0 or agility < 0 or luck < 0:
                raise ValueError("Сила, ловкость и удача не могут быть отрицательными")
            if agility > strength + 10:
                raise ValueError("Ловкость не может превышать силу более чем на 10")
            break
        except ValueError as e:
            print(f"{e}. Введите все четыре числа снова:")
    print()

    base_attack = 10
    damage = base_attack + strength * 1.5
    crit_damage = damage * 2
    stamina = (health // 10) + luck

    max_health = health
    max_stamina = stamina

    print("Характеристики героя:")
    print(f"Здоровье: {health}")
    print(f"Сила:     {strength}")
    print(f"Ловкость: {agility}")
    print(f"Удача:    {luck}")
    print()
    print(f"Урон героя:       {damage:.1f}")
    print(f"Критический урон: {crit_damage:.1f}")
    print(f"Запас сил:        {stamina}")
    print()

    enemies = ["упырь", "скелет", "паук", "летучая мышь"]
    log = []
    gold_total = 0
    ability_bonus = 0
    inventory = {}

    MAP = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", "#", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", "#", "S", ".", "#"],
    ]
    hero_r, hero_c = 4, 2
    visited = {(4, 2)}
    LOOT = {(1, 1): "старая монета", (2, 3): "пыльное зелье", (3, 3): "самоцвет стража"}
    found_loot = set()
    actions = 0
else:
   
    hero_name = loaded["hero"]
    health = loaded["health"]
    stamina = loaded["stamina"]
    gold_total = loaded["gold"]
    actions = loaded["actions"]
    enemies = loaded["enemies"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    inventory = loaded.get("inventory", {})
    ability_bonus = loaded.get("ability_bonus", 0)
    log = loaded.get("log", [])
    damage = loaded["damage"]
    crit_damage = loaded["crit_damage"]
    max_health = loaded["max_health"]
    max_stamina = loaded["max_stamina"]
    MAP = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", "#", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", "#", "S", ".", "#"],
    ]
    LOOT = {(1, 1): "старая монета", (2, 3): "пыльное зелье", (3, 3): "самоцвет стража"}
    print(f"Забег продолжен: здоровье {health}, золото {gold_total}, "
          f"врагов осталось {len(enemies)}.")
    print()

DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}

num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "listen",
               "5": "torch", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "drink", "0": "exit"}

commands = ["look", "go <direction>", "rest", "listen", "torch", "train",
            "descend", "leaders", "shop", "backpack", "drink potion",
            "buy <item> [count]", "map", "scout", "newgame", "help", "exit"]

MENU = ["Что делаешь? (номер или команда; help — справка)",
        "1 - осмотреться (look)",
        "2 - идти вперёд (go) или go north/south/west/east",
        "3 - отдохнуть (rest)",
        "4 - постучать по стене (listen)",
        "5 - зажечь фонарь (torch)",
        "6 - тренировка (train)",
        "7 - спуститься глубже (descend)",
        "8 - таблица лидеров (leaders)",
        "9 - магазин (shop)",
        "10 - рюкзак (backpack)",
        "11 - выпить зелье (drink)",
        "map - карта подземелья",
        "scout - сколько комнат доступно",
        "newgame - стереть сохранение",
        "0 - выйти из подземелья (exit)"]



def write_save():
    """Собирает состояние забега и пишет его в save.json.
    Кортежи и множества превращает в списки: JSON их не знает.
    Возвращает None.
    """
    save = {}
    save["hero"] = hero_name
    save["health"] = health
    save["stamina"] = stamina
    save["gold"] = gold_total
    save["actions"] = actions
    save["enemies"] = enemies
    save["position"] = [hero_r, hero_c]
    save["visited"] = [list(p) for p in visited]
    save["loot"] = sorted(found_loot)
    save["inventory"] = inventory
    save["ability_bonus"] = ability_bonus
    save["log"] = log
    save["damage"] = damage
    save["crit_damage"] = crit_damage
    save["max_health"] = max_health
    save["max_stamina"] = max_stamina
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.
    Возвращает None: контракт функции — печать, а не данные.
    """
    if not log:
        print("Вы ещё не сражались.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log, key=lambda r: r[2])
    print(f"Сильнейший удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя.
    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")


def scout(r, c, seen):
    """Рекурсивно считает доступные комнаты от клетки (r, c).
    seen — общее множество посещённых клеток обхода.
    Возвращает число доступных комнат.
    """
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total


def print_state(health, stamina, enemies_count, gold_total):
    """Печатает строку состояния зелёным, если colorama доступна.
    Возвращает None.
    """
    state = (f"Здоровье: {health}  Запас сил: {stamina}  "
             f"Врагов осталось: {enemies_count}  Золото: {gold_total}")
    if COLOR:
        print(Fore.GREEN + state + Style.RESET_ALL)
    else:
        print(state)


running = True
outcome = "прерывание"

try:
    while running:
        print("\n".join(MENU))
        print()

        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введи команду или номер.")
            line = input()
            cmd = line.strip().lower()
        words = cmd.split()
        verb = words[0]
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]

        match verb:
            case "exit":
                print("Вы разворачиваетесь и поднимаетесь обратно к свету. Шахта остаётся позади.")
                write_save()
                print("Прогресс сохранён.")
                outcome = "выход"
                running = False
            case "look":
                print("Вы осмотрелись. Стены покрыты каменистой пылью, вдали виден тёмный проход.")
            case "go":
                if len(words) > 1 and words[1] in DIRECTIONS:
                    dr, dc = DIRECTIONS[words[1]]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"Вы нашли {item}! Уникальный лут: {len(found_loot)}.")
                        print(f"Вы шагнули на {words[1]}. Комната ({hero_r}, {hero_c}).")
                    else:
                        print(f"Нельзя идти на {words[1]}: стена или край.")
                else:
                    cost = 2
                    if stamina >= cost:
                        stamina -= cost
                        print("Вы осторожно идёте вперёд. Под ногами хрустит мелкая угольная крошка.")
                    else:
                        health -= (cost - stamina)
                        stamina = 0
                        print("Сил больше нет — вы бредёте во тьме на одном упорстве. Дышать тяжело.")
            case "rest":
                print("Вы садитесь на холодный камень и переводите дух. Силы немного возвращаются.")
            case "listen":
                print("Вы постучали по стене. Звук глухой — за камнем сплошная порода.")
            case "torch":
                cost = 1
                if stamina >= cost:
                    stamina -= cost
                    print("Вы зажгли фонарь. Тьма немного отступила, стало уютнее.")
                else:
                    health -= (cost - stamina)
                    stamina = 0
                    print("Пальцы дрожат от усталости. Вы зажигаете фонарь, но это стоит вам последних сил.")
            case "train":
                cost = 3
                if stamina >= cost:
                    stamina -= cost
                else:
                    health -= (cost - stamina)
                    stamina = 0
                    print("Вы заставляете себя махать киркой через боль.")
                strikes = 6
                print("Вы подходите к старой ржавой вагонетке, набитой камнями.")
                print(f"Наносите {strikes} ударов.")
                total_damage = 0
                crit_count = 0
                for i in range(1, strikes + 1):
                    hit_damage, crit = dungeon.hero_hit(i, damage, crit_damage)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} урона — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f} урона")
                    total_damage += hit_damage
                average_damage = total_damage / strikes
                print(f"Итог: {strikes} ударов, критических: {crit_count}.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {average_damage:.1f}")
            case "descend":
                if not enemies:
                    print("Вы спускаетесь вниз, но подземелье пусто. Здесь больше некого искать.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = dungeon.fight(
                        enemy, health, ability_bonus, damage, crit_damage)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        msg = (f"{enemy} побеждён! В подземелье осталось врагов: {len(enemies)}. "
                               f"Добыча: {loot} золота.")
                        if COLOR:
                            print(Fore.YELLOW + msg + Style.RESET_ALL)
                        else:
                            print(msg)
                        print(f"Бой: {len(rounds)} раундов.")
            case "leaders":
                print_leaderboard(log)
            case "shop":
                print("Магазин:")
                for name, price in dungeon.prices.items():
                    print(f"{name}: {price} золота")
            case "backpack":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")
            case "drink":
                item = " ".join(words[1:]) or "зелье"
                if inventory.get(item, 0) == 0:
                    print(f"В рюкзаке нет предмета «{item}».")
                elif item == "зелье":
                    health = min(health + 10, max_health)
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f"Вы выпили зелье. Здоровье: {health}. "
                          f"Осталось зелий: {inventory.get(item, 0)}.")
                else:
                    print(f"«{item}» нельзя выпить.")
            case "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1])
                else:
                    qty = 1
                    item = " ".join(words[1:])
                if item == "":
                    print("Купить что? Введи: buy <предмет>.")
                    continue
                if item not in dungeon.prices:
                    print("Такого предмета в магазине нет.")
                    continue
                gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    if item == "эликсир":
                        ability_bonus += 2 * qty
                    print(f"Куплено {qty} {item} за {dungeon.prices[item] * qty} золота. "
                          f"Осталось золота: {gold_total}.")
                else:
                    print(f"Не хватает золота: нужно {dungeon.prices[item] * qty}, есть {gold_total}.")
            case "map":
                print("Карта:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        if (i, j) == (hero_r, hero_c):
                            cells.append("@")
                        else:
                            cells.append(MAP[i][j])
                    print(" ".join(cells))
            case "scout":
                seen = set()
                print(f"Разведка: {scout(hero_r, hero_c, seen)} комнат доступно.")
            case "newgame":
                if os.path.exists("save.json"):
                    os.remove("save.json")
                    print("Сохранение стёрто. Следующий забег начнётся с чистого листа.")
                else:
                    print("Нет сохранения, которое можно стереть.")
                continue
            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как раньше.")
            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Введи 'help'.")
                continue

        if running:
            actions += 1
            print()
            print_state(health, stamina, len(enemies), gold_total)
            if health <= 0:
                print()
                print(f"{hero_name} со стоном падает на холодный пол. Шахта забирает ещё одну душу.")
                if os.path.exists("save.json"):
                    os.remove("save.json")
                outcome = "гибель"
                running = False

except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
    write_save()
finally:
    print()
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    if inventory:
        print("Оставлено в рюкзаке:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("Оставлено в рюкзаке: ничего.")
    print_run_summary(log)
    print(frame)