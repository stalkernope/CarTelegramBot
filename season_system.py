import json
import os
from datetime import datetime



SEASON_FILE = "season.json"




# =========================
# НАГРАДЫ СЕЗОНА
# =========================


SEASON_REWARDS = [

    {

        "level": 1,

        "reward":

        "1000 🪙"

    },


    {

        "level": 5,

        "reward":

        "💎 Rare Case"

    },


    {

        "level": 10,

        "reward":

        "🔥 Legendary Case"

    },


    {

        "level": 25,

        "reward":

        "🚗 Exclusive Car"

    },


    {

        "level": 50,

        "reward":

        "👑 Season Mythic Car"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_season():

    if not os.path.exists(SEASON_FILE):

        return {

            "number": 1,

            "players": {}

        }



    try:

        with open(

            SEASON_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {

            "number": 1,

            "players": {}

        }




# =========================
# СОХРАНЕНИЕ
# =========================


def save_season(data):

    with open(

        SEASON_FILE,

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
# ИГРОК СЕЗОНА
# =========================


def get_season_player(user_id):

    data = load_season()


    uid = str(user_id)



    if uid not in data["players"]:


        data["players"][uid] = {

            "xp": 0,

            "level": 1,

            "claimed": []

        }


        save_season(data)



    return data["players"][uid]




# =========================
# ДОБАВИТЬ XP
# =========================


def add_season_xp(

    user_id,

    amount

):

    data = load_season()


    player = get_season_player(

        user_id

    )


    uid = str(user_id)



    player["xp"] += amount



    need = (

        player["level"]

        *

        500

    )



    if player["xp"] >= need:


        player["xp"] -= need

        player["level"] += 1



    data["players"][uid] = player


    save_season(data)



    return player




# =========================
# НАГРАДЫ
# =========================


def available_rewards(user_id):

    player = get_season_player(

        user_id

    )


    rewards = []



    for reward in SEASON_REWARDS:


        if player["level"] >= reward["level"]:


            if reward["level"] not in player["claimed"]:


                rewards.append(

                    reward

                )



    return rewards




# =========================
# ЗАБРАТЬ НАГРАДУ
# =========================


def claim_reward(

    user_id,

    level

):

    data = load_season()


    uid = str(user_id)


    player = get_season_player(

        user_id

    )



    for reward in SEASON_REWARDS:


        if reward["level"] == level:


            if level in player["claimed"]:

                return False



            if player["level"] < level:

                return False



            player["claimed"].append(

                level

            )


            data["players"][uid] = player


            save_season(data)


            return reward



    return False




# =========================
# НОВЫЙ СЕЗОН
# =========================


def next_season():

    data = load_season()


    data["number"] += 1


    data["players"] = {}



    save_season(data)



    return data["number"]




# =========================
# ТЕКСТ
# =========================


def season_text(user_id):

    data = load_season()


    player = get_season_player(

        user_id

    )


    return (

        "🏁 <b>SEASON PASS</b>\n\n"

        f"🔥 Сезон: {data['number']}\n"

        f"⭐ Уровень: {player['level']}\n"

        f"✨ XP: {player['xp']}\n\n"

        "🎁 Награды доступны за уровни"

    )