# ================================================
# ИГРА ЗАБРОШЕННАЯ ШАХТА
# Автор: Артем Бучнев
# Дата: октябрь 2026
# Этап 8: Сортировка и генераторы. Журнал боя стал
# таблицей чисел, добавлен лидерборд, рекорд врага
# и итог забега в прощании.
# Решение: при равных ударах врага max берёт первый
# из равных — устойчивость сортировки, это осознанный выбор.
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

# --- Враги и журнал боя ---------------------------
enemies = ["упырь", "скелет", "паук", "летучая мышь"]
log = []

# --- Главный цикл игры ---------------------------
running = True
actions = 0
menu_last = 8
outcome = "прерывание"

try:
    while running:
        # Меню выводится каждый круг
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - постучать по стене")
        print("5 - зажечь фонарь")
        print("6 - тренировка")
        print("7 - спуститься глубже")
        print("8 - таблица лидеров")
        print("0 - выйти из подземелья")

        # Универсальная проверка пункта меню
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Это не номер пункта. Введи число от 0 до 8:")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи число от 0 до 8:")

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
                    if i % 3 == 0:
                        hit_damage = crit_damage
                        print(f"Удар {i}: {hit_damage:.1f} урона — критический!")
                        crit_count += 1
                    else:
                        hit_damage = damage
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
                    enemy_hp = 45
                    round_n = 0
                    hero_strikes = 0
                    print(f"Вы спускаетесь по ступеням. Из темноты появляется {enemy}!")
                    while enemy_hp > 0 and health > 0:
                        round_n += 1
                        hero_strikes += 1
                        if hero_strikes % 3 == 0:
                            hit = crit_damage
                            crit_note = " — критический!"
                        else:
                            hit = damage
                            crit_note = ""
                        enemy_hp -= hit
                        if enemy_hp <= 0:
                            print(f"Раунд {round_n}: вы наносите {hit:.1f} урона{crit_note} Враг падает.")
                            log.append([round_n, hit, 0])
                            break
                        blow = random.randint(2, 6)
                        health -= blow
                        print(f"Раунд {round_n}: вы наносите {hit:.1f} урона{crit_note} "
                              f"Здоровье врага: {enemy_hp:.1f}. Враг бьёт в ответ на {blow}.")
                        log.append([round_n, hit, blow])
                    if enemy_hp <= 0:
                        enemies.remove(enemy)
                        print(f"{enemy} побеждён! В подземелье осталось врагов: {len(enemies)}.")
                        print(f"Бой: {round_n} раундов.")
            case "8":
                if not log:
                    print("Вы ещё не сражались.")
                else:
                    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
                    print("Таблица лидеров (урон героя):")
                    for i in range(len(top)):
                        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
                    worst = max(log, key=lambda r: r[2])
                    print(f"Сильнейший удар врага: {worst[2]} (раунд {worst[0]}).")

        if running:
            actions += 1
            print()
            print(f"Здоровье: {health}  Запас сил: {stamina}  Врагов осталось: {len(enemies)}")
            # Проверка гибели героя
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
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")
    print(frame)
