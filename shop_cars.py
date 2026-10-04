import random


from car_database import load_cars


from database import (
    get_player,
    add_car,
    add_coins
)



# =========================
# ЦЕНА МАШИНЫ
# =========================


def get_buy_price(car):

    return car.get(
        "price",
        100000
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
# ПОКУПКА
# =========================


def buy_car(user_id, car_name):


    player = get_player(
        user_id
    )


    cars = load_cars()



    car = None


    for item in cars:

        if item["name"] == car_name:

            car = item

            break



    if not car:

        raise Exception(

            "Машина не найдена"

        )



    price = get_buy_price(
        car
    )



    if player["coins"] < price:

        raise Exception(

            "Недостаточно монет"

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