import random


from car_database import load_cars


from database import (
    get_player,
    add_car,
    add_coins,
    add_xp,
    has_car
)



CASE_PRICE = 500




# =========================
# ВЫБОР МАШИНЫ ИЗ КЕЙСА
# =========================


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

            if "Mythic" in car.get(
                "rarity",
                ""
            )

        ]


    # 30% Legendary

    elif chance <= 40:


        pool = [

            car for car in cars

            if "Legendary" in car.get(
                "rarity",
                ""
            )

        ]


    # 60% Rare

    else:


        pool = [

            car for car in cars

            if "Rare" in car.get(
                "rarity",
                ""
            )

        ]



    if not pool:

        pool = cars



    return random.choice(
        pool
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

            "Недостаточно монет 💰"

        )



    car = get_case_car()



    if not car:


        raise Exception(

            "Машины отсутствуют"

        )




    # списываем деньги

    add_coins(

        user_id,

        -CASE_PRICE

    )



    already = has_car(

        user_id,

        car["name"]

    )



    add_car(

        user_id,

        car["name"]

    )




    # награды

    if already:


        add_xp(

            user_id,

            200

        )


        add_coins(

            user_id,

            100

        )


    else:


        add_xp(

            user_id,

            100

        )



    return car