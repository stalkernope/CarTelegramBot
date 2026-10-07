# =========================
# SHOP CARS FINAL
# =========================


from database import (
    get_player,
    update_player,
    add_car,
    remove_coins
)


from car_database import (
    get_all_cars,
    get_car
)







# =========================
# SHOP LIST
# =========================


def get_shop_cars():


    cars = get_all_cars()


    return cars







# =========================
# BUY CAR
# =========================


def buy_car(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    car = get_car(

        car_name

    )



    if not car:


        raise Exception(

            "Машина не найдена"

        )





    if car_name in player.get(

        "garage",

        []

    ):


        raise Exception(

            "Эта машина уже есть"

        )





    price = car.get(

        "price",

        0

    )





    if player.get(

        "coins",

        0

    ) < price:


        raise Exception(

            "Недостаточно монет"

        )





    player["coins"] -= price



    if "garage" not in player:


        player["garage"] = []





    player["garage"].append(

        car_name

    )





    if not player.get(

        "main_car"

    ):


        player["main_car"] = car_name





    update_player(

        user_id,

        player

    )





    return car







# =========================
# FREE CAR
# =========================


def give_free_car(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )


    if car_name not in player.get(

        "garage",

        []

    ):


        player["garage"].append(

            car_name

        )



    update_player(

        user_id,

        player

    )