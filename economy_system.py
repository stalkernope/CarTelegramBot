import json
import os
from datetime import datetime


from database import (
    get_player,
    update_player,
    add_coins,
    add_xp
)



ECONOMY_FILE = "economy.json"




# =========================
# ЗАГРУЗКА
# =========================


def load_data():

    if not os.path.exists(ECONOMY_FILE):

        return {}


    try:

        with open(
            ECONOMY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_data(data):

    with open(
        ECONOMY_FILE,
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
# ЕЖЕДНЕВНАЯ НАГРАДА
# =========================


def daily_reward(user_id):

    data = load_data()


    uid = str(user_id)


    today = str(
        datetime.now().date()
    )



    if uid not in data:

        data[uid] = {

            "daily": "",

            "streak": 0,

            "bank": 0

        }



    if data[uid]["daily"] == today:

        return {

            "success": False,

            "message":
            "🎁 Награда уже получена"

        }



    if data[uid]["daily"]:

        data[uid]["streak"] += 1

    else:

        data[uid]["streak"] = 1



    data[uid]["daily"] = today



    reward = (

        500

        +

        data[uid]["streak"] * 100

    )



    save_data(
        data
    )


    add_coins(

        user_id,

        reward

    )


    add_xp(

        user_id,

        50

    )



    return {

        "success": True,

        "coins": reward,

        "streak":

        data[uid]["streak"]

    }




# =========================
# БАНК
# =========================


def deposit(
    user_id,
    amount
):

    player = get_player(
        user_id
    )


    if player["coins"] < amount:

        return False



    player["coins"] -= amount



    update_player(

        user_id,

        player

    )



    data = load_data()


    uid = str(user_id)



    if uid not in data:

        data[uid] = {

            "daily": "",

            "streak": 0,

            "bank": 0

        }



    data[uid]["bank"] += amount



    save_data(
        data
    )



    return True




def withdraw(
    user_id,
    amount
):

    data = load_data()


    uid = str(user_id)



    if uid not in data:

        return False



    if data[uid]["bank"] < amount:

        return False



    data[uid]["bank"] -= amount



    save_data(
        data
    )



    add_coins(

        user_id,

        amount

    )


    return True




# =========================
# БАЛАНС БАНКА
# =========================


def bank_balance(user_id):

    data = load_data()


    return data.get(

        str(user_id),

        {}

    ).get(

        "bank",

        0

    )




# =========================
# ЕЖЕДНЕВНЫЕ ЗАДАНИЯ
# =========================


QUESTS = [

    {

        "id": "battle_3",

        "name":
        "⚔️ Выиграть 3 битвы",

        "reward":
        3000

    },


    {

        "id": "open_case",

        "name":
        "🎁 Открыть кейс",

        "reward":
        1000

    },


    {

        "id": "collect_car",

        "name":
        "🚗 Получить машину",

        "reward":
        500

    }

]




def quests_text():

    text = (

        "📜 <b>ЗАДАНИЯ</b>\n\n"

    )


    for quest in QUESTS:

        text += (

            quest["name"]

            +

            "\n💰 Награда: "

            +

            str(
                quest["reward"]
            )

            +

            " 🪙\n\n"

        )


    return text