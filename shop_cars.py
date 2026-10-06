from database import (
    get_player,
    add_car,
    remove_coins
)


from car_database import (
    get_car,
    get_all_cars
)





# =========================
# SHOP CARS
# =========================


def get_shop_cars():


    cars = get_all_cars()



    shop = []



    for car in cars:


        if car.get(

            "shop",

            True

        ):


            shop.append(

                car

            )



    return shop







# =========================
# FIND SHOP CAR
# =========================


def find_shop_car(name):


    cars = get_shop_cars()



    for car in cars:


        if car["name"] == name:


            return car



    return None







# =========================
# BUY CAR
# =========================


def buy_car(

    user_id,

    car_name

):


    car = find_shop_car(

        car_name

    )



    if not car:


        raise Exception(

            "Машина не найдена"

        )






    player = get_player(

        user_id

    )





    if car_name in player["garage"]:


        raise Exception(

            "У тебя уже есть эта машина"

        )







    price = car.get(

        "price",

        0

    )







    if player["coins"] < price:


        raise Exception(

            "Недостаточно монет"

        )








    success = remove_coins(

        user_id,

        price

    )



    if not success:


        raise Exception(

            "Ошибка оплаты"

        )








    add_car(

        user_id,

        car_name

    )





    return car