import json
import os



LEGEND_FILE = "legendary_cars.json"




# =========================
# ЛЕГЕНДАРНЫЕ МАШИНЫ
# =========================


LEGENDARY_CARS = [

    {

        "id": "shadow_x",

        "name": "🌑 Shadow X",

        "rarity": "Legendary",

        "power": 8000,

        "speed": 420,

        "condition":

        "Победить Night King"

    },


    {

        "id": "dragon_gt",

        "name": "🐉 Dragon GT",

        "rarity": "Mythic",

        "power": 12000,

        "speed": 480,

        "condition":

        "Победить 100 боссов"

    },


    {

        "id": "future_one",

        "name": "🚀 Future One",

        "rarity": "Secret",

        "power": 20000,

        "speed": 550,

        "condition":

        "Открыть все регионы"

    },


    {

        "id": "ultimate_zero",

        "name": "👑 Ultimate Zero",

        "rarity": "Divine",

        "power": 30000,

        "speed": 600,

        "condition":

        "Стать легендой сезона"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_legends():

    if not os.path.exists(LEGEND_FILE):

        return {}



    try:

        with open(

            LEGEND_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_legends(data):

    with open(

        LEGEND_FILE,

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
# ПРОФИЛЬ
# =========================


def get_legend_player(user_id):

    data = load_legends()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "cars": [],

            "discoveries": 0

        }


        save_legends(data)



    return data[uid]




# =========================
# ОТКРЫТЬ МАШИНУ
# =========================


def unlock_legend_car(

    user_id,

    car_id

):

    data = load_legends()


    player = get_legend_player(

        user_id

    )



    car = None



    for item in LEGENDARY_CARS:


        if item["id"] == car_id:

            car = item



    if not car:

        return False



    if car_id in player["cars"]:

        return False



    player["cars"].append(

        car_id

    )


    player["discoveries"] += 1



    data[str(user_id)] = player


    save_legends(data)



    return car




# =========================
# СПИСОК
# =========================


def legendary_cars_text(user_id):

    player = get_legend_player(

        user_id

    )


    text = (

        "👑 <b>ЛЕГЕНДАРНЫЕ АВТО</b>\n\n"

    )



    for car in LEGENDARY_CARS:


        if car["id"] in player["cars"]:

            status = "✅"

        else:

            status = "🔒"



        text += (

            f"{status} {car['name']}\n"

            f"💎 Редкость: {car['rarity']}\n"

            f"⚡ Мощность: {car['power']}\n"

            f"🏎 Скорость: {car['speed']}\n"

            f"🔑 Условие: {car['condition']}\n\n"

        )



    return text