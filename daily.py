import json
import os
from datetime import date

from car_database import get_random_car


DAILY_FILE = "daily_car.json"



def get_daily_car():

    today = str(date.today())


    if os.path.exists(DAILY_FILE):

        with open(
            DAILY_FILE,
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        if data.get("date") == today:

            return data["car"]



    car = get_random_car()


    data = {

        "date": today,

        "car": car

    }


    with open(
        DAILY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            data,

            f,

            ensure_ascii=False,

            indent=4

        )


    return car