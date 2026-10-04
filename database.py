import json
import os

from config import (
    USERS_FILE,
    GARAGE_FILE,
    VOTES_FILE
)


def create_files():

    os.makedirs("data", exist_ok=True)

    files = [
        USERS_FILE,
        GARAGE_FILE,
        VOTES_FILE
    ]

    for file in files:

        if not os.path.exists(file):

            with open(
                file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    {},
                    f,
                    ensure_ascii=False,
                    indent=4
                )


def load_data(file):

    try:

        with open(
            file,
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:

        return {}



def save_data(file, data):

    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



# 👤 Создание профиля пользователя

def get_user(user_id):

    users = load_data(USERS_FILE)

    uid = str(user_id)


    if uid not in users:

        users[uid] = {

            "xp": 0,

            "coins": 100,

            "level": "🚘 Новичок",

            "votes": 0,

            "cars": [],

            "achievements": []

        }


        save_data(
            USERS_FILE,
            users
        )


    return users[uid]



# ⭐ Добавление опыта

def add_xp(user_id, amount):

    users = load_data(USERS_FILE)

    uid = str(user_id)


    if uid in users:

        users[uid]["xp"] += amount


        # повышение уровня

        xp = users[uid]["xp"]


        if xp >= 1000:

            users[uid]["level"] = "👑 Car Legend"

        elif xp >= 500:

            users[uid]["level"] = "🔥 Auto Expert"

        elif xp >= 100:

            users[uid]["level"] = "🏎 Enthusiast"


        save_data(
            USERS_FILE,
            users
        )



# 🚘 Добавить машину в гараж

def add_car(user_id, car):

    users = load_data(USERS_FILE)

    uid = str(user_id)


    if uid in users:

        if car not in users[uid]["cars"]:

            users[uid]["cars"].append(car)

            users[uid]["xp"] += 50


    save_data(
        USERS_FILE,
        users
    )



# 🏆 Получить профиль

def profile(user_id):

    users = load_data(USERS_FILE)

    return users.get(
        str(user_id),
        None
    )