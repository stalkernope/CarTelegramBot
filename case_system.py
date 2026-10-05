import random
import json
import os



CASE_FILE = "cases.json"



# =========================
# ТИПЫ КЕЙСОВ
# =========================


CASES = {

    "normal": {

        "name": "📦 Обычный кейс",

        "price": 1000,

        "luck": 0

    },


    "rare": {

        "name": "💎 Редкий кейс",

        "price": 10000,

        "luck": 10

    },


    "legendary": {

        "name": "🔥 Легендарный кейс",

        "price": 50000,

        "luck": 25

    },


    "mythic": {

        "name": "👑 Mythic кейс",

        "price": 200000,

        "luck": 50

    }

}




# =========================
# НАСТРОЙКИ ШАНСОВ
# =========================


RARITY_CHANCE = {


    "🔵 Rare":

    60,


    "💎 Legendary":

    30,


    "🔥 Mythic":

    10

}




# =========================
# ЗАГРУЗКА
# =========================


def load_cases():

    if not os.path.exists(CASE_FILE):

        return {}


    try:

        with open(
            CASE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_cases(data):

    with open(
        CASE_FILE,
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
# ПРОГРЕСС КЕЙСОВ
# =========================


def get_case_progress(user_id):

    data = load_cases()


    uid = str(user_id)



    if uid not in data:

        data[uid] = {

            "opened": 0,

            "mythic_counter": 0

        }


        save_cases(
            data
        )



    return data[uid]




# =========================
# ВЫБОР РЕДКОСТИ
# =========================


def random_rarity(case_type):


    bonus = CASES[case_type]["luck"]



    chance = {


        "🔵 Rare":

        60 - bonus,


        "💎 Legendary":

        30 + bonus // 2,


        "🔥 Mythic":

        10 + bonus // 2

    }



    roll = random.randint(

        1,

        100

    )



    total = 0



    for rarity, value in chance.items():


        total += value


        if roll <= total:

            return rarity



    return "🔵 Rare"




# =========================
# ОТКРЫТИЕ
# =========================


def open_case_system(

    user_id,

    case_type,

    cars

):


    if case_type not in CASES:

        return None



    progress = get_case_progress(
        user_id
    )



    rarity = random_rarity(

        case_type

    )



    # гарантия Mythic

    if progress["mythic_counter"] >= 20:


        rarity = "🔥 Mythic"

        progress["mythic_counter"] = 0



    else:


        if rarity == "🔥 Mythic":

            progress["mythic_counter"] = 0

        else:

            progress["mythic_counter"] += 1



    possible = []


    for car in cars:


        if car["rarity"] == rarity:

            possible.append(
                car
            )



    if not possible:

        possible = cars



    car = random.choice(

        possible

    )



    progress["opened"] += 1



    data = load_cases()


    data[str(user_id)] = progress


    save_cases(
        data
    )



    return car




# =========================
# ТЕКСТ
# =========================


def cases_text():

    text = (

        "🎁 <b>CASE SHOP</b>\n\n"

    )


    for key, item in CASES.items():


        text += (

            f"{item['name']}\n"

            f"💰 Цена: {item['price']}\n\n"

        )


    return text