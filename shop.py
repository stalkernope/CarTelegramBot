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


    return random.choice(cars)





def open_case(user_id):


    player = get_player(
        user_id
    )


    if player["coins"] < CASE_PRICE:

        raise Exception(
            "Недостаточно монет"
        )



    car = get_case_car()


    if not car:

        raise Exception(
            "Нет машин в базе"
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