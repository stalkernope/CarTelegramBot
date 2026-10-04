import random


from car_database import load_cars


from database import (
    get_player,
    add_car,
    add_coins,
    has_car
)




# =========================
# ЦЕНА
# =========================


def get_buy_price(car):

    return car.get(
        "price",
        100000
    )




# =========================
# МАШИНЫ МАГАЗИНА
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
# ПОИСК МАШИНЫ
# =========================


def find_shop_car(name):

    cars = load_cars()


    for car in cars:


        if car.get("name") == name:

            return car



    return None




# =========================
# ПОКУПКА
# =========================


def buy_car(user_id, car_name):


    player = get_player(
        user_id
    )



    car = find_shop_car(
        car_name
    )



    if not car:


        raise Exception(

            "Машина не найдена"

        )




    if has_car(

        user_id,

        car["name"]

    ):


        raise Exception(

            "Эта машина уже есть в гараже 🏎"

        )




    price = get_buy_price(
        car
    )



    if player["coins"] < price:


        raise Exception(

            "Недостаточно монет 💰"

        )



    add_coins(

        user_id,

        -price

    )



    add_car(

        user_id,

        car["name"]

    )



    return car