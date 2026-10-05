import json
import os



CONDITION_FILE = "car_condition.json"




# =========================
# НАСТРОЙКИ
# =========================


MAX_CONDITION = 100



REPAIR_COST = {

    "repair":

    500,


    "service":

    1000,


    "wash":

    300

}




# =========================
# ЗАГРУЗКА
# =========================


def load_condition():

    if not os.path.exists(CONDITION_FILE):

        return {}



    try:

        with open(

            CONDITION_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_condition(data):

    with open(

        CONDITION_FILE,

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
# СОСТОЯНИЕ МАШИНЫ
# =========================


def get_condition(

    user_id,

    car_name

):

    data = load_condition()


    uid = str(user_id)



    if uid not in data:

        data[uid] = {}



    if car_name not in data[uid]:


        data[uid][car_name] = {

            "condition": 100,

            "races": 0,

            "repairs": 0

        }


        save_condition(data)



    return data[uid][car_name]




# =========================
# ИЗНОС ПОСЛЕ ГОНКИ
# =========================


def race_damage(

    user_id,

    car_name

):

    data = load_condition()


    car = get_condition(

        user_id,

        car_name

    )


    damage = 5



    car["condition"] -= damage


    car["races"] += 1



    if car["condition"] < 0:

        car["condition"] = 0



    data[str(user_id)][car_name] = car


    save_condition(data)



    return car["condition"]




# =========================
# РЕМОНТ
# =========================


def repair_car(

    user_id,

    car_name

):

    data = load_condition()


    car = get_condition(

        user_id,

        car_name

    )


    car["condition"] = 100


    car["repairs"] += 1



    data[str(user_id)][car_name] = car


    save_condition(data)



    return True




# =========================
# ОБСЛУЖИВАНИЕ
# =========================


def service_car(

    user_id,

    car_name

):

    data = load_condition()


    car = get_condition(

        user_id,

        car_name

    )


    car["condition"] += 20



    if car["condition"] > 100:

        car["condition"] = 100



    data[str(user_id)][car_name] = car


    save_condition(data)



    return car["condition"]




# =========================
# МОЙКА
# =========================


def wash_car(

    user_id,

    car_name

):

    data = load_condition()


    car = get_condition(

        user_id,

        car_name

    )


    car["condition"] += 5



    if car["condition"] > 100:

        car["condition"] = 100



    data[str(user_id)][car_name] = car


    save_condition(data)



    return car["condition"]




# =========================
# БОНУС СОСТОЯНИЯ
# =========================


def condition_bonus(

    user_id,

    car_name

):

    car = get_condition(

        user_id,

        car_name

    )


    condition = car["condition"]



    if condition >= 90:

        return 10



    if condition >= 50:

        return 0



    return -20




# =========================
# ТЕКСТ
# =========================


def condition_text(

    user_id,

    car_name

):

    car = get_condition(

        user_id,

        car_name

    )



    return (

        "🛠 <b>СОСТОЯНИЕ АВТО</b>\n\n"

        f"🚗 {car_name}\n\n"

        f"❤️ Состояние: {car['condition']}%\n"

        f"🏁 Гонок: {car['races']}\n"

        f"🔧 Ремонтов: {car['repairs']}\n\n"

        f"⚡ Бонус: {condition_bonus(user_id, car_name)}%"

    )