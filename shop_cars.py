import random


from car_database import load_cars


from database import (
    get_player,
    add_car,
    add_coins,
    add_xp,
    has_car
)



# =========================
# ЦЕНА МАШИНЫ
# =========================


def get_buy_price(car):

    if "Mythic" in car.get("rarity", ""):

        return car.get(
            "price",
            1000000
        )


    if "Legendary" in car.get("rarity", ""):

        return car.get(
            "price",
            500000
        )


    if "Rare" in car.get("rarity", ""):

        return car.get(
            "price",
            150000
        )


    return car.get(
        "price",
        50000
    )



# =========================
# МАШИНЫ В МАГАЗИНЕ
# =========================


def get_shop_cars(count=3):

    cars = load_cars()


    if not cars:

        return []



    if len(cars) <= count:

        return cars



    return random.sample(

        cars,

        count

    )



# =========================
# НАЙТИ МАШИНУ
# =========================


def find_car(car_name):

    cars = load_cars()


    for car in cars:

        if car.get("name") == car_name:

            return car



    return None



# =========================
# ПОКУПКА
# =========================


def buy_car(user_id, car_name):


    player = get_player(
        user_id
    )


    car = find_car(
        car_name
    )



    if not car:

        raise Exception(
            "❌ Машина не найдена"
        )



    if has_car(

        user_id,

        car["name"]

    ):

        raise Exception(
            "❌ Эта машина уже есть в гараже"
        )



    price = get_buy_price(
        car
    )



    if player["coins"] < price:

        raise Exception(

            f"❌ Нужно {price} 🪙"

        )



    add_coins(

        user_id,

        -price

    )


    add_car(

        user_id,

        car["name"]

    )


    add_xp(

        user_id,

        200

    )



    return car



# =========================
# ТЕКСТ МАГАЗИНА
# =========================


def shop_text():

    return (

        "🛒 <b>CAR LEGENDS SHOP</b>\n\n"

        "Покупай легендарные машины 🚗\n\n"

        "🔵 Rare\n"

        "💎 Legendary\n"

        "🔥 Mythic\n"

    )