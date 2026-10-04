import random
import json
import os


from car_database import get_random_car


from database import (
    add_win,
    add_loss
)



BATTLES_FILE = "battle_stats.json"




# =========================
# СТАТИСТИКА
# =========================


def load_stats():

    if not os.path.exists(BATTLES_FILE):

        return {}


    try:

        with open(
            BATTLES_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


            if isinstance(data, dict):

                return data


            return {}


    except Exception as e:

        print(
            "Ошибка battle_stats:",
            e
        )

        return {}




def save_stats(data):

    try:

        with open(
            BATTLES_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(

                data,

                file,

                ensure_ascii=False,

                indent=4

            )


    except Exception as e:

        print(
            "Ошибка сохранения битв:",
            e
        )




# =========================
# СОЗДАНИЕ БИТВЫ
# =========================


def create_battle():

    cars = []


    first = get_random_car()


    if first:

        cars.append(first)



    second = get_random_car()


    if second:

        cars.append(second)



    if len(cars) < 2:

        return None, None



    # защита от одинаковых машин

    attempts = 0


    while (

        cars[0]["name"]

        ==

        cars[1]["name"]

        and attempts < 10

    ):

        cars[1] = get_random_car()

        attempts += 1



    return cars[0], cars[1]




# =========================
# СИЛА МАШИНЫ
# =========================


def car_power(car):

    if not car:

        return 0



    power = car.get(
        "power",
        0
    )


    speed = car.get(
        "speed",
        0
    )


    rarity = car.get(
        "rarity",
        ""
    )


    bonus = 0


    if "Mythic" in rarity:

        bonus = 500


    elif "Legendary" in rarity:

        bonus = 300


    elif "Rare" in rarity:

        bonus = 150



    random_bonus = random.randint(
        -50,
        50
    )


    return (

        power * 0.5

        +

        speed * 2

        +

        bonus

        +

        random_bonus

    )




# =========================
# БИТВА
# =========================


def fight(car1, car2):

    if not car1 or not car2:

        return None, None



    score1 = car_power(
        car1
    )


    score2 = car_power(
        car2
    )



    if score1 >= score2:

        winner = car1

        loser = car2


    else:

        winner = car2

        loser = car1




    save_result(
        winner
    )


    return winner, loser




# =========================
# СОХРАНЕНИЕ ПОБЕД МАШИН
# =========================


def save_result(car):

    if not car:

        return


    data = load_stats()


    name = car["name"]



    if name not in data:

        data[name] = {

            "wins": 0

        }



    data[name]["wins"] += 1



    save_stats(
        data
    )




# =========================
# ТЕКСТ
# =========================


def battle_text(car1, car2):

    return (

        "⚔️ <b>LEGEND BATTLE</b>\n\n"

        f"🏎 <b>{car1['name']}</b>\n"

        f"⚡ {car1.get('power',0)} л.с.\n"

        f"🚀 {car1.get('speed',0)} км/ч\n"

        f"💎 {car1.get('rarity','')}\n\n"

        "🔥 VS 🔥\n\n"

        f"🏎 <b>{car2['name']}</b>\n"

        f"⚡ {car2.get('power',0)} л.с.\n"

        f"🚀 {car2.get('speed',0)} км/ч\n"

        f"💎 {car2.get('rarity','')}\n\n"

        "Выбирай победителя 👇"

    )




# =========================
# СТАРТ БИТВЫ
# =========================


def start_battle():

    return create_battle()




# =========================
# НАГРАДЫ ИГРОКА
# =========================


def player_win(user_id):

    add_win(
        user_id
    )



def player_loss(user_id):

    add_loss(
        user_id
    )