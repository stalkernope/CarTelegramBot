import json
import os



UPGRADE_FILE = "car_upgrades.json"




# =========================
# ЗАГРУЗКА
# =========================


def load_upgrades():

    if not os.path.exists(UPGRADE_FILE):

        return {}


    try:

        with open(
            UPGRADE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_upgrades(data):

    with open(

        UPGRADE_FILE,

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
# ДАННЫЕ МАШИНЫ
# =========================


def get_car_upgrade(

    user_id,

    car_name

):

    data = load_upgrades()


    uid = str(user_id)



    if uid not in data:

        data[uid] = {}



    if car_name not in data[uid]:


        data[uid][car_name] = {

            "level": 1,

            "power": 0,

            "speed": 0

        }


        save_upgrades(data)



    return data[uid][car_name]




# =========================
# ЦЕНА
# =========================


def upgrade_price(level):

    return level * 5000




# =========================
# УЛУЧШЕНИЕ
# =========================


def upgrade_car(

    user_id,

    player,

    car_name

):


    data = load_upgrades()


    upgrade = get_car_upgrade(

        user_id,

        car_name

    )



    level = upgrade["level"]



    if level >= 10:

        return {

            "success": False,

            "message":

            "🚫 Максимальный уровень"

        }




    price = upgrade_price(

        level

    )



    if player["money"] < price:


        return {

            "success": False,

            "message":

            "❌ Недостаточно денег"

        }




    player["money"] -= price



    upgrade["level"] += 1


    upgrade["power"] += 50


    upgrade["speed"] += 20




    data[str(user_id)][car_name] = upgrade


    save_upgrades(data)



    return {

        "success": True,

        "price": price,

        "level": upgrade["level"],

        "power": upgrade["power"],

        "speed": upgrade["speed"]

    }




# =========================
# ТЕКСТ
# =========================


def upgrade_text(

    user_id,

    car_name

):


    upgrade = get_car_upgrade(

        user_id,

        car_name

    )



    return (

        "🔧 <b>ПРОКАЧКА</b>\n\n"

        f"🚗 {car_name}\n\n"

        f"⭐ Уровень: {upgrade['level']}/10\n"

        f"⚡ Бонус мощности: +{upgrade['power']}\n"

        f"🚀 Бонус скорости: +{upgrade['speed']}"

    )