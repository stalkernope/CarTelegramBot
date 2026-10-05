import json
import os


from database import (
    load_database,
    get_player
)



SOCIAL_FILE = "social.json"



# =========================
# ЗАГРУЗКА
# =========================


def load_social():

    if not os.path.exists(SOCIAL_FILE):

        return {

            "season": 1,

            "players": {},

            "tournaments": []

        }


    try:

        with open(
            SOCIAL_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {

            "season": 1,

            "players": {},

            "tournaments": []

        }




# =========================
# СОХРАНЕНИЕ
# =========================


def save_social(data):

    with open(
        SOCIAL_FILE,
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
# ТОП ИГРОКОВ
# =========================


def get_top_players(limit=10):

    database = load_database()


    players = []



    for user_id, player in database.items():

        players.append(

            {

                "id": user_id,

                "wins": player.get(
                    "wins",
                    0
                ),

                "level": player.get(
                    "level",
                    1
                ),

                "rep": player.get(
                    "rep",
                    0
                )

            }

        )



    players.sort(

        key=lambda x:

        (

            x["rep"],

            x["wins"],

            x["level"]

        ),

        reverse=True

    )


    return players[:limit]




# =========================
# ТЕКСТ ТОПА
# =========================


def top_text():

    top = get_top_players()


    text = (

        "🏆 <b>CAR LEGENDS TOP</b>\n\n"

    )


    place = 1



    for player in top:


        text += (

            f"{place} место 🏎\n"

            f"⭐ Репутация: {player['rep']}\n"

            f"⚔️ Победы: {player['wins']}\n"

            f"📈 Уровень: {player['level']}\n\n"

        )


        place += 1



    if len(top) == 0:

        text += "Пока нет игроков"



    return text




# =========================
# СЕЗОН
# =========================


def get_season():

    data = load_social()


    return data.get(

        "season",

        1

    )




def next_season():

    data = load_social()


    data["season"] += 1


    save_social(
        data
    )


    return data["season"]




# =========================
# БОЕВОЙ ПРОПУСК
# =========================


PASS_REWARDS = [

    {
        "level": 1,

        "reward": "1000 🪙"

    },


    {
        "level": 5,

        "reward": "5000 🪙"

    },


    {
        "level": 10,

        "reward": "🎁 Legendary Case"

    },


    {
        "level": 50,

        "reward": "🔥 Mythic Car"

    }

]




def battle_pass_text():

    text = (

        "🏁 <b>BATTLE PASS</b>\n\n"

    )


    for item in PASS_REWARDS:

        text += (

            f"⭐ Уровень {item['level']}\n"

            f"🎁 {item['reward']}\n\n"

        )


    return text




# =========================
# ТУРНИРЫ
# =========================


def create_tournament(name):

    data = load_social()



    tournament = {

        "name": name,

        "players": [],

        "status": "open"

    }



    data["tournaments"].append(

        tournament

    )


    save_social(
        data
    )


    return tournament




def tournaments_text():

    data = load_social()


    text = (

        "🏆 <b>ТУРНИРЫ</b>\n\n"

    )



    if not data["tournaments"]:

        return text + "Нет активных турниров"



    for tournament in data["tournaments"]:


        text += (

            f"🔥 {tournament['name']}\n"

            f"👥 Игроков: "

            f"{len(tournament['players'])}\n\n"

        )



    return text