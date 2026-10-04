import random


from car_database import (
    get_random_car
)


from database import (
    add_win,
    add_loss
)



BATTLES_FILE = "battle_stats.json"



import json
import os



# =========================
# СТАТИСТИКА МАШИН
# =========================


def load_stats():

    if not os.path.exists(BATTLES_FILE):

        return {}


    with open(
        BATTLES_FILE,
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_stats(data):

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



# =========================
# СОЗДАТЬ БИТВУ
# =========================


def create_battle():

    car1 = get_random_car()

    car2 = get_random_car()



    while car1["name"] == car2["name"]:

        car2 = get_random_car()



    return car1, car2



# =========================
# СИЛА МАШИНЫ
# =========================


def car_power(car):

    score = 0


    score += car.get(
        "power",
        0
    )


    score += car.get(
        "speed",
        0
    )


    rarity = car.get(
        "rarity",
        ""
    )


    if "Mythic" in rarity:

        score += 500


    elif "Legendary" in rarity:

        score += 300


    elif "Rare" in rarity:

        score += 100



    return score



# =========================
# РЕЗУЛЬТАТ
# =========================


def fight(car1, car2):

    power1 = car_power(
        car1
    )


    power2 = car_power(
        car2
    )


    if power1 > power2:

        winner = car1

        loser = car2


    elif power2 > power1:

        winner = car2

        loser = car1


    else:

        winner = random.choice(
            [
                car1,
                car2
            ]
        )

        loser = (
            car2
            if winner == car1
            else car1
        )



    save_result(
        winner,
        loser
    )


    return winner, loser



# =========================
# СТАТИСТИКА
# =========================


def save_result(
    winner,
    loser
):

    data = load_stats()



    if winner["name"] not in data:

        data[winner["name"]] = {

            "wins":0

        }



    if loser["name"] not in data:

        data[loser["name"]] = {

            "wins":0

        }



    data[winner["name"]]["wins"] += 1



    save_stats(
        data
    )



# =========================
# ИГРОК ВЫИГРАЛ
# =========================


def player_win(user_id):

    add_win(
        user_id
    )



def player_loss(user_id):

    add_loss(
        user_id
    )
    
    def battle_text(car1, car2):

    return (

        "⚔️ <b>LEGEND BATTLE</b>\n\n"

        f"🏎 <b>{car1['name']}</b>\n"
        f"⚡ {car1['power']} л.с.\n"
        f"🚀 {car1['speed']} км/ч\n"
        f"💎 {car1['rarity']}\n\n"

        "🔥 VS 🔥\n\n"

        f"🏎 <b>{car2['name']}</b>\n"
        f"⚡ {car2['power']} л.с.\n"
        f"🚀 {car2['speed']} км/ч\n"
        f"💎 {car2['rarity']}\n\n"

        "Выбирай победителя 👇"
    )
    
    def start_battle():

    return create_battle()