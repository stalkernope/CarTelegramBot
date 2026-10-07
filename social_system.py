# =========================
# SOCIAL SYSTEM FINAL
# =========================


import json
import os



from database import (
    load_database,
    get_player
)







# =========================
# BATTLE PASS
# =========================


BATTLE_PASS = {


    "season":

    "Season 1: Street Kings",


    "levels":

    [

        {

            "level":1,

            "reward":

            "💰 1000 coins"

        },


        {

            "level":5,

            "reward":

            "💎 50 gems"

        },


        {

            "level":10,

            "reward":

            "🚗 Exclusive Car"

        }

    ]

}







# =========================
# PLAYER RATING
# =========================


def get_players_rating():


    database = load_database()



    players = []



    for uid, player in database.items():


        players.append(

            {

                "id":

                uid,


                "level":

                player.get(

                    "level",

                    1

                ),


                "wins":

                player.get(

                    "wins",

                    0

                ),


                "coins":

                player.get(

                    "coins",

                    0

                )

            }

        )





    players.sort(

        key=lambda x:

        (

            x["wins"],

            x["level"]

        ),

        reverse=True

    )



    return players[:50]









# =========================
# TOP TEXT
# =========================


def top_text():


    players = get_players_rating()



    text = (

        "🏆 <b>ТОП ИГРОКОВ</b>\n\n"

    )



    if not players:


        return text + "Игроков нет"





    place = 1



    for player in players:



        text += (

            f"{place}. 👤 ID {player['id']}\n"

            f"🏁 Победы: {player['wins']}\n"

            f"⭐ Уровень: {player['level']}\n\n"

        )


        place += 1



    return text







# =========================
# BATTLE PASS TEXT
# =========================


def battle_pass_text():


    text = (

        "🎫 <b>BATTLE PASS</b>\n\n"

        f"🔥 {BATTLE_PASS['season']}\n\n"

    )



    for reward in BATTLE_PASS["levels"]:


        text += (

            f"⭐ Уровень {reward['level']}\n"

            f"🎁 {reward['reward']}\n\n"

        )



    return text







# =========================
# TOURNAMENTS
# =========================


def tournaments_text():


    return """

🏆 <b>ТУРНИРЫ</b>


🔥 Ежедневные гонки

🥇 Чемпионаты

🎁 Большие награды


Скоро доступно.

"""







# =========================
# FRIENDS
# =========================


def get_friends(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "friends",

        []

    )








def add_friend(

    user_id,

    friend_id

):


    player = get_player(

        user_id

    )



    if "friends" not in player:


        player["friends"] = []





    if friend_id not in player["friends"]:


        player["friends"].append(

            friend_id

        )



    return True







# =========================
# REFERRALS
# =========================


def get_referrals(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "referrals",

        []

    )