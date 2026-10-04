import json
import os


DATABASE_FILE = "players.json"



# =========================
# БАЗА
# =========================


def create_database():

    if not os.path.exists(DATABASE_FILE):

        with open(
            DATABASE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {},
                file,
                ensure_ascii=False,
                indent=4
            )



def load_database():

    create_database()

    with open(
        DATABASE_FILE,
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_database(data):

    with open(
        DATABASE_FILE,
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
# ИГРОК
# =========================


def get_player(user_id):

    data = load_database()

    uid = str(user_id)


    if uid not in data:

        data[uid] = {

            "level": 1,

            "xp": 0,

            "coins": 100,

            "garage": [],

            "wins": 0,

            "losses": 0,

            "title": "🚗 Новичок"

        }


        save_database(data)


    return data[uid]



# =========================
# ТИТУЛЫ
# =========================


def update_title(player):

    level = player["level"]


    if level >= 50:

        player["title"] = "👑 Автомобильный Бог"


    elif level >= 25:

        player["title"] = "🔥 Легенда дорог"


    elif level >= 10:

        player["title"] = "💎 Коллекционер"


    else:

        player["title"] = "🚗 Новичок"



# =========================
# XP
# =========================


def add_xp(user_id, amount):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    player["xp"] += amount



    while player["xp"] >= player["level"] * 200:

        player["xp"] -= player["level"] * 200

        player["level"] += 1

        player["coins"] += 500



    update_title(player)


    data[uid] = player

    save_database(data)



# =========================
# МОНЕТЫ
# =========================


def add_coins(user_id, amount):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    player["coins"] += amount


    data[uid] = player


    save_database(data)



# =========================
# ГАРАЖ
# =========================


def add_car(user_id, car_name):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    if car_name not in player["garage"]:

        player["garage"].append(car_name)

        add_xp(
            user_id,
            50
        )


    data[uid] = player

    save_database(data)



def has_car(user_id, car_name):

    player = get_player(
        user_id
    )


    return car_name in player["garage"]



# =========================
# БИТВЫ
# =========================


def add_win(user_id):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    player["wins"] += 1


    player["coins"] += 100


    data[uid] = player


    save_database(data)


    add_xp(
        user_id,
        100
    )



def add_loss(user_id):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    player["losses"] += 1


    data[uid] = player


    save_database(data)