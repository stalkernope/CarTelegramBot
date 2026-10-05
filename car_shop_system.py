import json
import os



SHOP_FILE = "car_shop.json"




# =========================
# МАГАЗИН
# =========================


SHOP_CARS = [

    {
        "name": "🚗 Honda Civic",

        "price": 5000,

        "power": 200,

        "speed": 220,

        "rarity": "⚪ Common"

    },


    {
        "name": "🏎 BMW M3",

        "price": 50000,

        "power": 450,

        "speed": 300,

        "rarity": "🟣 Rare"

    },


    {
        "name": "🔥 Supra MK5",

        "price": 120000,

        "power": 600,

        "speed": 350,

        "rarity": "💎 Legendary"

    },


    {
        "name": "👑 Bugatti X",

        "price": 1000000,

        "power": 1500,

        "speed": 500,

        "rarity": "🔥 Mythic"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_shop():

    if not os.path.exists(SHOP_FILE):

        save_shop(SHOP_CARS)

        return SHOP_CARS



    try:

        with open(

            SHOP_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            data = json.load(file)


            if isinstance(data, list):

                return data



    except Exception:

        pass



    return SHOP_CARS




# =========================
# СОХРАНЕНИЕ
# =========================


def save_shop(data):

    with open(

        SHOP_FILE,

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
# ТЕКСТ МАГАЗИНА
# =========================


def shop_text():

    cars = load_shop()


    text = (

        "🛒 <b>АВТОСАЛОН</b>\n\n"

    )



    for car in cars:


        text += (

            f"{car['name']}\n"

            f"💰 Цена: {car['price']}\n"

            f"⚡ Мощность: {car['power']}\n"

            f"🚀 Скорость: {car['speed']}\n"

            f"💎 Редкость: {car['rarity']}\n\n"

        )



    return text




# =========================
# НАЙТИ МАШИНУ
# =========================


def find_shop_car(name):

    cars = load_shop()



    for car in cars:


        if car["name"] == name:

            return car



    return None




# =========================
# ПОКУПКА
# =========================


def buy_shop_car(

    user_id,

    player,

    car_name

):

    car = find_shop_car(

        car_name

    )



    if not car:

        return {

            "success": False,

            "message": "❌ Машина не найдена"

        }



    if player["coins"] < car["price"]:

        return {

            "success": False,

            "message": "❌ Недостаточно денег"

        }



    if car_name in player["garage"]:

        return {

            "success": False,

            "message": "❌ Машина уже есть в гараже"

        }



    player["coins"] -= car["price"]



    player["garage"].append(

        car_name

    )



    if player["main_car"] is None:


        player["main_car"] = car_name



    return {

        "success": True,

        "car": car,

        "message":

        (

            "🛒 <b>ПОКУПКА УСПЕШНА!</b>\n\n"

            f"🚗 {car['name']}\n"

            f"💰 Потрачено: {car['price']}\n"

            f"⚡ Мощность: {car['power']}\n"

            f"🚀 Скорость: {car['speed']}"

        )

    }




# =========================
# ПРОДАЖА
# =========================


def sell_shop_car(

    player,

    car_name

):


    if car_name not in player["garage"]:

        return False



    player["garage"].remove(

        car_name

    )



    player["coins"] += 1000



    if player["main_car"] == car_name:


        player["main_car"] = (

            player["garage"][0]

            if player["garage"]

            else None

        )



    return True




# =========================
# ТЕКСТ ПОКУПКИ
# =========================


def purchase_text(car):


    return (

        "🛒 <b>НОВАЯ МАШИНА!</b>\n\n"

        f"🚗 {car['name']}\n"

        f"💎 {car['rarity']}\n"

        f"⚡ {car['power']}\n"

        f"🚀 {car['speed']}"

    )