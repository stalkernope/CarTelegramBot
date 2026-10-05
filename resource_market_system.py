import json
import os
import random
import time



RESOURCE_FILE = "resource_market.json"




# =========================
# РЕСУРСЫ
# =========================


RESOURCES = {


    "metal": {

        "name": "🔩 Металл",

        "price": 100

    },


    "carbon": {

        "name": "🖤 Карбон",

        "price": 500

    },


    "engine_part": {

        "name": "⚙️ Деталь двигателя",

        "price": 1000

    },


    "turbo_part": {

        "name": "🔥 Деталь турбины",

        "price": 1500

    },


    "rare_chip": {

        "name": "💎 Редкий чип",

        "price": 5000

    }

}




# =========================
# ЗАГРУЗКА
# =========================


def load_market():

    if not os.path.exists(RESOURCE_FILE):

        return {

            "prices": {},

            "players": {},

            "history": []

        }


    try:

        with open(

            RESOURCE_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {

            "prices": {},

            "players": {},

            "history": []

        }




# =========================
# СОХРАНЕНИЕ
# =========================


def save_market(data):

    with open(

        RESOURCE_FILE,

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
# ЦЕНЫ
# =========================


def update_prices():


    data = load_market()



    for resource, info in RESOURCES.items():


        old = data["prices"].get(

            resource,

            info["price"]

        )


        change = random.randint(

            -20,

            20

        )


        new_price = old + (

            old * change // 100

        )


        if new_price < 10:

            new_price = 10



        data["prices"][resource] = new_price



    save_market(data)



    return data["prices"]




# =========================
# ИНВЕНТАРЬ
# =========================


def get_inventory(user_id):

    data = load_market()


    uid = str(user_id)



    if uid not in data["players"]:


        data["players"][uid] = {

            "resources": {}

        }


        save_market(data)



    return data["players"][uid]




# =========================
# ДОБАВИТЬ РЕСУРС
# =========================


def add_resource(

    user_id,

    resource,

    amount

):

    data = load_market()


    player = get_inventory(

        user_id

    )



    if resource not in RESOURCES:

        return False



    player["resources"][resource] = (

        player["resources"].get(

            resource,

            0

        )

        +

        amount

    )



    data["players"][str(user_id)] = player


    save_market(data)



    return True




# =========================
# КУПИТЬ
# =========================


def buy_resource(

    user_id,

    resource,

    amount

):

    data = load_market()



    if resource not in RESOURCES:

        return False



    price = data["prices"].get(

        resource,

        RESOURCES[resource]["price"]

    )



    total = price * amount



    # Деньги подключим к общей экономике

    # через database / bank



    add_resource(

        user_id,

        resource,

        amount

    )



    data["history"].append(

        {

            "user":

            user_id,

            "resource":

            resource,

            "amount":

            amount,

            "price":

            total,

            "time":

            time.time()

        }

    )


    save_market(data)



    return total




# =========================
# ПРОДАТЬ
# =========================


def sell_resource(

    user_id,

    resource,

    amount

):

    data = load_market()


    player = get_inventory(

        user_id

    )



    have = player["resources"].get(

        resource,

        0

    )



    if have < amount:

        return False



    player["resources"][resource] -= amount



    price = data["prices"].get(

        resource,

        RESOURCES[resource]["price"]

    )



    reward = price * amount



    data["players"][str(user_id)] = player



    data["history"].append(

        {

            "user":

            user_id,

            "sold":

            resource,

            "amount":

            amount,

            "reward":

            reward

        }

    )


    save_market(data)



    return reward




# =========================
# ТЕКСТ
# =========================


def resource_market_text():

    data = load_market()



    text = (

        "💱 <b>РЫНОК РЕСУРСОВ</b>\n\n"

    )



    for resource, info in RESOURCES.items():


        price = data["prices"].get(

            resource,

            info["price"]

        )


        text += (

            f"{info['name']}\n"

            f"💰 Цена: {price}\n\n"

        )



    return text