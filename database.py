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

    try:

        with open(
            DATABASE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


            if isinstance(data, dict):

                return data


    except Exception as e:

        print(
            "Ошибка базы игроков:",
            e
        )


    return {}



# =========================
# СОХРАНЕНИЕ
# =========================


def save_database(data):

    try:

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

    except Exception as e:

        print(
            "Ошибка сохранения:",
            e
        )



# =========================
# НОВЫЙ ИГРОК
# =========================


def default_player():

    return {

        "level": 1,

        "xp": 0,

        "coins": 1000,

        "garage": [],

        "wins": 0,

        "losses": 0,

        "title": "🚗 Новичок"

    }



# =========================
# ПОЛУЧИТЬ ИГРОКА
# =========================


def get_player(user_id):

    data = load_database()

    uid = str(user_id)



    if uid not in data:

        data[uid] = default_player()

        save_database(data)



    return data[uid]



# =========================
# ТИТУЛЫ
# =========================


def update_title(player):

    level = player.get(
        "level",
        1
    )


    if level >= 50:

        player["title"] = "👑 Автомобильный Бог"


    elif level >= 30:

        player["title"] = "🔥 Легенда дорог"


    elif level >= 15:

        player["title"] = "💎 Коллекционер легенд"


    elif level >= 5:

        player["title"] = "🏆 Опытный владелец"


    else:

        player["title"] = "🚗 Новичок"




# =========================
# XP
# =========================


def add_xp(user_id, amount):

    data = load_database()

    uid = str(user_id)


    player = get_player(
        user_id
    )


    player["xp"] += amount



    while player["xp"] >= player["level"] * 200:


        player["xp"] -= (
            player["level"] * 200
        )


        player["level"] += 1


        player["coins"] += 500



    update_title(
        player
    )


    data[uid] = player


    save_database(
        data
    )



# =========================
# МОНЕТЫ
# =========================


def add_coins(user_id, amount):

    data = load_database()

    uid = str(user_id)


    player = get_player(
        user_id
    )


    player["coins"] += amount


    if player["coins"] < 0:

        player["coins"] = 0



    data[uid] = player


    save_database(
        data
    )



# =========================
# ГАРАЖ
# =========================


def add_car(user_id, car):

    player = get_player(
        user_id
    )


    if isinstance(car, dict):

        car = car.get(
            "name"
        )


    if not car:

        return



    if car not in player["garage"]:

        player["garage"].append(
            car
        )


        add_xp(
            user_id,
            50
        )


    data = load_database()

    data[str(user_id)] = player


    save_database(
        data
    )



# =========================
# ПРОВЕРКА МАШИНЫ
# =========================


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


    player = get_player(
        user_id
    )


    player["wins"] += 1

    player["coins"] += 100


    data[uid] = player


    save_database(
        data
    )


    add_xp(
        user_id,
        100
    )



def add_loss(user_id):

    data = load_database()

    uid = str(user_id)


    player = get_player(
        user_id
    )


    player["losses"] += 1


    data[uid] = player


    save_database(
        data
    )