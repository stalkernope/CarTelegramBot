# =========================
# TUNING FINAL COMPLETE
# CAR LEGENDS
# =========================


from database import (
    get_player,
    update_player,
    remove_coins
)


from car_database import (
    get_car
)







# =========================
# CONFIG
# =========================


MAX_LEVEL = 10



UPGRADES = {


    "engine": {


        "name": "⚡ Двигатель",

        "stat": "power",

        "bonus": 50,

        "base_price": 5000

    },



    "turbo": {


        "name": "🚀 Турбо",

        "stat": "speed",

        "bonus": 40,

        "base_price": 6000

    },



    "nitro": {


        "name": "🔥 NOS",

        "stat": "nitro",

        "bonus": 35,

        "base_price": 7000

    },



    "brakes": {


        "name": "🛑 Тормоза",

        "stat": "handling",

        "bonus": 25,

        "base_price": 4000

    },



    "handling": {


        "name": "🎯 Управление",

        "stat": "handling",

        "bonus": 40,

        "base_price": 5500

    }

}








# =========================
# GET PLAYER TUNING
# =========================


def get_tuning_data(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    tuning = player.get(

        "car_upgrades",

        {}

    )



    if car_name not in tuning:


        tuning[car_name] = {}



    return tuning[car_name]
    
    
    # =========================
# GET UPGRADE PRICE
# =========================


def get_upgrade_price(

    user_id,

    car_name,

    upgrade

):


    tuning = get_tuning_data(

        user_id,

        car_name

    )



    level = tuning.get(

        upgrade,

        0

    )



    if upgrade not in UPGRADES:


        return 0





    data = UPGRADES[upgrade]



    return data["base_price"] * (level + 1)








# =========================
# UPGRADE CAR
# =========================


def upgrade_car(

    user_id,

    car_name,

    upgrade

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

            "text":

            "❌ Машины нет в гараже"

        }






    if upgrade not in UPGRADES:


        return {


            "success":False,

            "text":

            "❌ Такой модификации нет"

        }







    tuning = get_tuning_data(

        user_id,

        car_name

    )



    current_level = tuning.get(

        upgrade,

        0

    )



    if current_level >= MAX_LEVEL:


        return {


            "success":False,

            "text":

            "🔒 Максимальный уровень"

        }








    price = get_upgrade_price(

        user_id,

        car_name,

        upgrade

    )






    if player["coins"] < price:


        return {


            "success":False,

            "text":

            "💰 Недостаточно монет"

        }







    remove_coins(

        user_id,

        price

    )



    player = get_player(

        user_id

    )



    if car_name not in player["car_upgrades"]:


        player["car_upgrades"][car_name] = {}





    player["car_upgrades"][car_name][upgrade] = current_level + 1



    update_player(

        user_id,

        player

    )





    return {


        "success":True,


        "text":f"""

🔧 Улучшение установлено!


🚗 {car_name}


{UPGRADES[upgrade]['name']}


Уровень:

{current_level + 1}/{MAX_LEVEL}


💰 Цена:

{price}

"""

    }









# =========================
# GET CAR BONUS
# =========================


def get_car_bonus(

    user_id,

    car_name

):


    tuning = get_tuning_data(

        user_id,

        car_name

    )



    bonus = {


        "power":0,

        "speed":0,

        "nitro":0,

        "handling":0

    }





    for upgrade, level in tuning.items():


        if upgrade not in UPGRADES:


            continue




        data = UPGRADES[upgrade]



        stat = data["stat"]



        bonus[stat] += (

            data["bonus"]

            *

            level

        )




    return bonus








# =========================
# GET FULL TUNING CARD
# MINI APP
# =========================


def get_tuning_card(

    user_id,

    car_name

):


    car = get_car(

        car_name

    )



    if not car:


        return None






    tuning = get_tuning_data(

        user_id,

        car_name

    )



    bonus = get_car_bonus(

        user_id,

        car_name

    )



    return {


        "car":

        car_name,



        "levels":

        tuning,



        "bonus":

        bonus,



        "available":UPGRADES

    }








# =========================
# RESET TUNING
# =========================


def reset_tuning(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    if car_name in player.get(

        "car_upgrades",

        {}

    ):


        player["car_upgrades"][car_name] = {}



        update_player(

            user_id,

            player

        )



    return True