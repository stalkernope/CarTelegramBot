import json
import os


from database import (
    get_player,
    update_player
)



TUNING_FILE = "tuning.json"




# =========================
# ДЕТАЛИ ТЮНИНГА
# =========================


PARTS = {


    "engine": {


        "name": "⚡ Двигатель",


        "max_level": 10,


        "price": 5000,


        "bonus": {

            "power": 50

        }

    },



    "turbo": {


        "name": "🔥 Турбо",


        "max_level": 10,


        "price": 7000,


        "bonus": {

            "speed": 20

        }

    },



    "tires": {


        "name": "🛞 Шины",


        "max_level": 10,


        "price": 3000,


        "bonus": {

            "speed": 10,

            "handling": 5

        }

    },



    "suspension": {


        "name": "🔧 Подвеска",


        "max_level": 10,


        "price": 4000,


        "bonus": {

            "handling": 10

        }

    },



    "electronics": {


        "name": "🔋 Электроника",


        "max_level": 10,


        "price": 6000,


        "bonus": {

            "critical": 5

        }

    }

}




# =========================
# ЗАГРУЗКА
# =========================


def load_tuning():


    if not os.path.exists(TUNING_FILE):

        return {}



    try:


        with open(

            TUNING_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except:


        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_tuning(data):


    with open(

        TUNING_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )




# =========================
# ПОЛУЧИТЬ ТЮНИНГ
# =========================


def get_car_tuning(

    user_id,

    car_name

):


    data = load_tuning()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {}



    if car_name not in data[uid]:


        data[uid][car_name] = {


            "engine": 0,

            "turbo": 0,

            "tires": 0,

            "suspension": 0,

            "electronics": 0

        }


        save_tuning(data)



    return data[uid][car_name]




# =========================
# УЛУЧШЕНИЕ
# =========================


def upgrade_car(

    user_id,

    car_name,

    part

):


    if part not in PARTS:


        return {


            "success": False,


            "message":

            "❌ Такой детали нет"

        }




    player = get_player(

        user_id

    )



    tuning = get_car_tuning(

        user_id,

        car_name

    )



    current = tuning[part]



    config = PARTS[part]



    if current >= config["max_level"]:


        return {


            "success": False,


            "message":

            "🔥 Максимальный уровень"

        }




    price = config["price"] * (

        current + 1

    )




    if player["coins"] < price:


        return {


            "success": False,


            "message":

            "❌ Недостаточно монет"

        }




    player["coins"] -= price



    tuning[part] += 1



    update_player(

        user_id,

        player

    )



    data = load_tuning()


    data[str(user_id)][car_name] = tuning


    save_tuning(data)



    return {


        "success": True,


        "message":

        (

            f"✅ {config['name']}\n"

            f"⭐ Уровень: "

            f"{tuning[part]}/10\n"

            f"💰 Цена: {price}"

        )

    }




# =========================
# БОНУСЫ
# =========================


def tuning_bonus(

    user_id,

    car_name

):


    tuning = get_car_tuning(

        user_id,

        car_name

    )


    bonus = {


        "power": 0,

        "speed": 0,

        "handling": 0,

        "critical": 0

    }



    for part, level in tuning.items():


        config = PARTS[part]



        for stat, value in config["bonus"].items():


            bonus[stat] += value * level



    return bonus




# =========================
# ТЕКСТ
# =========================


def tuning_text(

    user_id,

    car_name

):


    tuning = get_car_tuning(

        user_id,

        car_name

    )



    text = (

        "🔧 <b>ТЮНИНГ</b>\n\n"

        f"🏎 {car_name}\n\n"

    )



    for part, level in tuning.items():


        item = PARTS[part]


        stars = "⭐" * level + "▫️" * (

            10 - level

        )



        text += (

            f"{item['name']}\n"

            f"{stars}\n"

            f"Уровень: {level}/10\n\n"

        )



    return text