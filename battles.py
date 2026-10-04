import random
import json
import os


from car_database import get_random_car


from database import (
    add_win,
    add_loss
)



BATTLE_FILE = "battle_stats.json"



# =========================
# СТАТИСТИКА МАШИН
# =========================


def load_stats():

    if not os.path.exists(
        BATTLE_FILE
    ):

        return {}



    try:

        with open(
            BATTLE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


            if isinstance(data, dict):

                return data


    except Exception as e:

        print(
            "Ошибка статистики:",
            e
        )


    return {}



def save_stats(data):

    try:

        with open(
            BATTLE_FILE,
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

    car1 = get_random_car()

    car2 = get_random_car()



    if not car1 or not car2:

        return None, None



    attempts = 0


    while (

        car1["name"] == car2["name"]

        and attempts < 20

    ):

        car2 = get_random_car()

        attempts += 1



    return car1, car2



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



    rarity_bonus = 0



    if "Mythic" in rarity:

        rarity_bonus = 500


    elif "Legendary" in rarity:

        rarity_bonus = 300


    elif "Rare" in rarity:

        rarity_bonus = 150



    random_bonus = random.randint(
        -50,
        50
    )



    return (

        power * 0.6

        +

        speed * 2

        +

        rarity_bonus

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



    save_car_win(
        winner
    )



    return winner, loser



# =========================
# ПОБЕДЫ МАШИН
# =========================


def save_car_win(car):

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
# ТЕКСТ БИТВЫ
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
# ЗАПУСК
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