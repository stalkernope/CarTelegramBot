import json
import os

from datetime import date


from car_database import (
    get_random_car
)



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



    except Exception:

        return None



# =========================
# СОХРАНЕНИЕ
# =========================


def save_daily(data):

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



# =========================
# МАШИНА ДНЯ
# =========================


def get_daily_car():


    today = str(
        date.today()
    )


    data = load_daily()



    if data:


        if data.get("date") == today:


            return data.get(
                "car"
            )



    car = get_random_car()



    if not car:

        return None



    save_daily(

        {

            "date": today,

            "car": car

        }

    )


    return car