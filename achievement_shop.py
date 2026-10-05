import json
import os



SHOP_FILE = "achievement_shop.json"




# =========================
# ТОВАРЫ
# =========================


SHOP_ITEMS = [

    {

        "id": "gold_plate",

        "name":
        "🏆 Золотой номер",

        "price":
        10,

        "type":
        "profile"

    },


    {

        "id": "legend_case",

        "name":
        "🔥 Легендарный кейс",

        "price":
        25,

        "type":
        "case"

    },


    {

        "id": "vip_car",

        "name":
        "🚗 VIP автомобиль",

        "price":
        50,

        "type":
        "car"

    },


    {

        "id": "mythic_car",

        "name":
        "👑 Секретная Mythic машина",

        "price":
        100,

        "type":
        "car"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_shop():

    if not os.path.exists(SHOP_FILE):

        return {}



    try:

        with open(
            SHOP_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




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
# ПРОФИЛЬ МАГАЗИНА
# =========================


def get_shop_player(user_id):

    data = load_shop()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "points": 0,

            "bought": []

        }


        save_shop(
            data
        )



    return data[uid]




# =========================
# ДОБАВИТЬ ОЧКИ
# =========================


def add_points(
    user_id,
    amount
):

    data = load_shop()


    uid = str(user_id)



    player = get_shop_player(
        user_id
    )


    player["points"] += amount


    data[uid] = player


    save_shop(
        data
    )




# =========================
# ПОКУПКА
# =========================


def buy_item(
    user_id,
    item_id
):

    data = load_shop()


    player = get_shop_player(
        user_id
    )


    item = None



    for shop_item in SHOP_ITEMS:


        if shop_item["id"] == item_id:

            item = shop_item



    if not item:

        return {

            "success":

            False,

            "message":

            "❌ Предмет не найден"

        }




    if item_id in player["bought"]:

        return {

            "success":

            False,

            "message":

            "❌ Уже куплено"

        }




    if player["points"] < item["price"]:

        return {

            "success":

            False,

            "message":

            "❌ Недостаточно очков"

        }




    player["points"] -= item["price"]


    player["bought"].append(
        item_id
    )


    data[str(user_id)] = player


    save_shop(
        data
    )



    return {

        "success":

        True,

        "item":

        item["name"]

    }




# =========================
# ТЕКСТ
# =========================


def achievement_shop_text(user_id):

    player = get_shop_player(
        user_id
    )


    text = (

        "🏪 <b>ACHIEVEMENT SHOP</b>\n\n"

        f"⭐ Очки: {player['points']}\n\n"

    )



    for item in SHOP_ITEMS:


        status = "✅" if item["id"] in player["bought"] else "🔒"



        text += (

            f"{status} {item['name']}\n"

            f"Цена: {item['price']} ⭐\n\n"

        )



    return text