# =========================
# RANKING SYSTEM FINAL
# =========================


from database import (
    load_database
)


from car_database import (
    get_all_cars
)


from clan_system import (
    top_clans
)








# =========================
# PLAYER RANKING
# =========================


def player_ranking():


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

                ),


                "garage":

                len(

                    player.get(

                        "garage",

                        []

                    )

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



    return players







# =========================
# TOP PLAYERS TEXT
# =========================


def players_rating_text():


    players = player_ranking()



    text = (

        "🏆 <b>РЕЙТИНГ ИГРОКОВ</b>\n\n"

    )



    place = 1



    for player in players[:10]:


        text += (

            f"{place}. 👤 ID {player['id']}\n"

            f"🏁 Победы: {player['wins']}\n"

            f"⭐ Уровень: {player['level']}\n"

            f"🚗 Машины: {player['garage']}\n\n"

        )



        place += 1



    if place == 1:


        text += "Игроков пока нет"



    return text







# =========================
# WEALTH RANKING
# =========================


def coins_ranking():


    database = load_database()



    players = []



    for uid, player in database.items():


        players.append(

            {

                "id":

                uid,


                "coins":

                player.get(

                    "coins",

                    0

                )

            }

        )



    players.sort(

        key=lambda x:

        x["coins"],

        reverse=True

    )



    return players







# =========================
# CAR RANKING
# =========================


def car_ranking():


    cars = get_all_cars()



    cars.sort(

        key=lambda x:

        x.get(

            "power",

            0

        ),

        reverse=True

    )



    return cars







# =========================
# TOP CARS TEXT
# =========================


def cars_rating_text():


    cars = car_ranking()



    text = (

        "🚗 <b>ТОП МАШИН</b>\n\n"

    )



    place = 1



    for car in cars[:10]:


        text += (

            f"{place}. 🚘 {car['name']}\n"

            f"⚡ Power: {car.get('power',0)}\n"

            f"🚀 Speed: {car.get('speed',0)}\n\n"

        )


        place += 1



    return text







# =========================
# CLAN RANKING
# =========================


def clan_ranking():


    return top_clans()







# =========================
# GLOBAL RANKING
# =========================


def global_rating():


    return {


        "players":

        player_ranking(),


        "cars":

        car_ranking(),


        "clans":

        clan_ranking()

    }