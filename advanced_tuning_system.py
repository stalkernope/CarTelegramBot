import json
import os



TUNING_FILE = "advanced_tuning.json"




# =========================
# ДЕТАЛИ
# =========================


PARTS = {

    "engine": {

        "name": "⚙️ Двигатель",

        "max": 10,

        "bonus": 5

    },


    "turbo": {

        "name": "🔥 Турбина",

        "max": 10,

        "bonus": 7

    },


    "gearbox": {

        "name": "🏎 Коробка",

        "max": 10,

        "bonus": 4

    },


    "brakes": {

        "name": "🛑 Тормоза",

        "max": 10,

        "bonus": 3

    },


    "suspension": {

        "name": "🔧 Подвеска",

        "max": 10,

        "bonus": 3

    }

}




# =========================
# СБОРКИ
# =========================


BUILDS = {


    "speed": {

        "name":

        "🚀 Speed Build",

        "bonus":

        "Максимальная скорость"

    },


    "race": {

        "name":

        "🏁 Race Build",

        "bonus":

        "Баланс"

    },


    "drift": {

        "name":

        "🔥 Drift Build",

        "bonus":

        "Управление"

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
# МАШИНА
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


            "engine": 1,

            "turbo": 1,

            "gearbox": 1,

            "brakes": 1,

            "suspension": 1,

            "build":

            "race"

        }



        save_tuning(data)



    return data[uid][car_name]




# =========================
# УЛУЧШЕНИЕ
# =========================


def upgrade_part(

    user_id,

    car_name,

    part

):

    data = load_tuning()


    car = get_car_tuning(

        user_id,

        car_name

    )



    if part not in PARTS:

        return False



    if car[part] >= PARTS[part]["max"]:

        return False



    car[part] += 1



    data[str(user_id)][car_name] = car


    save_tuning(data)



    return car[part]




# =========================
# ВЫБОР СБОРКИ
# =========================


def set_build(

    user_id,

    car_name,

    build

):

    if build not in BUILDS:

        return False



    data = load_tuning()


    car = get_car_tuning(

        user_id,

        car_name

    )


    car["build"] = build



    data[str(user_id)][car_name] = car


    save_tuning(data)



    return True




# =========================
# БОНУС ТЮНИНГА
# =========================


def tuning_bonus(

    user_id,

    car_name

):

    car = get_car_tuning(

        user_id,

        car_name

    )


    bonus = 0



    for part in PARTS:


        bonus += (

            car[part]

            *

            PARTS[part]["bonus"]

        )



    return bonus




# =========================
# ТЕКСТ
# =========================


def tuning_text(

    user_id,

    car_name

):

    car = get_car_tuning(

        user_id,

        car_name

    )



    text = (

        "⚙️ <b>ТЮНИНГ</b>\n\n"

        f"🚗 {car_name}\n\n"

    )



    for part, value in car.items():


        if part in PARTS:


            text += (

                f"{PARTS[part]['name']}: "

                f"{value}/10\n"

            )



    text += (

        f"\n🏁 Сборка: {BUILDS[car['build']]['name']}\n"

        f"🔥 Бонус: +{tuning_bonus(user_id, car_name)}%"

    )



    return text