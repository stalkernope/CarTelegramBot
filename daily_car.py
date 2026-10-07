# =========================
# DAILY CAR SYSTEM FINAL
# =========================


import random
import datetime



from database import (
    get_player,
    update_player
)


from car_database import (
    get_all_cars
)







# =========================
# DAILY CONFIG
# =========================


DAILY_REWARD = {


    "coins":

    1000,


    "gems":

    5

}








# =========================
# GET TODAY
# =========================


def today():


    return str(

        datetime.date.today()

    )








# =========================
# AVAILABLE CARS
# =========================


def get_daily_car():


    cars = get_all_cars()



    if not cars:


        return None



    return random.choice(

        cars

    )









# =========================
# CLAIM DAILY CAR
# =========================


def claim_daily_car(user_id):


    player = get_player(

        user_id

    )



    current_day = today()



    daily = player.get(

        "daily_car",

        {}

    )





    if daily.get(

        "date"

    ) == current_day:


        return {


            "success":

            False,


            "message":

            "🚗 Машина уже получена сегодня"

        }







    car = get_daily_car()



    if not car:


        return {


            "success":

            False,


            "message":

            "Нет доступных машин"

        }







    if "garage" not in player:


        player["garage"] = []






    if car["name"] not in player["garage"]:


        player["garage"].append(

            car["name"]

        )





    if not player.get(

        "main_car"

    ):


        player["main_car"] = car["name"]







    player["daily_car"] = {


        "date":

        current_day,


        "car":

        car["name"]

    }





    player["coins"] += DAILY_REWARD["coins"]



    player["gems"] += DAILY_REWARD["gems"]





    update_player(

        user_id,

        player

    )





    return {


        "success":

        True,


        "car":

        car,


        "coins":

        DAILY_REWARD["coins"],


        "gems":

        DAILY_REWARD["gems"]

    }








# =========================
# DAILY TEXT
# =========================


def daily_car_text(user_id):


    player = get_player(

        user_id

    )



    daily = player.get(

        "daily_car",

        {}

    )



    if daily.get(

        "date"

    ) == today():


        return f"""

🚗 <b>ЕЖЕДНЕВНАЯ МАШИНА</b>


Сегодня уже получено:


🏎 {daily.get('car')}


Возвращайся завтра.

"""





    return """

🚗 <b>ЕЖЕДНЕВНАЯ МАШИНА</b>


🎁 Бесплатный автомобиль каждый день


💰 +1000 монет

💎 +5 кристаллов


Жми получить!

"""