import json
import os


DATABASE_FILE = "game_core.json"



# =========================
# ЗАГРУЗКА
# =========================


def load_players():

    if not os.path.exists(DATABASE_FILE):

        return {}


    try:

        with open(
            DATABASE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# ТОП ПО РЕЙТИНГУ
# =========================


def top_rating(limit=10):

    players = load_players()


    result = []


    for uid, player in players.items():

        result.append({

            "id": uid,

            "rating":

            player.get(
                "rating",
                0
            ),

            "wins":

            player.get(
                "wins",
                0
            ),

            "money":

            player.get(
                "money",
                0
            )

        })


    result.sort(

        key=lambda x:

        x["rating"],

        reverse=True

    )


    return result[:limit]




# =========================
# ТЕКСТ
# =========================


def leaderboard_text():


    players = top_rating()


    text = (

        "🏆 <b>CAR LEGENDS TOP</b>\n\n"

    )


    if not players:


        return text + "Пока игроков нет"



    place = 1



    for player in players:


        text += (

            f"{place}. 🏎 Игрок\n"

            f"⭐ Рейтинг: {player['rating']}\n"

            f"🏁 Победы: {player['wins']}\n"

            f"💰 Деньги: {player['money']}\n\n"

        )


        place += 1



    return text