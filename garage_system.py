# =========================
# GARAGE SYSTEM FINAL COMPLETE
# CAR LEGENDS
# =========================


from database import (
    get_player,
    add_car,
    remove_car,
    set_main_car as db_set_main_car
)


from car_database import (
    get_car
)





# =========================
# GET PLAYER GARAGE
# =========================


def get_garage(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "garage",

        []

    )








# =========================
# GET GARAGE CARDS
# FOR MINI APP
# =========================


def get_garage_cards(user_id):


    garage = get_garage(

        user_id

    )


    result = []



    for car_name in garage:


        car = get_car(

            car_name

        )



        if not car:

            continue




        result.append(

            {

                "name":
                car.get(
                    "name",
                    ""
                ),


                "brand":
                car.get(
                    "brand",
                    ""
                ),


                "class":
                car.get(
                    "class",
                    "A"
                ),


                "rarity":
                car.get(
                    "rarity",
                    ""
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


                "image":
                car.get(
                    "image",
                    ""
                )

            }

        )



    return result







# =========================
# GET MAIN CAR
# =========================


def get_main_car(user_id):


    player = get_player(

        user_id

    )


    car_name = player.get(

        "main_car"

    )



    if not car_name:


        return None





    return get_car(

        car_name

    )







# =========================
# MAIN CAR DATA
# =========================


def get_main_car_card(user_id):


    car = get_main_car(

        user_id

    )



    if not car:


        return {


            "name":

            "Нет машины",


            "power":

            0,


            "speed":

            0,


            "handling":

            0

        }






    return {


        "name":

        car["name"],


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


        "image":

        car.get(
            "image",
            ""
        )

    }








# =========================
# ADD CAR
# =========================


def add_car_to_garage(

    user_id,

    car_name

):


    return add_car(

        user_id,

        car_name

    )
    
    
    # =========================
# REMOVE CAR
# =========================


def remove_car_from_garage(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    garage = player.get(

        "garage",

        []

    )



    if car_name not in garage:


        return {

            "success":False,

            "text":"❌ Машины нет в гараже"

        }






    if player.get(

        "main_car"

    ) == car_name:


        return {

            "success":False,

            "text":

            "❌ Нельзя удалить главную машину"

        }







    remove_car(

        user_id,

        car_name

    )



    return {

        "success":True,

        "text":

        f"🚗 {car_name} удалена"

    }








# =========================
# SET MAIN CAR
# =========================


def set_main_car(

    user_id,

    car_name

):


    garage = get_garage(

        user_id

    )



    if car_name not in garage:


        return {

            "success":False,

            "text":

            "❌ Машина отсутствует"

        }







    db_set_main_car(

        user_id,

        car_name

    )



    return {

        "success":True,

        "text":

        f"""

👑 Главная машина:


{car_name}

"""

    }








# =========================
# CAR STATS
# =========================


def get_car_stats(

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


        return None






    car = get_car(

        car_name

    )



    if not car:


        return None





    return {


        "name":

        car["name"],


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


        "acceleration":

        car.get(

            "acceleration",

            0

        ),


        "nitro":

        car.get(

            "nitro",

            0

        )

    }








# =========================
# COMPARE CARS
# =========================


def compare_cars(

    user_id,

    first,

    second

):


    car1 = get_car_stats(

        user_id,

        first

    )


    car2 = get_car_stats(

        user_id,

        second

    )



    if not car1 or not car2:


        return None






    return {


        "power":

        car1["power"] -

        car2["power"],



        "speed":

        car1["speed"] -

        car2["speed"],



        "handling":

        car1["handling"] -

        car2["handling"],



        "acceleration":

        car1["acceleration"] -

        car2["acceleration"]

    }








# =========================
# GARAGE VALUE
# =========================


def get_garage_value(

    user_id

):


    garage = get_garage(

        user_id

    )


    total = 0



    for car_name in garage:


        car = get_car(

            car_name

        )


        if car:


            total += car.get(

                "price",

                0

            )



    return total








# =========================
# GARAGE COUNT
# =========================


def get_garage_count(

    user_id

):


    return len(

        get_garage(

            user_id

        )

    )








# =========================
# FULL GARAGE DATA
# MINI APP API
# =========================


def get_full_garage_data(

    user_id

):


    player = get_player(

        user_id

    )



    return {


        "count":

        get_garage_count(

            user_id

        ),



        "value":

        get_garage_value(

            user_id

        ),



        "main_car":

        player.get(

            "main_car"

        ),



        "cars":

        get_garage_cards(

            user_id

        )

    }
    
    
    # =========================
# ADD CAR SAFE
# =========================


def add_car_to_garage_safe(

    user_id,

    car_name

):

    player = get_player(

        user_id

    )


    if car_name in player.get(

        "garage",

        []

    ):

        return {

            "success": False,

            "text": "🚗 Машина уже есть"

        }



    add_car(

        user_id,

        car_name

    )


    return {

        "success": True,

        "text": f"✅ {car_name} добавлена"

    }





# =========================
# GET CAR UPGRADES
# =========================


def get_car_upgrades(

    user_id,

    car_name

):

    player = get_player(

        user_id

    )


    upgrades = player.get(

        "car_upgrades",

        {}

    )


    return upgrades.get(

        car_name,

        {}

    )







# =========================
# CAR POWER SCORE
# =========================


def get_car_power_score(

    user_id,

    car_name

):

    car = get_car(

        car_name

    )


    if not car:

        return 0



    score = (

        car.get("power",0)

        +

        car.get("speed",0)

        +

        car.get("handling",0)

        +

        car.get("nitro",0)

    )



    upgrades = get_car_upgrades(

        user_id,

        car_name

    )



    bonus = 0



    for value in upgrades.values():

        bonus += value * 25



    return score + bonus








# =========================
# RACE ACTIVE CAR
# =========================


def get_race_car(

    user_id

):

    player = get_player(

        user_id

    )


    car = player.get(

        "main_car"

    )


    if not car:

        return None



    return get_car(

        car

    )








# =========================
# FULL CAR CARD
# MINI APP
# =========================


def get_full_car_card(

    user_id,

    car_name

):

    car = get_car(

        car_name

    )


    if not car:

        return None



    return {


        "name":

        car.get("name"),


        "brand":

        car.get("brand"),


        "image":

        car.get("image"),


        "rarity":

        car.get("rarity"),


        "class":

        car.get("class"),


        "price":

        car.get("price",0),


        "stats": {


            "power":

            car.get("power",0),


            "speed":

            car.get("speed",0),


            "handling":

            car.get("handling",0),


            "nitro":

            car.get("nitro",0)

        },


        "upgrades":

        get_car_upgrades(

            user_id,

            car_name

        ),


        "battle_score":

        get_car_power_score(

            user_id,

            car_name

        )

    }