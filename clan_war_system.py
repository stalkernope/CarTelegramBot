import json
import os
import random
import time



CLAN_FILE = "clan_wars.json"




# =========================
# ТЕРРИТОРИИ
# =========================


TERRITORIES = [

    {
        "id": "garage_city",

        "name": "🏙 Garage City",

        "reward": 1000

    },


    {
        "id": "night_street",

        "name": "🌃 Night Street",

        "reward": 5000

    },


    {
        "id": "speed_valley",

        "name": "🏔 Speed Valley",

        "reward": 10000

    },


    {
        "id": "legend_zone",

        "name": "👑 Legend Zone",

        "reward": 50000

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_clans():

    if not os.path.exists(CLAN_FILE):

        return {

            "clans": {},

            "territories": {}

        }



    try:

        with open(

            CLAN_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {

            "clans": {},

            "territories": {}

        }




# =========================
# СОХРАНЕНИЕ
# =========================


def save_clans(data):

    with open(

        CLAN_FILE,

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
# СОЗДАТЬ КЛАН
# =========================


def create_clan(

    user_id,

    name

):

    data = load_clans()


    uid = str(user_id)



    if uid in data["clans"]:

        return False



    data["clans"][uid] = {

        "name": name,

        "members": [

            user_id

        ],

        "points": 0,

        "wins": 0,

        "territories": []

    }



    save_clans(data)



    return True




# =========================
# ПОЛУЧИТЬ КЛАН
# =========================


def get_clan(user_id):

    data = load_clans()


    return data["clans"].get(

        str(user_id)

    )




# =========================
# ДОБАВИТЬ УЧАСТНИКА
# =========================


def join_clan(

    owner_id,

    player_id

):

    data = load_clans()


    clan = get_clan(

        owner_id

    )


    if not clan:

        return False



    if player_id not in clan["members"]:

        clan["members"].append(

            player_id

        )



    data["clans"][str(owner_id)] = clan


    save_clans(data)



    return True




# =========================
# АТАКА ТЕРРИТОРИИ
# =========================


def attack_territory(

    user_id,

    territory_id

):

    data = load_clans()


    clan = get_clan(

        user_id

    )


    if not clan:

        return False




    chance = random.randint(

        1,

        100

    )



    if chance >= 50:


        clan["wins"] += 1


        clan["points"] += 500



        if territory_id not in clan["territories"]:

            clan["territories"].append(

                territory_id

            )


        result = {

            "success": True,

            "message":

            "⚔️ Территория захвачена!"

        }



    else:


        clan["points"] += 50



        result = {

            "success": False,

            "message":

            "❌ Атака провалена"

        }




    data["clans"][str(user_id)] = clan


    save_clans(data)



    return result




# =========================
# КЛАНОВЫЙ РЕЙТИНГ
# =========================


def clan_rating():

    data = load_clans()



    clans = list(

        data["clans"].values()

    )



    clans.sort(

        key=lambda x:

        x["points"],

        reverse=True

    )



    return clans




# =========================
# ТЕКСТ
# =========================


def clan_war_text(user_id):

    clan = get_clan(

        user_id

    )


    if not clan:

        return "❌ Ты не в клане"



    return (

        "⚔️ <b>КЛАН</b>\n\n"

        f"🏴 {clan['name']}\n"

        f"👥 Участники: {len(clan['members'])}\n"

        f"🏆 Победы: {clan['wins']}\n"

        f"⭐ Очки: {clan['points']}\n"

        f"🌍 Территории: {len(clan['territories'])}"

    )