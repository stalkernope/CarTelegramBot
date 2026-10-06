from database import (
    get_player,
    update_player,
    remove_coins
)





# =========================
# TUNING PARTS
# =========================


TUNING_PARTS = {


    "engine_1": {

        "name": "⚡ Stage 1 Engine",

        "price": 5000,

        "power": 300,

        "speed": 20

    },


    "engine_2": {

        "name": "🔥 Stage 2 Engine",

        "price": 15000,

        "power": 800,

        "speed": 50

    },


    "turbo": {

        "name": "🚀 Turbo",

        "price": 25000,

        "power": 1200,

        "speed": 80

    },


    "race_kit": {

        "name": "🏎 Race Kit",

        "price": 50000,

        "power": 2000,

        "speed": 120

    }

}








# =========================
# GET PARTS
# =========================


def get_tuning_parts():


    return TUNING_PARTS








# =========================
# BUY TUNING
# =========================


def buy_tuning(

    user_id,

    part_id

):


    if part_id not in TUNING_PARTS:


        raise Exception(

            "Деталь не найдена"

        )



    part = TUNING_PARTS[part_id]



    player = get_player(

        user_id

    )





    if part_id in player["tuning_parts"]:


        raise Exception(

            "Деталь уже установлена"

        )





    if player["coins"] < part["price"]:


        raise Exception(

            "Недостаточно монет"

        )





    remove_coins(

        user_id,

        part["price"]

    )





    player["tuning_parts"].append(

        part_id

    )



    update_player(

        user_id,

        player

    )



    return part








# =========================
# BONUS
# =========================


def tuning_bonus(

    user_id,

    car_name=None

):


    player = get_player(

        user_id

    )



    power = 0

    speed = 0





    for part_id in player.get(

        "tuning_parts",

        []

    ):



        part = TUNING_PARTS.get(

            part_id

        )



        if part:


            power += part["power"]


            speed += part["speed"]






    return {


        "power": power,


        "speed": speed


    }
    
    # =========================
# TUNING TEXT
# =========================

def tuning_text(user_id):

    from database import get_player


    player = get_player(user_id)


    parts = player.get(
        "tuning_parts",
        []
    )


    text = (
        "🔧 <b>ТЮНИНГ</b>\n\n"
    )


    if not parts:

        text += (
            "❌ Установленных деталей нет\n\n"
        )

    else:

        text += (
            "Установлено:\n\n"
        )


        for part in parts:

            text += (
                f"⚙️ {part}\n"
            )


    text += (
        "\n💪 Улучшай машину и побеждай!"
    )


    return text