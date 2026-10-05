import json
import os



GARAGE_FILE = "garage_upgrade.json"




# =========================
# УРОВНИ ГАРАЖА
# =========================


GARAGE_LEVELS = [

    {
        "level": 1,

        "slots": 5,

        "price": 0,

        "bonus": 0
    },


    {
        "level": 2,

        "slots": 10,

        "price": 10000,

        "bonus": 5
    },


    {
        "level": 3,

        "slots": 20,

        "price": 50000,

        "bonus": 10
    },


    {
        "level": 4,

        "slots": 35,

        "price": 150000,

        "bonus": 20
    },


    {
        "level": 5,

        "slots": 60,

        "price": 500000,

        "bonus": 35
    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_garage():


    if not os.path.exists(GARAGE_FILE):

        return {}



    try:

        with open(

            GARAGE_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_garage(data):


    with open(

        GARAGE_FILE,

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
# ПРОФИЛЬ ГАРАЖА
# =========================


def get_garage(user_id):


    data = load_garage()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "level": 1,

            "workshop": 1,

            "paint": 1,

            "slots": 5

        }


        save_garage(data)



    return data[uid]




# =========================
# УЛУЧШЕНИЕ ГАРАЖА
# =========================


def upgrade_garage(

    user_id

):


    data = load_garage()


    uid = str(user_id)


    garage = get_garage(

        user_id

    )



    current = garage["level"]



    if current >= len(GARAGE_LEVELS):


        return False




    next_level = GARAGE_LEVELS[current]



    garage["level"] += 1


    garage["slots"] = next_level["slots"]



    data[uid] = garage


    save_garage(data)



    return garage




# =========================
# МАСТЕРСКАЯ
# =========================


def upgrade_workshop(

    user_id

):


    data = load_garage()


    uid = str(user_id)


    garage = get_garage(

        user_id

    )



    garage["workshop"] += 1



    if garage["workshop"] > 10:

        garage["workshop"] = 10



    data[uid] = garage


    save_garage(data)



    return garage["workshop"]




# =========================
# БОНУС ГАРАЖА
# =========================


def garage_bonus(user_id):


    garage = get_garage(

        user_id

    )


    level = garage["level"]



    return GARAGE_LEVELS[level-1]["bonus"]




# =========================
# ТЕКСТ
# =========================


def garage_upgrade_text(user_id):


    garage = get_garage(

        user_id

    )


    return (

        "🏠 <b>ТВОЙ ГАРАЖ</b>\n\n"

        f"⭐ Уровень: {garage['level']}\n"

        f"🚗 Слоты: {garage['slots']}\n"

        f"🔧 Мастерская: {garage['workshop']}\n"

        f"🎨 Покраска: {garage['paint']}\n"

        f"🔥 Бонус гаража: +{garage_bonus(user_id)}%"

    )