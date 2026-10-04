import random

from database import (
    get_player,
    add_car,
    add_coins
)

from car_database import (
    get_random_car
)



# =========================
# НАГРАДЫ
# =========================


def daily_reward(user_id):

    coins = random.randint(
        100,
        500
    )

    xp = random.randint(
        20,
        100
    )


    add_coins(
        user_id,
        coins
    )


    return {

        "coins": coins,

        "xp": xp

    }



# =========================
# ЦЕНА МАШИНЫ
# =========================


def car_price(car):

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


    price = car_price(
        car
    )


    if player["coins"] < price:

        return {

            "success": False,

            "message":
            "❌ Недостаточно монет"

        }



    player["coins"] -= price


    add_car(

        user_id,

        car["name"]

    )


    return {

        "success": True,

        "message":

        f"🏎 Ты купил {car['name']}"

    }



# =========================
# КЕЙС
# =========================


def open_case(user_id):


    car = get_random_car()


    add_car(

        user_id,

        car["name"]

    )


    return car



# =========================
# СЛУЧАЙНЫЙ БОНУС
# =========================


def random_bonus(user_id):


    reward = random.choice(

        [

            ("coins", 500),

            ("coins", 1000),

            ("coins", 5000),

            ("rare", True)

        ]

    )


    if reward[0] == "coins":

        add_coins(

            user_id,

            reward[1]

        )


    return reward