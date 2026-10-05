import random


from car_database import (
    get_all_cars
)


from database import (
    add_car
)



# =========================
# ВЕСА КЕЙСА
# =========================


RARITY_CHANCE = {


    "🔵 Rare": 70,


    "💎 Legendary": 25,


    "🔥 Mythic": 5

}



# =========================
# ВЫБОР ИЗ КЕЙСА
# =========================


def open_case(user_id):


    cars = get_all_cars()



    if not cars:

        return None



    weighted = []



    for car in cars:


        rarity = car.get(

            "rarity",

            "🔵 Rare"

        )


        chance = RARITY_CHANCE.get(

            rarity,

            10

        )



        weighted.extend(

            [car] * chance

        )



    car = random.choice(

        weighted

    )



    add_car(

        user_id,

        car["name"]

    )



    return car



# =========================
# ИНФОРМАЦИЯ О КЕЙСЕ
# =========================


def case_info():


    return (

        "🎁 <b>LEGEND CASE</b>\n\n"

        "🔵 Rare — 70%\n"

        "💎 Legendary — 25%\n"

        "🔥 Mythic — 5%\n\n"

        "Открывай и собирай коллекцию!"

    )