# =========================
# SHOP CARS FINAL COMPLETE
# CAR LEGENDS
# =========================


from car_database import (
    get_all_cars,
    get_car
)


from database import (
    get_player,
    add_car,
    remove_car,
    add_coins,
    remove_coins,
    add_gems,
    remove_gems,
    update_player
)





# =========================
# GET ALL SHOP CARS
# =========================


def get_shop_cars():


    result = []


    for car in get_all_cars():


        if car.get("locked", False):

            continue


        result.append(car)


    return result





# =========================
# GET CAR CARD FOR MINI APP
# =========================


def get_car_card(car_name):


    car = get_car(car_name)



    if not car:


        return None



    return {


        "name": car["name"],

        "brand": car.get(
            "brand",
            ""
        ),


        "class": car.get(
            "class",
            "A"
        ),


        "rarity": car.get(
            "rarity",
            "Common"
        ),


        "price": car.get(
            "price",
            0
        ),


        "power": car.get(
            "power",
            0
        ),


        "speed": car.get(
            "speed",
            0
        ),


        "handling": car.get(
            "handling",
            0
        ),


        "image": car.get(
            "image",
            ""
        )

    }





# =========================
# SEARCH
# =========================


def search_shop(text):


    text = str(text).lower()



    result = []



    for car in get_shop_cars():


        if text in car["name"].lower():


            result.append(car)



    return result
    
    
    # =========================
# FILTER BY CLASS
# =========================


def filter_by_class(car_class):


    result = []


    for car in get_shop_cars():


        if car.get("class") == car_class:


            result.append(car)



    return result







# =========================
# FILTER BY RARITY
# =========================


def filter_by_rarity(rarity):


    result = []


    for car in get_shop_cars():


        if car.get("rarity") == rarity:


            result.append(car)



    return result







# =========================
# BUY CAR WITH COINS
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


        return {

            "success":False,

            "text":"❌ Машина не найдена"

        }







    if car_name in player.get(

        "garage",

        []

    ):


        return {

            "success":False,

            "text":"🚗 Машина уже есть в гараже"

        }







    if car.get(

        "locked",

        False

    ):


        return {

            "success":False,

            "text":"🔒 Машина заблокирована"

        }







    price = car.get(

        "price",

        0

    )







    if player["coins"] < price:


        return {

            "success":False,

            "text":"💰 Недостаточно монет"

        }








    remove_coins(

        user_id,

        price

    )



    add_car(

        user_id,

        car_name

    )





    return {

        "success":True,

        "text":f"""

✅ Покупка совершена!


🏎 {car_name}


💰 Потрачено:

{price} coins

"""

    }









# =========================
# BUY WITH GEMS
# =========================


def buy_car_with_gems(

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


        return {

            "success":False,

            "text":"❌ Машина не найдена"

        }







    price = car.get(

        "gems_price",

        0

    )



    if price <= 0:


        return {

            "success":False,

            "text":"❌ Нельзя купить за Gems"

        }







    if player["gems"] < price:


        return {

            "success":False,

            "text":"💎 Недостаточно Gems"

        }







    remove_gems(

        user_id,

        price

    )



    add_car(

        user_id,

        car_name

    )



    return {

        "success":True,

        "text":f"""

💎 Покупка за Gems успешна!


🏎 {car_name}

"""

    }









# =========================
# BUY WITH TOKENS
# =========================


def buy_car_with_tokens(

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


        return {

            "success":False,

            "text":"❌ Машина не найдена"

        }





    price = car.get(

        "token_price",

        0

    )



    if price <= 0:


        return {

            "success":False,

            "text":"❌ Нельзя купить за Tokens"

        }






    if player["tokens"] < price:


        return {

            "success":False,

            "text":"🎟 Недостаточно Tokens"

        }






    player["tokens"] -= price



    update_player(

        user_id,

        player

    )



    add_car(

        user_id,

        car_name

    )



    return {

        "success":True,

        "text":f"""

🎟 Покупка за Tokens!


🏎 {car_name}

"""

    }
    
    
    # =========================
# SELL CAR
# =========================


def sell_car(

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


        return {

            "success":False,

            "text":"❌ Такой машины нет в гараже"

        }







    car = get_car(

        car_name

    )



    if not car:


        return {

            "success":False,

            "text":"❌ Машина не найдена"

        }







    sell_price = int(

        car.get(

            "price",

            0

        )

        *

        0.5

    )







    remove_car(

        user_id,

        car_name

    )



    add_coins(

        user_id,

        sell_price

    )







    return {

        "success":True,

        "text":f"""

💰 Машина продана!


🏎 {car_name}


Получено:

{sell_price} coins

"""

    }








# =========================
# UNLOCK CAR
# =========================


def unlock_car(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    if car_name in player.get(

        "unlocked_cars",

        []

    ):


        return False






    if "unlocked_cars" not in player:


        player["unlocked_cars"] = []





    player["unlocked_cars"].append(

        car_name

    )



    update_player(

        user_id,

        player

    )



    return True








# =========================
# CHECK UNLOCK
# =========================


def is_car_unlocked(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    return car_name in player.get(

        "unlocked_cars",

        []

    )








# =========================
# GET BEST CARS
# =========================


def get_best_cars(

    limit=10

):


    cars = get_shop_cars()



    cars.sort(

        key=lambda x:

        x.get(

            "power",

            0

        ),

        reverse=True

    )



    return cars[:limit]








# =========================
# MINI APP SHOP DATA
# =========================


def get_shop_data():


    result = []



    for car in get_shop_cars():


        result.append(

            {

                "name":
                car["name"],


                "brand":
                car.get(
                    "brand",
                    ""
                ),


                "price":
                car.get(
                    "price",
                    0
                ),


                "power":
                car.get(
                    "power",
                    0
                ),


                "speed":
                car.get(
                    "speed",
                    0
                ),


                "handling":
                car.get(
                    "handling",
                    0
                ),


                "rarity":
                car.get(
                    "rarity",
                    ""
                ),


                "image":
                car.get(
                    "image",
                    ""
                )

            }

        )



    return result








# =========================
# PLAYER CAN BUY
# =========================


def can_buy(

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


        return False




    if car_name in player.get(

        "garage",

        []

    ):


        return False




    if player["coins"] >= car.get(

        "price",

        0

    ):


        return True



    return False