import random

from car_database import load_cars
from database import (
    get_player,
    add_car,
    add_coins,
    add_xp
)


CASE_PRICE = 500



def get_case_car():

    cars = load_cars()


    if not cars:

        return None



    chance = random.randint(
        1,
        100
    )


    # 10% Mythic

    if chance <= 10:

        pool = [

            car for car in cars

            if "Mythic" in car["rarity"]

        ]



    # 30% Legendary

    elif chance <= 40:

        pool = [

            car for car in cars

            if "Legendary" in car["rarity"]

        ]



    # 60% Rare

    else:

        pool = [

            car for car in cars

            if "Rare" in car["rarity"]

        ]



    if not pool:

        pool = cars



    return random.choice(pool)




def open_case(user_id):


    player = get_player(
        user_id
    )


    if player["coins"] < CASE_PRICE:

        raise Exception(
            "Недостаточно монет"
        )



    add_coins(

        user_id,

        -CASE_PRICE

    )


    car = get_case_car()



    if not car:

        raise Exception(
            "Нет машин"
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