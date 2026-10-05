import json
import os
import random
from datetime import datetime



DEALER_FILE = "dealer.json"



# =========================
# ЗАГРУЗКА
# =========================


def load_dealer():

    if not os.path.exists(DEALER_FILE):

        return {}


    try:

        with open(
            DEALER_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_dealer(data):

    with open(
        DEALER_FILE,
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
# СОЗДАНИЕ САЛОНА
# =========================


def generate_dealer(cars):

    today = str(
        datetime.now().date()
    )


    data = load_dealer()



    if data.get("date") == today:

        return data.get(
            "cars",
            []
        )



    available = cars.copy()


    random.shuffle(
        available
    )


    dealer_cars = available[:5]



    save_dealer(

        {

            "date": today,

            "cars": dealer_cars

        }

    )


    return dealer_cars




# =========================
# ПРЕМИУМ САЛОН
# =========================


def premium_dealer(cars):

    premium = []


    for car in cars:

        rarity = car.get(
            "rarity",
            ""
        )


        if (

            "Legendary" in rarity

            or

            "Mythic" in rarity

        ):

            premium.append(
                car
            )



    random.shuffle(
        premium
    )


    return premium[:3]




# =========================
# СЕКРЕТНЫЕ МАШИНЫ
# =========================


SECRET_CARS = [

    {

        "name":

        "McLaren F1",

        "condition":

        "100 побед"

    },


    {

        "name":

        "Ferrari F40",

        "condition":

        "50 побед"

    },


    {

        "name":

        "Lexus LFA",

        "condition":

        "Первый Mythic"

    }

]




def secret_cars_text():

    text = (

        "🕵️ <b>СЕКРЕТНЫЕ МАШИНЫ</b>\n\n"

    )



    for car in SECRET_CARS:

        text += (

            f"🔒 {car['name']}\n"

            f"Условие: {car['condition']}\n\n"

        )



    return text




# =========================
# КОЛЛЕКЦИИ
# =========================


COLLECTIONS = [

    {

        "name":

        "🇯🇵 JDM LEGENDS",

        "cars":

        [

            "Toyota Supra MK4",

            "Nissan Skyline GT-R R34",

            "Mazda RX-7 FD"

        ],

        "reward":

        "5000 🪙"

    },


    {

        "name":

        "🇮🇹 ITALIAN DREAM",

        "cars":

        [

            "Ferrari F40",

            "Lamborghini Diablo SV",

            "Pagani Zonda F"

        ],

        "reward":

        "🔥 Legendary Case"

    }

]




def collections_text():

    text = (

        "🏆 <b>КОЛЛЕКЦИИ</b>\n\n"

    )


    for collection in COLLECTIONS:


        text += (

            f"{collection['name']}\n"

            "Машины:\n"

        )


        for car in collection["cars"]:

            text += (

                "🚗 "

                +

                car

                +

                "\n"

            )


        text += (

            "🎁 Награда: "

            +

            collection["reward"]

            +

            "\n\n"

        )


    return text