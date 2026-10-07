# =========================
# BATTLES SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player
)


from battle_system import (
    start_battle,
    battle_text
)







# =========================
# BATTLE MODES
# =========================


BATTLE_MODES = {


    "quick":

    {

        "name":

        "⚔️ Быстрый бой",

        "reward":

        2000

    },


    "ranked":

    {

        "name":

        "🏆 Рейтинговый бой",

        "reward":

        5000

    },


    "clan":

    {

        "name":

        "⚔️ Клановая битва",

        "reward":

        10000

    }

}







# =========================
# GET MODES
# =========================


def get_battle_modes():


    return BATTLE_MODES







# =========================
# BATTLE TEXT MENU
# =========================


def battles_text():


    text = (

        "⚔️ <b>БИТВЫ</b>\n\n"

    )



    for key, mode in BATTLE_MODES.items():


        text += (

            f"{mode['name']}\n"

            f"🎁 Награда: "

            f"{mode['reward']}\n\n"

        )



    return text







# =========================
# START PVP
# =========================


def create_battle(

    player_id,

    enemy_id

):


    result = start_battle(

        player_id,

        enemy_id

    )



    return result







# =========================
# RESULT TEXT
# =========================


def get_battle_result_text(

    result,

    user_id

):


    return battle_text(

        result,

        user_id

    )








# =========================
# SAVE HISTORY
# =========================


def save_battle_history(

    user_id,

    result

):


    player = get_player(

        user_id

    )



    if "battle_history" not in player:


        player["battle_history"] = []





    player["battle_history"].append(

        {


            "winner":

            result.get(

                "winner"

            ),


            "loser":

            result.get(

                "loser"

            )

        }

    )



    # ограничиваем историю

    player["battle_history"] = (

        player["battle_history"][-20:]

    )



    update_player(

        user_id,

        player

    )



    return True







# =========================
# GET HISTORY
# =========================


def get_history(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "battle_history",

        []

    )