import json
import os
from datetime import datetime, timedelta



DAILY_FILE = "daily_rewards.json"




# =========================
# НАГРАДЫ
# =========================


REWARDS = [

    {
        "day": 1,

        "reward":
        "💰 1000 монет"

    },


    {
        "day": 2,

        "reward":
        "🔩 5 металла"

    },


    {
        "day": 3,

        "reward":
        "🎁 Обычный кейс"

    },


    {
        "day": 7,

        "reward":
        "🔥 Rare Case"

    },


    {
        "day": 14,

        "reward":
        "💎 Epic Parts"

    },


    {
        "day": 30,

        "reward":
        "👑 Legendary Car"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_daily():

    if not os.path.exists(DAILY_FILE):

        return {}


    try:

        with open(

            DAILY_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_daily(data):

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




# =========================
# ПРОФИЛЬ
# =========================


def get_daily_player(user_id):

    data = load_daily()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "streak": 0,

            "last_claim": None,

            "total_claims": 0

        }


        save_daily(data)



    return data[uid]




# =========================
# ПОЛУЧИТЬ НАГРАДУ
# =========================


def claim_daily(user_id):

    data = load_daily()


    player = get_daily_player(

        user_id

    )


    uid = str(user_id)



    today = datetime.now().date()



    if player["last_claim"]:


        last = datetime.strptime(

            player["last_claim"],

            "%Y-%m-%d"

        ).date()



        if last == today:

            return {

                "success":

                False,

                "message":

                "⏳ Сегодня уже получено"

            }



        if today - last == timedelta(days=1):

            player["streak"] += 1


        else:

            player["streak"] = 1



    else:


        player["streak"] = 1



    player["last_claim"] = str(today)

    player["total_claims"] += 1




    reward = None



    for item in REWARDS:


        if item["day"] == player["streak"]:


            reward = item["reward"]



    if not reward:


        reward = "💰 500 монет"




    data[uid] = player


    save_daily(data)



    return {

        "success":

        True,


        "streak":

        player["streak"],


        "reward":

        reward

    }




# =========================
# ТЕКСТ
# =========================


def daily_text(user_id):

    player = get_daily_player(

        user_id

    )


    return (

        "🎁 <b>ЕЖЕДНЕВНАЯ НАГРАДА</b>\n\n"

        f"🔥 Серия дней: {player['streak']}\n"

        f"📦 Получено наград: {player['total_claims']}\n\n"

        "Заходи каждый день и получай бонусы!"

    )