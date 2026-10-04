import random


from car_database import load_cars


from database import (
    get_player,
    add_car,
    add_coins,
    add_xp
)



# =========================
# НАСТРОЙКИ
# =========================


CASE_PRICE = 500



# =========================
# ШАНСЫ РЕДКОСТИ
# =========================


RARITY_CHANCES = [

    ("🔵 Rare", 60),

    ("💎 Legendary", 30),

    ("🔥 Mythic", 10)

]



# =========================
# ПОЛУЧЕНИЕ МАШИНЫ ИЗ КЕЙСА
# =========================


def get_case_car():

    cars = load_cars()


    if not cars:

        return None



    rarity_roll = random.randint(
        1,
        100
    )


    if rarity_roll <= 10:

        rarity = "🔥 Mythic"


    elif rarity_roll <= 40:

        rarity = "💎 Legendary"


    else:

        rarity = "🔵 Rare"



    filtered = []


    for car in cars:

        if car.get("rarity") == rarity:

            filtered.append(
                car
            )



    if not filtered:

        filtered = cars



    return random.choice(
        filtered
    )



# =========================
# ОТКРЫТИЕ КЕЙСА
# =========================


def open_case(user_id):


    player = get_player(
        user_id
    )



    if player["coins"] < CASE_PRICE:

        raise Exception(
            "❌ Нужно 500 🪙 монет"
        )



    car = get_case_car()



    if not car:

        raise Exception(
            "❌ Машины не найдены"
        )



    add_coins(

        user_id,

        -CASE_PRICE

    )


    add_car(

        user_id,

        car["name"]

    )


    add_xp(

        user_id,

        100

    )



    return car



# =========================
# ИНФОРМАЦИЯ КЕЙСА
# =========================


def case_info():

    return (

        "🎁 <b>LEGEND CASE</b>\n\n"

        "💰 Цена: 500 🪙\n\n"

        "🔵 Rare — 60%\n"

        "💎 Legendary — 30%\n"

        "🔥 Mythic — 10%\n\n"

        "Открой и получи легендарную машину!"

    )



# =========================
# ЦЕНА
# =========================


def get_car_price(car):

    return car.get(
        "price",
        100000
    )