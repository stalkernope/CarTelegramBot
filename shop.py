import random


from car_database import (
    get_random_car,
    load_cars
)


from database import (
    get_player,
    add_car
)



# =========================
# ЦЕНА МАШИНЫ
# =========================


def get_car_price(car):

    rarity = car.get(
        "rarity",
        ""
    )


    if "Mythic" in rarity:

        return 1000000


    if "Legendary" in rarity:

        return 500000


    if "Rare" in rarity:

        return 150000


    return 50000



# =========================
# ПОКУПКА
# =========================


def buy_car(user_id, car):

    player = get_player(
        user_id
    )


    price = get_car_price(
        car
    )


    if player["coins"] < price:

        return {

            "success": False,

            "message":
            "❌ Не хватает монет"

        }



    player["coins"] -= price


    add_car(

        user_id,

        car["name"]

    )


    return {

        "success": True,

        "message":

        f"🏎 Поздравляем!\n"
        f"Ты купил {car['name']}"

    }



# =========================
# КЕЙСЫ
# =========================


def open_case(user_id):


    cars = load_cars()


    chance = random.randint(
        1,
        100
    )


    if chance <= 5:

        # Mythic

        possible = [

            c for c in cars

            if "Mythic" in c["rarity"]

        ]


    elif chance <= 25:

        # Legendary

        possible = [

            c for c in cars

            if "Legendary" in c["rarity"]

        ]


    else:

        possible = cars



    car = random.choice(
        possible
    )


    add_car(

        user_id,

        car["name"]

    )


    return car



# =========================
# ИНФОРМАЦИЯ О КЕЙСЕ
# =========================


def case_info():

    return """

🎁 <b>LEGEND CASE</b>

Шансы:

🔥 Mythic — 5%

💎 Legendary — 20%

🔵 Rare — 75%

Открой и попробуй получить легенду!
"""