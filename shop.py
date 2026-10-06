import random



from database import (
    get_player,
    remove_coins,
    add_car
)


from car_database import (
    get_all_cars
)







# =========================
# CASE SETTINGS
# =========================


CASE_PRICE = 2500








# =========================
# GET CASE CARS
# =========================


def get_case_cars():


    cars = get_all_cars()



    result = []



    for car in cars:


        if car.get(

            "case",

            True

        ):


            result.append(

                car

            )



    return result








# =========================
# RANDOM CAR
# =========================


def random_case_car():


    cars = get_case_cars()



    if not cars:


        return None



    weights = []



    for car in cars:


        rarity = car.get(

            "rarity",

            "Common"

        )



        if rarity == "Legendary":


            weights.append(5)



        elif rarity == "Epic":


            weights.append(15)



        elif rarity == "Rare":


            weights.append(30)



        else:


            weights.append(50)





    return random.choices(

        cars,

        weights=weights,

        k=1

    )[0]









# =========================
# OPEN CASE
# =========================


def open_case(user_id):


    player = get_player(

        user_id

    )



    if player["coins"] < CASE_PRICE:


        raise Exception(

            "Недостаточно монет для кейса"

        )





    paid = remove_coins(

        user_id,

        CASE_PRICE

    )



    if not paid:


        raise Exception(

            "Ошибка оплаты"

        )






    car = random_case_car()



    if not car:


        raise Exception(

            "Нет машин в кейсе"

        )





    add_car(

        user_id,

        car["name"]

    )





    return car