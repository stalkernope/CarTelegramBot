import json
import os
import random



POLICE_FILE = "police.json"




# =========================
# УРОВНИ РОЗЫСКА
# =========================


WANTED_LEVELS = [

    {
        "level": 0,
        "name": "🟢 Чист",
        "fine": 0
    },


    {
        "level": 1,
        "name": "🟡 Подозрение",
        "fine": 500
    },


    {
        "level": 2,
        "name": "🟠 В розыске",
        "fine": 2000
    },


    {
        "level": 3,
        "name": "🔴 Опасный гонщик",
        "fine": 5000
    },


    {
        "level": 4,
        "name": "🚨 Главный нарушитель",
        "fine": 15000
    },


    {
        "level": 5,
        "name": "👑 Легенда улиц",
        "fine": 50000
    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_police():

    if not os.path.exists(POLICE_FILE):

        return {}


    try:

        with open(
            POLICE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_police(data):

    with open(
        POLICE_FILE,
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


def get_police_data(user_id):

    data = load_police()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "wanted": 0,

            "escapes": 0,

            "caught": 0

        }


        save_police(data)



    return data[uid]




# =========================
# ДОБАВИТЬ РОЗЫСК
# =========================


def add_wanted(
    user_id,
    amount
):

    data = load_police()


    uid = str(user_id)



    player = get_police_data(
        user_id
    )


    player["wanted"] += amount



    if player["wanted"] > 5:

        player["wanted"] = 5



    data[uid] = player


    save_police(data)



    return player["wanted"]




# =========================
# УМЕНЬШИТЬ РОЗЫСК
# =========================


def remove_wanted(
    user_id,
    amount
):

    data = load_police()


    uid = str(user_id)


    player = get_police_data(
        user_id
    )


    player["wanted"] -= amount



    if player["wanted"] < 0:

        player["wanted"] = 0



    data[uid] = player


    save_police(data)



# =========================
# НЕЛЕГАЛЬНАЯ ГОНКА
# =========================


def illegal_race(
    user_id
):

    wanted = add_wanted(

        user_id,

        1

    )



    chance = random.randint(

        1,

        100

    )



    if chance <= wanted * 15:


        return {

            "caught": True,

            "wanted": wanted,

            "reward": 0

        }



    reward = (

        random.randint(

            1000,

            5000

        )

    )



    return {

        "caught": False,

        "wanted": wanted,

        "reward": reward

    }




# =========================
# ШТРАФ
# =========================


def pay_fine(user_id):

    player = get_police_data(
        user_id
    )


    level = player["wanted"]



    if level == 0:

        return 0



    fine = WANTED_LEVELS[level]["fine"]



    remove_wanted(

        user_id,

        level

    )



    return fine




# =========================
# ТЕКСТ
# =========================


def police_text(user_id):

    player = get_police_data(
        user_id
    )


    level = player["wanted"]



    status = WANTED_LEVELS[level]



    return (

        "🚓 <b>ПОЛИЦИЯ</b>\n\n"

        f"Статус: {status['name']}\n"

        f"⭐ Розыск: {level}/5\n"

        f"💰 Штраф: {status['fine']}\n\n"

        f"🏃 Побегов: {player['escapes']}\n"

        f"🚔 Задержаний: {player['caught']}"

    )