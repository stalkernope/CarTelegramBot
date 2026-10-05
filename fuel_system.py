import json
import os



FUEL_FILE = "fuel.json"




# =========================
# ТОПЛИВО
# =========================


FUELS = {

    "normal": {

        "name": "⛽ Обычный бензин",

        "bonus": 0

    },


    "sport": {

        "name": "🔥 Спортивное топливо",

        "bonus": 5

    },


    "race": {

        "name": "🏁 Гоночное топливо",

        "bonus": 10

    },


    "nitro": {

        "name": "🚀 Nitro Fuel",

        "bonus": 20

    }

}




MAX_FUEL = 100




# =========================
# ЗАГРУЗКА
# =========================


def load_fuel():

    if not os.path.exists(FUEL_FILE):

        return {}


    try:

        with open(
            FUEL_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_fuel(data):

    with open(
        FUEL_FILE,
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


def get_car_fuel(

    user_id,

    car_name

):

    data = load_fuel()


    uid = str(user_id)



    if uid not in data:

        data[uid] = {}



    if car_name not in data[uid]:


        data[uid][car_name] = {

            "fuel": 100,

            "type": "normal"

        }


        save_fuel(data)



    return data[uid][car_name]




# =========================
# РАСХОД
# =========================


def consume_fuel(

    user_id,

    car_name

):

    data = load_fuel()


    car = get_car_fuel(

        user_id,

        car_name

    )



    if car["fuel"] <= 0:

        return False



    car["fuel"] -= 10



    if car["fuel"] < 0:

        car["fuel"] = 0



    data[str(user_id)][car_name] = car


    save_fuel(data)



    return True




# =========================
# ЗАПРАВКА
# =========================


def refuel(

    user_id,

    car_name

):

    data = load_fuel()


    car = get_car_fuel(

        user_id,

        car_name

    )


    car["fuel"] = MAX_FUEL



    data[str(user_id)][car_name] = car


    save_fuel(data)



    return True




# =========================
# ВЫБОР ТОПЛИВА
# =========================


def change_fuel_type(

    user_id,

    car_name,

    fuel_type

):

    if fuel_type not in FUELS:

        return False



    data = load_fuel()


    car = get_car_fuel(

        user_id,

        car_name

    )


    car["type"] = fuel_type



    data[str(user_id)][car_name] = car


    save_fuel(data)



    return True




# =========================
# БОНУС
# =========================


def fuel_bonus(

    user_id,

    car_name

):

    car = get_car_fuel(

        user_id,

        car_name

    )


    return FUELS[

        car["type"]

    ]["bonus"]




# =========================
# ТЕКСТ
# =========================


def fuel_text(

    user_id,

    car_name

):

    car = get_car_fuel(

        user_id,

        car_name

    )


    fuel = FUELS[

        car["type"]

    ]



    return (

        "⛽ <b>ТОПЛИВО</b>\n\n"

        f"🚗 {car_name}\n\n"

        f"⛽ Бак: {car['fuel']}%\n"

        f"🔥 Тип: {fuel['name']}\n"

        f"⚡ Бонус: +{fuel['bonus']}%"

    )