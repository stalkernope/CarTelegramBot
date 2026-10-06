import json
import os


from database import (
    get_player,
    update_player
)




CAREER_FILE = "career.json"




# =========================
# НАГРАДЫ УРОВНЕЙ
# =========================


LEVEL_REWARDS = {


    2: {

        "coins": 1000,

        "title": "🚗 Новичок"

    },


    5: {

        "coins": 5000,

        "title": "🏁 Street Racer"

    },


    10: {

        "coins": 15000,

        "title": "🔥 Speed Master"

    },


    25: {

        "coins": 50000,

        "title": "💎 Elite Driver"

    },


    50: {

        "coins": 200000,

        "title": "👑 Car Legend"

    }

}




# =========================
# ЗАГРУЗКА
# =========================


def load_career():


    if not os.path.exists(CAREER_FILE):

        return {}



    try:


        with open(

            CAREER_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except:


        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_career(data):


    with open(

        CAREER_FILE,

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
# ПРОФИЛЬ КАРЬЕРЫ
# =========================


def get_career(user_id):


    data = load_career()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {


            "level": 1,


            "xp": 0,


            "titles": [],


            "claimed": []

        }


        save_career(data)



    return data[uid]
    
    # =========================
# ДОБАВИТЬ XP
# =========================


def add_career_xp(

    user_id,

    amount

):


    data = load_career()


    career = get_career(

        user_id

    )


    career["xp"] += amount



    leveled = False



    while career["xp"] >= need_xp(

        career["level"]

    ):


        career["xp"] -= need_xp(

            career["level"]

        )


        career["level"] += 1


        leveled = True



    data[str(user_id)] = career


    save_career(

        data

    )



    rewards = check_rewards(

        user_id

    )



    return {


        "level":

        career["level"],


        "leveled":

        leveled,


        "rewards":

        rewards

    }




# =========================
# XP ДЛЯ УРОВНЯ
# =========================


def need_xp(level):


    return level * 1000




# =========================
# ПРОВЕРКА НАГРАД
# =========================


def check_rewards(

    user_id

):


    data = load_career()


    career = get_career(

        user_id

    )


    rewards = []



    for level, reward in LEVEL_REWARDS.items():


        if level <= career["level"] and level not in career["claimed"]:



            career["claimed"].append(

                level

            )



            if reward.get("title"):


                career["titles"].append(

                    reward["title"]

                )



            rewards.append(

                reward

            )



    data[str(user_id)] = career


    save_career(

        data

    )



    return rewards




# =========================
# ДОБАВИТЬ ТИТУЛ
# =========================


def get_titles(user_id):


    career = get_career(

        user_id

    )


    return career.get(

        "titles",

        []

    )
    # =========================
# ТЕКСТ КАРЬЕРЫ
# =========================


def career_text(user_id):


    career = get_career(

        user_id

    )



    level = career["level"]

    xp = career["xp"]



    need = need_xp(

        level

    )



    text = (

        "🏆 <b>КАРЬЕРА</b>\n\n"

        f"⭐ Уровень: {level}\n"

        f"📈 XP: {xp}/{need}\n\n"

    )



    titles = career.get(

        "titles",

        []

    )



    if titles:


        text += (

            "🎖 Титулы:\n"

        )


        for title in titles:


            text += (

                f"{title}\n"

            )


    else:


        text += (

            "🎖 Титулы:\n"

            "Нет\n"

        )



    text += (

        "\n🎁 Следующие награды:\n"

    )



    found = False



    for lvl, reward in LEVEL_REWARDS.items():


        if lvl > level:


            text += (

                f"⭐ {lvl} уровень\n"

                f"🎁 {reward.get('coins',0)} 🪙\n"

            )


            found = True


            break



    if not found:


        text += (

            "👑 Ты достиг вершины!"

        )



    return text




# =========================
# СТАТИСТИКА КАРЬЕРЫ
# =========================


def career_stats(user_id):


    career = get_career(

        user_id

    )


    return {


        "level":

        career["level"],


        "xp":

        career["xp"],


        "titles":

        len(

            career["titles"]

        )

    }
    
    # =========================
# CAREER SYSTEM FIX
# =========================


from database import get_player






# =========================
# CAREER TEXT
# =========================


def career_text(user_id):


    player = get_player(

        user_id

    )


    level = player.get(

        "level",

        1

    )


    xp = player.get(

        "xp",

        0

    )


    wins = player.get(

        "wins",

        0

    )


    text = (

        "🏆 <b>КАРЬЕРА</b>\n\n"

        f"⭐ Уровень: {level}\n"

        f"🔥 Опыт: {xp}\n\n"

        f"🏁 Победы: {wins}\n\n"

    )



    if level >= 50:


        text += (

            "👑 Ранг: CAR LEGEND"

        )


    elif level >= 20:


        text += (

            "🔥 Ранг: PRO RACER"

        )


    elif level >= 5:


        text += (

            "⚡ Ранг: STREET RACER"

        )


    else:


        text += (

            "🚗 Ранг: NOVICE"

        )



    return text