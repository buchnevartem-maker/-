# ================================================
# ИГРА ЗАБРОШЕННАЯ ШАХТА
# Автор: Артем Бучнев
# Дата: октябрь 2026
# Этап 10: Функции глубже. Добавлены золото и магазин
# с умолчаниями и именованными аргументами, надбавка
# к урону через bonus, потолки здоровья и запаса сил.
# Решение: боевой эликсир копит надбавку до конца забега,
# каждая покупка добавляет +2 к урону за штуку.
# Решение: bonus прибавляется к обычному урону до удвоения
# критом — критический удар с эликсиром бьёт вдвое сильнее.
# Решение: при равных ударах врага max берёт первый
# из равных — устойчивость сортировки, осознанный выбор.
# ================================================
import random
# --- Заголовок ------------------------------------
title = "ЗАБРОШЕННАЯ ШАХТА"
frame = "=" * (len(title) + 6)
print(frame)
print(f"   {title}   ")
print(frame)
print()
# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты стоишь у входа в заброшенную шахту. Оттуда тянет могильным холодом и угольной пылью.")
print()
# --- Настройка героя -------------------------------
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
# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = (health // 10) + luck
# --- Потолки героя ---------------------------------
max_health = health
max_stamina = stamina
# --- Формуляр героя --------------------------------
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
# --- Враги, журнал и кошелёк ----------------------
enemies = ["упырь", "скелет", "паук", "летучая мышь"]
log = []
gold_total = 0
ability_bonus = 0
# --- Функции --------------------------------------
def hero_hit(strike_n, bonus=0):
    """Урон героя в удар номер strike_n.
    bonus — надбавка к обычному урону, по умолчанию 0.
    Надбавка прибавляется до удвоения критом.
    Возвращает пару (hit, crit): урон и признак критического удара.
    Читает глобальные damage и crit_damage, ничего не меняет.
    """
    if strike_n % 3 == 0:
        return (damage + bonus) * 2, True
    return damage + bonus, False


def fight(enemy, hero_health, bonus=0):
    """Бой с enemy до гибели одного из двоих.
    bonus — надбавка к урону героя, по умолчанию 0: без эликсира
    бой идёт как прежде. Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot):
    таблицу раундов, признак победы, здоровье после боя и трофеи.
    Глобальные переменные не меняет.
    """
    enemy_hp = 45.0
    rounds = []
    round_n = 0
    print(f"Вы спускаетесь по ступеням. Из темноты появляется {enemy}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n, bonus=bonus)
        enemy_hp -= hit
        line = f"Раунд {round_n}: вы наносите {hit:.1f} урона"
        if crit:
            line += " — критический!"
        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += f" Здоровье врага: {enemy_hp:.1f}. Враг бьёт в ответ на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy_hp <= 0
    if won:
        loot = 10 + 5 * round_n
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
# --- Главный цикл игры ---------------------------
running = True
actions = 0
menu_last = 9
outcome = "прерывание"

try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - постучать по стене")
        print("5 - зажечь фонарь")
        print("6 - тренировка")
        print("7 - спуститься глубже")
        print("8 - таблица лидеров")
        print("9 - магазин")
        print("0 - выйти из подземелья")
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Это не номер пункта. Введи число от 0 до 9:")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи число от 0 до 9:")
        # Разбор выбора
        match choice:
            case "0":
                print("Вы разворачиваетесь и поднимаетесь обратно к свету. Шахта остаётся позади.")
                outcome = "выход"
                running = False
            case "1":
                print("Вы осмотрелись. Стены покрыты каменистой пылью, вдали виден тёмный проход.")
            case "2":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Под ногами хрустит мелкая угольная крошка.")
                else:
                    health -= (cost - stamina)
                    stamina = 0
                    print("Сил больше нет — вы бредёте во тьме на одном упорстве. Дышать тяжело.")
            case "3":
                print("Вы садитесь на холодный камень и переводите дух. Силы немного возвращаются.")
            case "4":
                print("Вы постучали по стене. Звук глухой — за камнем сплошная порода.")
            case "5":
                cost = 1
                if stamina >= cost:
                    stamina -= cost
                    print("Вы зажгли фонарь. Тьма немного отступила, стало уютнее.")
                else:
                    health -= (cost - stamina)
                    stamina = 0
                    print("Пальцы дрожат от усталости. Вы зажигаете фонарь, но это стоит вам последних сил.")
            case "6":
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
                    hit_damage, crit = hero_hit(i)
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
            case "7":
                if not enemies:
                    print("Вы спускаетесь вниз, но подземелье пусто. Здесь больше некого искать.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"{enemy} побеждён! В подземелье осталось врагов: {len(enemies)}. "
                              f"Добыча: {loot} золота.")
                        print(f"Бой: {len(rounds)} раундов.")
            case "8":
                print_leaderboard(log)
            case "9":
                print("Магазин:")
                print("1 - зелье (+10 здоровья): 10 золота")
                print("2 - масло для фонаря (+5 запаса сил): 15 золота")
                print("3 - боевой эликсир (+2 к урону за забег): 40 золота")
                print("Номер предмета (0 — не покупать):")
                item = input()
                prices = (10, 15, 40)
                names = ("зелье", "масло для фонаря", "боевой эликсир")
                if item in ("1", "2", "3"):
                    price = prices[int(item) - 1]
                    name = names[int(item) - 1]
                    print("Количество (Enter — одна штука):")
                    qty_line = input()
                    if qty_line == "":
                        qty = 1
                        gold_total, ok = buy(price, gold_total)
                    else:
                        try:
                            qty = int(qty_line)
                        except ValueError:
                            qty = 0
                        gold_total, ok = buy(price, gold_total, quantity=qty)
                    if ok:
                        if item == "1":
                            health = min(health + 10 * qty, max_health)
                        elif item == "2":
                            stamina = min(stamina + 5 * qty, max_stamina)
                        else:
                            ability_bonus += 2 * qty
                        print(f"Куплено {qty} {name} за {price * qty} золота. Осталось золота: {gold_total}.")
                    else:
                        print(f"Не хватает золота: нужно {price * qty}, есть {gold_total}.")
                elif item != "0":
                    print("Такого предмета в магазине нет.")

        if running:
            actions += 1
            print()
            print(f"Здоровье: {health}  Запас сил: {stamina}  "
                  f"Врагов осталось: {len(enemies)}  Золото: {gold_total}")
            if health <= 0:
                print()
                print(f"{hero_name} со стоном падает на холодный пол. Шахта забирает ещё одну душу.")
                outcome = "гибель"
                running = False

except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
finally:
    print()
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print_run_summary(log)
    print(frame)