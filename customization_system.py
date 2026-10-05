import json
import os



CUSTOM_FILE = "customization.json"




# =========================
# ВАРИАНТЫ КАСТОМА
# =========================


PAINTS = [

    "⚫ Black",

    "⚪ White",

    "🔴 Red",

    "🔵 Blue",

    "🟣 Purple",

    "🌈 Chrome"

]



VINYLS = [

    "🔥 Flame",

    "⚡ Lightning",

    "🏁 Racing",

    "🐉 Dragon",

    "👑 Royal"

]



WHEELS = [

    "🏎 Sport",

    "🔥 Racing",

    "💎 Diamond",

    "👑 Luxury"

]



BODY_KITS = [

    "Stock",

    "Street",

    "Racing",

    "Legend"

]




# =========================
# ЗАГРУЗКА
# =========================


def load_custom():

    if not os.path.exists(CUSTOM_FILE):

        return {}



    try:

        with open(

            CUSTOM_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_custom(data):

    with open(

        CUSTOM_FILE,

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
# МАШИНА
# =========================


def get_car_custom(

    user_id,

    car_name

):

    data = load_custom()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {}



    if car_name not in data[uid]:


        data[uid][car_name] = {

            "paint":

            "⚫ Black",

            "vinyl":

            None,

            "wheels":

            "🏎 Sport",

            "body":

            "Stock",

            "level":

            1

        }


        save_custom(data)



    return data[uid][car_name]




# =========================
# ПОКРАСКА
# =========================


def change_paint(

    user_id,

    car_name,

    paint

):

    if paint not in PAINTS:

        return False



    data = load_custom()


    car = get_car_custom(

        user_id,

        car_name

    )


    car["paint"] = paint



    data[str(user_id)][car_name] = car


    save_custom(data)



    return True




# =========================
# ВИНИЛ
# =========================


def add_vinyl(

    user_id,

    car_name,

    vinyl

):

    if vinyl not in VINYLS:

        return False



    data = load_custom()


    car = get_car_custom(

        user_id,

        car_name

    )


    car["vinyl"] = vinyl



    data[str(user_id)][car_name] = car


    save_custom(data)



    return True




# =========================
# ДИСКИ
# =========================


def change_wheels(

    user_id,

    car_name,

    wheels

):

    if wheels not in WHEELS:

        return False



    data = load_custom()


    car = get_car_custom(

        user_id,

        car_name

    )


    car["wheels"] = wheels



    data[str(user_id)][car_name] = car


    save_custom(data)



    return True




# =========================
# ОБВЕС
# =========================


def install_bodykit(

    user_id,

    car_name,

    kit

):

    if kit not in BODY_KITS:

        return False



    data = load_custom()


    car = get_car_custom(

        user_id,

        car_name

    )


    car["body"] = kit


    car["level"] += 1



    data[str(user_id)][car_name] = car


    save_custom(data)



    return car




# =========================
# БОНУС КАСТОМА
# =========================


def customization_bonus(

    user_id,

    car_name

):

    car = get_car_custom(

        user_id,

        car_name

    )


    bonus = 0



    if car["vinyl"]:

        bonus += 5



    if car["body"] != "Stock":

        bonus += 10



    if car["paint"] == "🌈 Chrome":

        bonus += 15



    return bonus




# =========================
# ТЕКСТ
# =========================


def customization_text(

    user_id,

    car_name

):

    car = get_car_custom(

        user_id,

        car_name

    )



    return (

        "🎨 <b>КАСТОМИЗАЦИЯ</b>\n\n"

        f"🚗 {car_name}\n\n"

        f"🎨 Цвет: {car['paint']}\n"

        f"🔥 Винил: {car['vinyl']}\n"

        f"🏎 Диски: {car['wheels']}\n"

        f"🔧 Обвес: {car['body']}\n"

        f"⭐ Уровень: {car['level']}\n"

        f"⚡ Бонус: +{customization_bonus(user_id, car_name)}%"

    )