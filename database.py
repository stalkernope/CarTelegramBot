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

            return json.load(file)


    except Exception:

        return {}



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
# НОВЫЙ ИГРОК
# =========================


def create_player():

    return {

        "level": 1,

        "xp": 0,

        "coins": 1000,

        "garage": [],

        "wins": 0,

        "losses": 0,

        "title": "🚗 Новичок",

        "daily_streak": 0,

        "last_daily": "",

        "collection_value": 0

    }



# =========================
# ПОЛУЧИТЬ ИГРОКА
# =========================


def get_player(user_id):

    data = load_database()

    uid = str(user_id)



    if uid not in data:

        data[uid] = create_player()

        save_database(data)



    return data[uid]



# =========================
# СОХРАНИТЬ ИГРОКА
# =========================


def update_player(
    user_id,
    player
):

    data = load_database()

    data[str(user_id)] = player

    save_database(data)



# =========================
# ТИТУЛЫ
# =========================


def get_title(level):

    if level >= 50:

        return "👑 Автомобильный Бог"


    if level >= 25:

        return "🔥 Легенда дорог"


    if level >= 10:

        return "💎 Коллекционер"


    if level >= 5:

        return "🏆 Опытный владелец"


    return "🚗 Новичок"



# =========================
# XP
# =========================


def add_xp(
    user_id,
    amount
):

    player = get_player(
        user_id
    )


    player["xp"] += amount



    while player["xp"] >= player["level"] * 200:


        player["xp"] -= player["level"] * 200

        player["level"] += 1

        player["coins"] += 500



    player["title"] = get_title(

        player["level"]

    )



    update_player(

        user_id,

        player

    )



# =========================
# МОНЕТЫ
# =========================


def add_coins(
    user_id,
    amount
):

    player = get_player(
        user_id
    )


    player["coins"] += amount



    if player["coins"] < 0:

        player["coins"] = 0



    update_player(

        user_id,

        player

    )



# =========================
# ДОБАВИТЬ МАШИНУ
# =========================


def add_car(
    user_id,
    car_name
):

    player = get_player(
        user_id
    )


    if isinstance(car_name, dict):

        car_name = car_name.get(
            "name"
        )



    if not car_name:

        return



    if car_name not in player["garage"]:


        player["garage"].append(
            car_name
        )


        add_xp(
            user_id,
            50
        )



    update_player(

        user_id,

        player

    )



# =========================
# ПРОВЕРКА МАШИНЫ
# =========================


def has_car(
    user_id,
    car_name
):

    player = get_player(
        user_id
    )


    return car_name in player["garage"]



# =========================
# ПОБЕДА
# =========================


def add_win(
    user_id
):

    player = get_player(
        user_id
    )


    player["wins"] += 1

    player["coins"] += 200



    update_player(

        user_id,

        player

    )


    add_xp(

        user_id,

        100

    )



# =========================
# ПОРАЖЕНИЕ
# =========================


def add_loss(
    user_id
):

    player = get_player(
        user_id
    )


    player["losses"] += 1



    update_player(

        user_id,

        player

    )