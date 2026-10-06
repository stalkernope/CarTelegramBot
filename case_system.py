import random
import json
import os


from database import (
    get_player,
    update_player
)


from garage_system import (
    add_car_to_garage
)


from pet_system import (
    add_pet
)




CASE_FILE = "cases_history.json"




# =========================
# КЕЙСЫ
# =========================


CASES = {


    "normal": {


        "name": "📦 Обычный кейс",

        "price": 1000,


        "rewards": [

            {

                "type": "coins",

                "amount": 2000,

                "chance": 40

            },


            {

                "type": "car",

                "id": "Honda Civic",

                "chance": 30

            },


            {

                "type": "part",

                "id": "engine",

                "chance": 30

            }

        ]

    },



    "premium": {


        "name": "💎 Премиум кейс",

        "price": 5000,


        "rewards": [

            {

                "type": "coins",

                "amount": 10000,

                "chance": 30

            },


            {

                "type": "car",

                "id": "BMW M3",

                "chance": 35

            },


            {

                "type": "pet",

                "id": "speed_hawk",

                "chance": 35

            }

        ]

    },



    "legendary": {


        "name": "🔥 Легендарный кейс",

        "price": 15000,


        "rewards": [

            {

                "type": "car",

                "id": "Bugatti X",

                "chance": 40

            },


            {

                "type": "pet",

                "id": "fire_dragon",

                "chance": 30

            },


            {

                "type": "coins",

                "amount": 50000,

                "chance": 30

            }

        ]

    }

}

# =========================
# ИСТОРИЯ КЕЙСОВ
# =========================


def load_history():


    if not os.path.exists(CASE_FILE):


        return {}



    try:


        with open(

            CASE_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except:


        return {}




def save_history(data):


    with open(

        CASE_FILE,

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
# ВЫБОР НАГРАДЫ
# =========================


def random_reward(case_id):


    case = CASES.get(

        case_id

    )



    if not case:


        return None



    rewards = case["rewards"]



    roll = random.randint(

        1,

        100

    )


    current = 0



    for reward in rewards:


        current += reward["chance"]



        if roll <= current:


            return reward



    return rewards[-1]




# =========================
# ОТКРЫТИЕ КЕЙСА
# =========================


def open_case(

    user_id,

    case_id

):


    if case_id not in CASES:


        return {


            "success": False,


            "message":

            "❌ Такой кейс не найден"

        }




    player = get_player(

        user_id

    )



    case = CASES[case_id]



    if player["coins"] < case["price"]:


        return {


            "success": False,


            "message":

            "❌ Недостаточно монет"

        }




    player["coins"] -= case["price"]



    reward = random_reward(

        case_id

    )



    text = ""




    if reward["type"] == "coins":


        player["coins"] += reward["amount"]


        text = (

            f"💰 Монеты +"

            f"{reward['amount']}"

        )




    elif reward["type"] == "car":


        add_car_to_garage(

            user_id,

            reward["id"]

        )


        text = (

            f"🚗 Получена машина:\n"

            f"{reward['id']}"

        )




    elif reward["type"] == "pet":


        add_pet(

            user_id,

            reward["id"]

        )


        text = (

            f"🐾 Получен питомец:\n"

            f"{reward['id']}"

        )




    elif reward["type"] == "part":


        if "parts" not in player:


            player["parts"] = []



        player["parts"].append(

            reward["id"]

        )


        text = (

            f"🧩 Получена деталь:\n"

            f"{reward['id']}"

        )




    update_player(

        user_id,

        player

    )



    save_case_history(

        user_id,

        case_id,

        reward

    )



    return {


        "success": True,


        "message":

        (

            f"🎁 <b>{case['name']}</b>\n\n"

            f"{text}"

        )

    }




# =========================
# СОХРАНЕНИЕ ОТКРЫТИЯ
# =========================


def save_case_history(

    user_id,

    case_id,

    reward

):


    data = load_history()


    uid = str(user_id)



    if uid not in data:


        data[uid] = []



    data[uid].append(

        {

            "case":

            case_id,


            "reward":

            reward

        }

    )



    save_history(

        data

    )
    
    # =========================
# ТЕКСТ КЕЙСОВ
# =========================


def cases_text():


    return (

        "🎁 <b>КЕЙСЫ</b>\n\n"

        "📦 Обычный кейс\n"

        "💰 Цена: 1000\n\n"

        "💎 Премиум кейс\n"

        "💰 Цена: 5000\n\n"

        "🔥 Легендарный кейс\n"

        "💰 Цена: 15000\n\n"

        "Открывай и получай:\n"

        "🚗 Машины\n"

        "🐾 Питомцев\n"

        "🧩 Детали\n"

        "💎 Валюту"

    )




# =========================
# СПИСОК КЕЙСОВ
# =========================


def get_cases():


    result = []



    for key, value in CASES.items():


        result.append(

            {

                "id": key,

                "name": value["name"],

                "price": value["price"]

            }

        )



    return result




# =========================
# ИСТОРИЯ ИГРОКА
# =========================


def get_case_history(user_id):


    data = load_history()



    return data.get(

        str(user_id),

        []

    )




# =========================
# ТЕКСТ ИСТОРИИ
# =========================


def history_text(user_id):


    history = get_case_history(

        user_id

    )


    text = (

        "🎁 <b>ИСТОРИЯ КЕЙСОВ</b>\n\n"

    )



    if not history:


        return text + "Пока ничего не открыто"



    for item in history[-10:]:


        reward = item["reward"]



        text += (

            f"📦 {item['case']}\n"

            f"🎉 {reward['type']}\n\n"

        )



    return text