# =========================
# CAREER SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player,
    add_coins,
    add_xp
)








# =========================
# CAREER LEVELS
# =========================


CAREER_LEVELS = {


    1: {

        "name":
        "Rookie",

        "need_xp":
        0,

        "reward":
        500

    },


    2: {

        "name":
        "Street Driver",

        "need_xp":
        1000,

        "reward":
        1000

    },


    3: {

        "name":
        "Racer",

        "need_xp":
        3000,

        "reward":
        2000

    },


    4: {

        "name":
        "Pro Racer",

        "need_xp":
        6000,

        "reward":
        5000

    },


    5: {

        "name":
        "Elite Driver",

        "need_xp":
        10000,

        "reward":
        10000

    },


    10: {

        "name":
        "Car Legend",

        "need_xp":
        50000,

        "reward":
        50000

    }

}








# =========================
# GET CAREER RANK
# =========================


def get_career_rank(level):


    rank = "Rookie"



    for lvl, data in CAREER_LEVELS.items():


        if level >= lvl:


            rank = data["name"]



    return rank







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



    rank = get_career_rank(

        level

    )



    next_level = level + 1



    need = next_level * 1000



    text = f"""

🏆 <b>КАРЬЕРА</b>


🎖 Ранг:

{rank}


⭐ Уровень:

{level}


🔥 XP:

{xp}/{need}


🎁 Следующая награда:

{need-xp} XP


"""



    return text







# =========================
# CHECK LEVEL UP
# =========================


def check_level(user_id):


    player = get_player(

        user_id

    )



    level_up = False




    while player["xp"] >= player["level"] * 1000:


        player["xp"] -= (

            player["level"]

            *

            1000

        )


        player["level"] += 1


        level_up = True






    if level_up:


        update_player(

            user_id,

            player

        )



    return level_up







# =========================
# CLAIM LEVEL REWARD
# =========================


def claim_level_reward(user_id):


    player = get_player(

        user_id

    )



    level = player.get(

        "level",

        1

    )



    if "career_rewards" not in player:


        player["career_rewards"] = []





    if level in player["career_rewards"]:


        return {


            "success":False,

            "message":

            "Награда уже получена"

        }






    reward = 0



    if level in CAREER_LEVELS:


        reward = CAREER_LEVELS[level]["reward"]





    player["career_rewards"].append(

        level

    )



    update_player(

        user_id,

        player

    )



    add_coins(

        user_id,

        reward

    )



    return {


        "success":True,


        "reward":reward,


        "message":

        f"🎁 Получено {reward} монет"

    }