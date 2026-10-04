import json
import os


DATABASE_FILE = "players.json"



# =========================
# СОЗДАНИЕ БАЗЫ
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



# =========================
# ЗАГРУЗКА
# =========================


def load_database():

    create_database()

    with open(
        DATABASE_FILE,
        encoding="utf-8"
    ) as file:

        return json.load(file)



# =========================
# СОХРАНЕНИЕ
# =========================


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

            "title": "Новичок"

        }


        save_database(data)



    return data[uid]



# =========================
# XP
# =========================


def add_xp(user_id, amount):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    player["xp"] += amount



    needed = player["level"] * 200


    if player["xp"] >= needed:

        player["level"] += 1

        player["coins"] += 500



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

        player["xp"] += 50



    data[uid] = player


    save_database(data)



# =========================
# БИТВЫ
# =========================


def add_win(user_id):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    player["wins"] += 1

    player["xp"] += 100

    player["coins"] += 100



    data[uid] = player


    save_database(data)



def add_loss(user_id):

    data = load_database()

    uid = str(user_id)


    player = get_player(user_id)


    player["losses"] += 1


    data[uid] = player


    save_database(data)