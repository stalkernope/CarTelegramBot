import json
import os



TITLE_FILE = "titles.json"




# =========================
# ТИТУЛЫ
# =========================


TITLES = [

    {

        "id": "rookie",

        "name": "🏁 Новичок",

        "need": 0,

        "type": "points",

        "rarity": "Common"

    },


    {

        "id": "street",

        "name": "🔥 Уличный гонщик",

        "need": 500,

        "type": "points",

        "rarity": "Rare"

    },


    {

        "id": "collector",

        "name": "🚗 Коллекционер",

        "need": 2000,

        "type": "points",

        "rarity": "Epic"

    },


    {

        "id": "champion",

        "name": "🏆 Чемпион трассы",

        "need": 5000,

        "type": "points",

        "rarity": "Legendary"

    },


    {

        "id": "legend",

        "name": "👑 Легенда CAR LEGENDS",

        "need": 20000,

        "type": "points",

        "rarity": "Mythic"

    }

]




# =========================
# РАМКИ
# =========================


FRAMES = [

    {

        "id": "bronze",

        "name": "🥉 Bronze Frame",

        "need": 0

    },


    {

        "id": "gold",

        "name": "🥇 Gold Frame",

        "need": 5000

    },


    {

        "id": "fire",

        "name": "🔥 Fire Frame",

        "need": 10000

    },


    {

        "id": "legend",

        "name": "👑 Legend Frame",

        "need": 50000

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_titles():

    if not os.path.exists(TITLE_FILE):

        return {}


    try:

        with open(

            TITLE_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_titles(data):

    with open(

        TITLE_FILE,

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


def get_titles(user_id):

    data = load_titles()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "points": 0,

            "titles": [

                "rookie"

            ],

            "active":

            "rookie",

            "frame":

            "bronze"

        }


        save_titles(data)



    return data[uid]




# =========================
# ДОБАВИТЬ ОЧКИ
# =========================


def add_title_points(

    user_id,

    amount

):

    data = load_titles()


    player = get_titles(

        user_id

    )


    player["points"] += amount



    for title in TITLES:


        if player["points"] >= title["need"]:


            if title["id"] not in player["titles"]:


                player["titles"].append(

                    title["id"]

                )



    data[str(user_id)] = player


    save_titles(data)




# =========================
# ВЫБОР ТИТУЛА
# =========================


def set_title(

    user_id,

    title_id

):

    data = load_titles()


    player = get_titles(

        user_id

    )



    if title_id not in player["titles"]:

        return False



    player["active"] = title_id



    data[str(user_id)] = player


    save_titles(data)



    return True




# =========================
# РАМКА
# =========================


def set_frame(

    user_id,

    frame_id

):

    data = load_titles()


    player = get_titles(

        user_id

    )


    player["frame"] = frame_id



    data[str(user_id)] = player


    save_titles(data)




# =========================
# ТЕКСТ
# =========================


def title_text(user_id):

    player = get_titles(

        user_id

    )


    active = "rookie"



    for title in TITLES:


        if title["id"] == player["active"]:

            active = title["name"]



    return (

        "🪪 <b>ПРОФИЛЬНЫЙ СТАТУС</b>\n\n"

        f"⭐ Очки: {player['points']}\n"

        f"🏆 Титул: {active}\n"

        f"🖼 Рамка: {player['frame']}"

    )