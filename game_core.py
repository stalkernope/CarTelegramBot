import json
import os
import time



CORE_FILE = "game_core.json"




# =========================
# ПРОФИЛЬ ИГРОКА
# =========================


def load_core():

    if not os.path.exists(CORE_FILE):

        return {}


    try:

        with open(
            CORE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




def save_core(data):

    with open(
        CORE_FILE,
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
# СОЗДАНИЕ ИГРОКА
# =========================


def get_player(user_id):

    data = load_core()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "level": 1,

            "xp": 0,

            "money": 500000,

            "rating": 0,

            "races": 0,

            "wins": 0,

            "losses": 0,

            "created":

            time.time()

        }


        save_core(data)



    return data[uid]




# =========================
# ОПЫТ
# =========================


def add_xp(

    user_id,

    amount

):

    data = load_core()


    player = get_player(

        user_id

    )



    player["xp"] += amount



    need = player["level"] * 500



    if player["xp"] >= need:


        player["xp"] -= need

        player["level"] += 1



        level_up = True


    else:


        level_up = False




    data[str(user_id)] = player


    save_core(data)



    return level_up




# =========================
# ДЕНЬГИ
# =========================


def add_money(

    user_id,

    amount

):

    data = load_core()


    player = get_player(

        user_id

    )


    player["money"] += amount



    data[str(user_id)] = player


    save_core(data)




# =========================
# ГОНКА
# =========================


def race_result(

    user_id,

    win

):

    data = load_core()


    player = get_player(

        user_id

    )


    player["races"] += 1



    if win:


        player["wins"] += 1

        player["rating"] += 25

        player["money"] += 1000

        xp = 200



    else:


        player["losses"] += 1

        player["rating"] += 5

        player["money"] += 200

        xp = 50




    data[str(user_id)] = player


    save_core(data)



    add_xp(

        user_id,

        xp

    )



    return player




# =========================
# СТАТИСТИКА
# =========================


def profile_text(user_id):

    player = get_player(

        user_id

    )



    return (

        "🎮 <b>ПРОФИЛЬ ИГРОКА</b>\n\n"

        f"⭐ Уровень: {player['level']}\n"

        f"✨ XP: {player['xp']}\n"

        f"💰 Деньги: {player['money']}\n"

        f"🏁 Гонки: {player['races']}\n"

        f"🏆 Победы: {player['wins']}\n"

        f"❌ Поражения: {player['losses']}\n"

        f"🔥 Рейтинг: {player['rating']}"

    )