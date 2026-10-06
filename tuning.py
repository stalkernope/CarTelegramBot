import json
import os



from database import (

    get_player,

    update_player

)




TUNING_FILE = "tuning.json"




# =========================
# ДЕТАЛИ
# =========================


PARTS = {


    "engine": {

        "name": "⚡ Двигатель",

        "power": 50,

        "price": 5000

    },


    "turbo": {

        "name": "🔥 Турбо",

        "speed": 15,

        "price": 7000

    },


    "tires": {

        "name": "🛞 Шины",

        "speed": 10,

        "price": 3000

    },


    "suspension": {

        "name": "🔧 Подвеска",

        "power": 20,

        "price": 4000

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

            "suspension": 0

        }



        save_tuning(

            data

        )



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


            "success":

            False,


            "message":

            "❌ Деталь не найдена"

        }



    player = get_player(

        user_id

    )



    price = PARTS[part]["price"]



    if player["coins"] < price:


        return {


            "success":

            False,


            "message":

            "❌ Недостаточно монет"

        }




    data = load_tuning()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {}



    if car_name not in data[uid]:


        data[uid][car_name] = {


            "engine": 0,

            "turbo": 0,

            "tires": 0,

            "suspension": 0

        }




    if data[uid][car_name][part] >= 5:


        return {


            "success":

            False,


            "message":

            "❌ Максимальный уровень"

        }




    player["coins"] -= price



    data[uid][car_name][part] += 1



    update_player(

        user_id,

        player

    )



    save_tuning(

        data

    )



    return {


        "success":

        True,


        "message":


        f"✅ {PARTS[part]['name']} улучшено\n"

        f"Уровень: "

        f"{data[uid][car_name][part]}/5"

    }
    
    # =========================
# БОНУСЫ ТЮНИНГА
# =========================


def tuning_bonus(

    user_id,

    car_name

):


    tuning = get_car_tuning(

        user_id,

        car_name

    )



    power = (

        tuning.get(

            "engine",

            0

        )

        *

        PARTS["engine"]["power"]

        +

        tuning.get(

            "suspension",

            0

        )

        *

        PARTS["suspension"]["power"]

    )



    speed = (

        tuning.get(

            "turbo",

            0

        )

        *

        PARTS["turbo"]["speed"]

        +

        tuning.get(

            "tires",

            0

        )

        *

        PARTS["tires"]["speed"]

    )



    return {


        "power":

        power,


        "speed":

        speed

    }




# =========================
# ТЕКСТ ТЮНИНГА
# =========================


def tuning_text(

    user_id,

    car_name

):


    tuning = get_car_tuning(

        user_id,

        car_name

    )



    bonus = tuning_bonus(

        user_id,

        car_name

    )



    return (

        "🔧 <b>ТЮНИНГ</b>\n\n"

        f"🚗 Машина: {car_name}\n\n"

        f"⚡ Двигатель: "

        f"{tuning['engine']}/5\n"

        f"🔥 Турбо: "

        f"{tuning['turbo']}/5\n"

        f"🛞 Шины: "

        f"{tuning['tires']}/5\n"

        f"🔧 Подвеска: "

        f"{tuning['suspension']}/5\n\n"

        "📈 Бонусы:\n"

        f"⚡ Сила +{bonus['power']}\n"

        f"🚀 Скорость +{bonus['speed']}"

    )