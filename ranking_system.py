from database import load_database



# =========================
# РЕЙТИНГИ
# =========================


def get_players():

    database = load_database()


    players = []



    for user_id, player in database.items():

        players.append(

            {

                "id": user_id,

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

                "rep":
                player.get(
                    "rep",
                    0
                ),

                "garage":
                len(
                    player.get(
                        "garage",
                        []
                    )
                ),

                "league":
                player.get(
                    "league",
                    "🥉 Bronze"
                )

            }

        )



    return players




# =========================
# ОБЩИЙ РЕЙТИНГ
# =========================


def global_ranking(limit=10):


    players = get_players()



    for player in players:


        player["score"] = (

            player["rep"]

            +

            player["wins"] * 100

            +

            player["level"] * 50

            +

            player["garage"] * 20

        )



    players.sort(

        key=lambda x:

        x["score"],

        reverse=True

    )


    return players[:limit]




# =========================
# РЕЙТИНГ ПО ПОБЕДАМ
# =========================


def wins_ranking(limit=10):


    players = get_players()



    players.sort(

        key=lambda x:

        x["wins"],

        reverse=True

    )


    return players[:limit]




# =========================
# РЕЙТИНГ ПО ГАРАЖУ
# =========================


def garage_ranking(limit=10):


    players = get_players()



    players.sort(

        key=lambda x:

        x["garage"],

        reverse=True

    )


    return players[:limit]




# =========================
# ТЕКСТ ТОПА
# =========================


def ranking_text():

    top = global_ranking()



    text = (

        "🏆 <b>GLOBAL RANKING</b>\n\n"

    )


    place = 1



    for player in top:


        text += (

            f"{place} место 🏎\n"

            f"🏆 Лига: {player['league']}\n"

            f"⭐ Репутация: {player['rep']}\n"

            f"⚔️ Победы: {player['wins']}\n"

            f"🚗 Машин: {player['garage']}\n\n"

        )


        place += 1



    if not top:

        text += "Пока нет игроков"



    return text




# =========================
# СЕЗОННЫЕ НАГРАДЫ
# =========================


SEASON_REWARDS = [

    {

        "place":

        "1",

        "reward":

        "👑 Mythic Car + 100000 🪙"

    },


    {

        "place":

        "2-3",

        "reward":

        "🔥 Legendary Case"

    },


    {

        "place":

        "4-10",

        "reward":

        "💎 Rare Case"

    }

]




def season_rewards_text():

    text = (

        "🏁 <b>SEASON REWARDS</b>\n\n"

    )


    for reward in SEASON_REWARDS:


        text += (

            f"🏆 Место: {reward['place']}\n"

            f"🎁 {reward['reward']}\n\n"

        )



    return text