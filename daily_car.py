import json
import os

from datetime import date


from car_database import get_random_car



DAILY_FILE = "daily_car.json"



# =========================
# ЗАГРУЗКА
# =========================


def load_daily():

    if not os.path.exists(
        DAILY_FILE
    ):

        return None


    try:

        with open(
            DAILY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


            if isinstance(data, dict):

                return data



    except Exception as e:

        print(
            "Ошибка daily:",
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
            "Ошибка сохранения daily:",
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



    # если уже есть сегодня

    if daily:


        if daily.get(
            "date"
        ) == today:


            car = daily.get(
                "car"
            )


            if car:

                return car




    # создаём новую


    car = get_random_car()



    if not car:

        return None




    save_daily({

        "date": today,

        "car": car

    })



    return car