import json
import os

from datetime import date


from car_database import get_random_car



DAILY_FILE = "daily_car.json"




# =========================
# ЗАГРУЗКА
# =========================


def load_daily():

    if not os.path.exists(DAILY_FILE):

        return None


    try:

        with open(
            DAILY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except Exception as e:

        print(
            "Ошибка daily_car.json:",
            e
        )

        return None




# =========================
# СОХРАНЕНИЕ
# =========================


def save_daily(data):

    try:

        with open(
            DAILY_FILE,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(

                data,

                file,

                ensure_ascii=False,

                indent=4

            )


    except Exception as e:

        print(
            "Ошибка сохранения машины дня:",
            e
        )





# =========================
# МАШИНА ДНЯ
# =========================


def get_daily_car():


    today = str(
        date.today()
    )


    daily = load_daily()



    if daily:


        if daily.get("date") == today:


            return daily.get(
                "car"
            )




    car = get_random_car()



    if not car:

        return None




    save_daily({

        "date": today,

        "car": car

    })



    return car