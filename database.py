import json
import os


DATABASE_FILE = "players.json"


DEFAULT_PLAYER = {

    "coins": 1000,

    "level": 1,

    "xp": 0,

    "rep": 0,

    "title": "Новичок",

    "league": "🥉 Bronze",

    "wins": 0,

    "losses": 0,

    "win_streak": 0,

    "best_streak": 0,

    "garage": [],

    "main_car": None,

    "achievements": [],

    "created": ""

}



# =========================
# ЗАГРУЗКА
# =========================


def load_database():

    if not os.path.exists(DATABASE_FILE):

        return {}


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
            "Ошибка базы:",
            e
        )


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
# ПОЛУЧЕНИЕ ИГРОКА
# =========================


def get_player(user_id):

    data = load_database()


    uid = str(user_id)



    if uid not in data:


        data[uid] = DEFAULT_PLAYER.copy()


        save_database(
            data
        )


    else:


        # добавляем новые поля старым игрокам

        changed = False


        for key, value in DEFAULT_PLAYER.items():

            if key not in data[uid]:

                data[uid][key] = value

                changed = True



        if changed:

            save_database(
                data
            )



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


    save_database(
        data
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


    if car_name not in player["garage"]:

        player["garage"].append(
            car_name
        )


    if player["main_car"] is None:

        player["main_car"] = car_name



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


    update_player(

        user_id,

        player

    )




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



    need = player["level"] * 1000



    if player["xp"] >= need:

        player["xp"] -= need

        player["level"] += 1



    update_player(

        user_id,

        player

    )




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

    player["win_streak"] += 1



    if player["win_streak"] > player["best_streak"]:

        player["best_streak"] = player["win_streak"]



    player["rep"] += 50


    add_xp(
        user_id,
        200
    )



    update_player(

        user_id,

        player

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

    player["win_streak"] = 0


    update_player(

        user_id,

        player

    )