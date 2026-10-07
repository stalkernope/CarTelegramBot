# =========================
# PLAYER SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player
)





# =========================
# PLAYER PROFILE
# =========================


def get_profile(user_id):


    player = get_player(

        user_id

    )



    return {


        "id":

        player.get(

            "id",

            user_id

        ),



        "level":

        player.get(

            "level",

            1

        ),



        "xp":

        player.get(

            "xp",

            0

        ),



        "coins":

        player.get(

            "coins",

            0

        ),



        "gems":

        player.get(

            "gems",

            0

        ),



        "wins":

        player.get(

            "wins",

            0

        ),



        "losses":

        player.get(

            "losses",

            0

        ),



        "garage":

        player.get(

            "garage",

            []

        ),



        "main_car":

        player.get(

            "main_car"

        ),



        "pets":

        player.get(

            "pets",

            []

        ),



        "titles":

        player.get(

            "titles",

            []

        ),



        "clan":

        player.get(

            "clan"

        ),



        "premium":

        player.get(

            "premium",

            False

        )

    }







# =========================
# PROFILE TEXT
# =========================


def profile_text(user_id):


    player = get_player(

        user_id

    )



    return f"""

👤 <b>ПРОФИЛЬ</b>


🆔 ID:

{user_id}


⭐ Уровень:

{player.get('level',1)}


🔥 XP:

{player.get('xp',0)}


💰 Монеты:

{player.get('coins',0)}


💎 Кристаллы:

{player.get('gems',0)}


🏁 Победы:

{player.get('wins',0)}


❌ Поражения:

{player.get('losses',0)}


🚗 Машины:

{len(player.get('garage',[]))}


🐾 Питомцы:

{len(player.get('pets',[]))}


👑 Главная машина:

{player.get('main_car','нет')}

"""








# =========================
# STATS
# =========================


def get_stats(user_id):


    player = get_player(

        user_id

    )


    wins = player.get(

        "wins",

        0

    )


    losses = player.get(

        "losses",

        0

    )



    total = wins + losses



    if total > 0:


        win_rate = round(

            wins / total * 100,

            1

        )


    else:


        win_rate = 0





    return {


        "wins":

        wins,


        "losses":

        losses,


        "win_rate":

        win_rate,


        "cars":

        len(

            player.get(

                "garage",

                []

            )

        ),


        "pets":

        len(

            player.get(

                "pets",

                []

            )

        )

    }








# =========================
# ADD TITLE
# =========================


def add_title(

    user_id,

    title

):


    player = get_player(

        user_id

    )



    if "titles" not in player:


        player["titles"] = []





    if title not in player["titles"]:


        player["titles"].append(

            title

        )



    update_player(

        user_id,

        player

    )



    return True







# =========================
# PREMIUM
# =========================


def set_premium(

    user_id,

    status=True

):


    player = get_player(

        user_id

    )



    player["premium"] = status



    update_player(

        user_id,

        player

    )



    return True







# =========================
# RESET PLAYER
# =========================


def reset_player(user_id):


    player = get_player(

        user_id

    )



    player["coins"] = 5000

    player["gems"] = 0

    player["level"] = 1

    player["xp"] = 0

    player["garage"] = []

    player["main_car"] = None

    player["wins"] = 0

    player["losses"] = 0



    update_player(

        user_id,

        player

    )


    return True