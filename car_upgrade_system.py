import json
import os



UPGRADE_FILE = "car_upgrades.json"




# =========================
# ЛИМИТЫ
# =========================


RARITY_LIMITS = {


    "🔵 Rare": 20,


    "🟣 Rare": 30,


    "💎 Legendary": 50,


    "🔥 Mythic": 70,


    "👑 Divine": 100


}




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
# ПОЛУЧИТЬ МАШИНУ
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


            "xp": 0,


            "power_bonus": 0,


            "speed_bonus": 0

        }



        save_upgrades(data)



    return data[uid][car_name]




# =========================
# ДОБАВИТЬ ОПЫТ
# =========================


def add_car_xp(

    user_id,

    car_name,

    amount

):

    data = load_upgrades()


    car = get_car_upgrade(

        user_id,

        car_name

    )



    car["xp"] += amount



    need = car["level"] * 500



    if car["xp"] >= need:


        car["xp"] -= need


        car["level"] += 1


        car["power_bonus"] += 10


        car["speed_bonus"] += 5



        level_up = True


    else:


        level_up = False




    data[str(user_id)][car_name] = car


    save_upgrades(data)



    return level_up




# =========================
# СИЛА МАШИНЫ
# =========================


def get_car_bonus(

    user_id,

    car_name

):

    car = get_car_upgrade(

        user_id,

        car_name

    )


    return {


        "power":

        car["power_bonus"],


        "speed":

        car["speed_bonus"]

    }




# =========================
# ТЕКСТ
# =========================


def car_upgrade_text(

    user_id,

    car_name

):

    car = get_car_upgrade(

        user_id,

        car_name

    )



    return (

        "🚗 <b>ПРОКАЧКА АВТО</b>\n\n"

        f"🏎 Машина: {car_name}\n"

        f"⭐ Уровень: {car['level']}\n"

        f"✨ XP: {car['xp']}\n\n"

        f"⚡ Бонус мощности: +{car['power_bonus']}\n"

        f"🚀 Бонус скорости: +{car['speed_bonus']}"

    )