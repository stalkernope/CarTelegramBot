from database import (
    get_player,
    update_player,
    add_car
)

from car_database import (
    get_all_cars,
    get_car
)



# =========================
# МАШИНЫ МАГАЗИНА
# =========================


def get_shop_cars():

    cars = get_all_cars()


    # самые дорогие и редкие впереди

    cars.sort(

        key=lambda x: x.get(
            "price",
            0
        ),

        reverse=True

    )


    return cars[:10]



# =========================
# ЦЕНА
# =========================


def get_car_price(car):

    if isinstance(car, str):

        car = get_car(
            car
        )


    if not car:

        return 0


    return car.get(
        "price",
        0
    )



# =========================
# ПОКУПКА
# =========================


def buy_car(
    user_id,
    car_name
):


    car = get_car(
        car_name
    )


    if not car:

        raise Exception(
            "Машина не найдена"
        )



    player = get_player(
        user_id
    )



    price = get_car_price(
        car
    )



    if player["coins"] < price:


        raise Exception(

            "Недостаточно монет"

        )



    if car_name in player["garage"]:


        raise Exception(

            "Эта машина уже есть в гараже"

        )



    player["coins"] -= price


    update_player(

        user_id,

        player

    )


    add_car(

        user_id,

        car_name

    )


    return car