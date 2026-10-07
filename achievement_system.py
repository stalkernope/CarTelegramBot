# =========================
# ACHIEVEMENT SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player,
    add_coins,
    add_xp
)







# =========================
# ACHIEVEMENTS DATABASE
# =========================


ACHIEVEMENTS = {


    "first_win": {


        "name":
        "🏁 Первая победа",


        "description":
        "Выиграть первую гонку",


        "reward_coins":
        1000,


        "reward_xp":
        200,


        "title":
        "Street Racer"

    },



    "collector": {


        "name":
        "🚗 Коллекционер",


        "description":
        "Собрать 5 машин",


        "reward_coins":
        5000,


        "reward_xp":
        500,


        "title":
        "Car Collector"

    },



    "legend": {


        "name":
        "👑 Легенда",


        "description":
        "Достичь 10 уровня",


        "reward_coins":
        25000,


        "reward_xp":
        3000,


        "title":
        "Car Legend"

    }

}








# =========================
# CHECK ACHIEVEMENTS
# =========================


def check_achievements(user_id):


    player = get_player(

        user_id

    )



    unlocked = player.get(

        "achievements",

        []

    )



    new = []





    for key, data in ACHIEVEMENTS.items():



        if key in unlocked:

            continue





        result = False





        if key == "first_win":


            if player.get(

                "wins",

                0

            ) >= 1:


                result = True





        elif key == "collector":


            if len(

                player.get(

                    "garage",

                    []

                )

            ) >= 5:


                result = True





        elif key == "legend":


            if player.get(

                "level",

                1

            ) >= 10:


                result = True






        if result:


            unlocked.append(

                key

            )


            new.append(

                key

            )



            if data.get(

                "reward_coins"

            ):


                add_coins(

                    user_id,

                    data["reward_coins"]

                )





            if data.get(

                "reward_xp"

            ):


                add_xp(

                    user_id,

                    data["reward_xp"]

                )





            if data.get(

                "title"

            ):


                if "titles" not in player:


                    player["titles"] = []



                if data["title"] not in player["titles"]:


                    player["titles"].append(

                        data["title"]

                    )






    player["achievements"] = unlocked



    update_player(

        user_id,

        player

    )



    return new







# =========================
# ACHIEVEMENT TEXT
# =========================


def achievement_text(user_id):


    player = get_player(

        user_id

    )


    unlocked = player.get(

        "achievements",

        []

    )



    text = (

        "🏆 <b>ДОСТИЖЕНИЯ</b>\n\n"

    )





    for key, data in ACHIEVEMENTS.items():


        if key in unlocked:


            status = "✅"


        else:


            status = "🔒"





        text += (

            f"{status} {data['name']}\n"

            f"{data['description']}\n\n"

        )



    return text







# =========================
# TITLES
# =========================


def get_titles(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "titles",

        []

    )