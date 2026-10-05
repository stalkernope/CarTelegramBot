import json
import os
import time



MARKET_FILE = "market.json"




# =========================
# ЗАГРУЗКА
# =========================


def load_market():

    if not os.path.exists(MARKET_FILE):

        return {

            "cars": [],

            "history": []

        }


    try:

        with open(

            MARKET_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {

            "cars": [],

            "history": []

        }




# =========================
# СОХРАНЕНИЕ
# =========================


def save_market(data):

    with open(

        MARKET_FILE,

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
# ВЫСТАВИТЬ МАШИНУ
# =========================


def sell_car(

    user_id,

    car_name,

    price

):

    data = load_market()



    offer = {

        "id":

        int(time.time()),


        "seller":

        user_id,


        "car":

        car_name,


        "price":

        price,


        "time":

        time.time()

    }



    data["cars"].append(

        offer

    )



    save_market(

        data

    )



    return offer




# =========================
# ПОЛУЧИТЬ РЫНОК
# =========================


def market_cars():

    data = load_market()


    return data["cars"]




# =========================
# КУПИТЬ
# =========================


def buy_market_car(

    user_id,

    offer_id

):

    data = load_market()



    offer = None



    for car in data["cars"]:


        if car["id"] == offer_id:

            offer = car

            break



    if not offer:

        return {

            "success":

            False,

            "message":

            "❌ Машина не найдена"

        }



    if offer["seller"] == user_id:


        return {

            "success":

            False,

            "message":

            "❌ Нельзя купить свою машину"

        }




    data["cars"].remove(

        offer

    )



    data["history"].append(

        {

            "buyer":

            user_id,


            "seller":

            offer["seller"],


            "car":

            offer["car"],


            "price":

            offer["price"]

        }

    )



    save_market(

        data

    )



    return {

        "success":

        True,


        "car":

        offer["car"],


        "price":

        offer["price"]

    }




# =========================
# ЦЕНА МАШИНЫ
# =========================


def calculate_price(car):


    price = car.get(

        "price",

        1000

    )



    rarity = car.get(

        "rarity",

        ""

    )



    if "Legendary" in rarity:

        price *= 2



    if "Mythic" in rarity:

        price *= 5



    return price




# =========================
# ТЕКСТ РЫНКА
# =========================


def market_text():

    cars = market_cars()



    text = (

        "🏪 <b>CAR MARKET</b>\n\n"

    )



    if not cars:

        return text + "Рынок пуст"



    for car in cars:


        text += (

            f"🚗 {car['car']}\n"

            f"💰 Цена: {car['price']}\n"

            f"🆔 ID: {car['id']}\n\n"

        )



    return text




# =========================
# ИСТОРИЯ
# =========================


def market_history():

    data = load_market()


    return data["history"]