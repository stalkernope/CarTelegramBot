# =========================
# TUNING SYSTEM FINAL
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
# DEFAULT PARTS
# =========================


TUNING_PARTS = {


    "engine": {

        "name": "Двигатель",

        "price": 1000,

        "power": 50

    },


    "turbo": {

        "name": "Турбо",

        "price": 1500,

        "speed": 30

    },


    "handling": {

        "name": "Управление",

        "price": 1200,

        "handling": 20

    }


}







# =========================
# TUNING TEXT
# =========================


def tuning_text(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )


    parts = player.get(

        "tuning_parts",

        {}

    )


    text = (

        f"🔧 <b>ТЮНИНГ</b>\n\n"

        f"🚗 {car_name}\n\n"

    )



    for key, part in TUNING_PARTS.items():


        level = parts.get(

            key,

            0

        )


        text += (

            f"{part['name']}: "

            f"Lv.{level}\n"

            f"💰 {part['price']} монет\n\n"

        )



    return text







# =========================
# GET PART LEVEL
# =========================


def get_tuning_level(

    user_id,

    part

):


    player = get_player(

        user_id

    )


    return player.get(

        "tuning_parts",

        {}

    ).get(

        part,

        0

    )








# =========================
# UPGRADE CAR
# =========================


def upgrade_car(

    user_id,

    car_name,

    part

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

            "message":
            "❌ Машина не найдена"

        }






    if part not in TUNING_PARTS:


        return {

            "success":False,

            "message":
            "❌ Деталь не найдена"

        }






    data = TUNING_PARTS[part]



    price = data["price"]



    if player.get(

        "coins",

        0

    ) < price:


        return {

            "success":False,

            "message":
            "❌ Недостаточно монет"

        }






    player["coins"] -= price




    if "tuning_parts" not in player:


        player["tuning_parts"] = {}





    player["tuning_parts"][part] = (

        player["tuning_parts"].get(

            part,

            0

        ) + 1

    )




    update_player(

        user_id,

        player

    )



    return {


        "success":True,


        "message":

        (

            f"✅ {data['name']} улучшен\n"

            f"Новый уровень: "

            f"{player['tuning_parts'][part]}"

        )

    }







# =========================
# APPLY STATS
# =========================


def apply_tuning(

    user_id,

    car

):


    player = get_player(

        user_id

    )


    parts = player.get(

        "tuning_parts",

        {}

    )



    result = dict(car)





    engine = parts.get(

        "engine",

        0

    )


    turbo = parts.get(

        "turbo",

        0

    )


    handling = parts.get(

        "handling",

        0

    )



    result["power"] = (

        result.get(

            "power",

            0

        )

        +

        engine * 50

    )



    result["speed"] = (

        result.get(

            "speed",

            0

        )

        +

        turbo * 30

    )



    result["handling"] = (

        result.get(

            "handling",

            0

        )

        +

        handling * 20

    )



    return result