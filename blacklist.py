# =========================
# BLACKLIST FINAL COMPLETE
# CAR LEGENDS
# =========================


from database import (
    get_player,
    update_player,
    add_coins,
    add_xp
)


from boss_race_system import (
    BOSSES
)


from car_database import (
    get_car
)








# =========================
# BLACKLIST REWARDS
# =========================


BLACKLIST_REWARDS = {


    1: {


        "coins":10000,

        "xp":500,

        "car":
        "Nissan Skyline R34"

    },


    2: {


        "coins":25000,

        "xp":1000,

        "car":
        "Lamborghini Aventador SVJ"

    },


    3: {


        "coins":50000,

        "xp":2000,

        "car":
        "Bugatti Chiron"

    }

}








# =========================
# GET BLACKLIST
# =========================


def get_blacklist():



    result = []



    for level, boss in BOSSES.items():


        result.append(

            {


                "level":

                level,


                "name":

                boss["name"],


                "car":

                boss["car"],


                "power":

                boss["power"],


                "reward":

                BLACKLIST_REWARDS.get(

                    level,

                    {}

                )

            }

        )



    return result







# =========================
# CURRENT OPPONENT
# =========================


def get_current_opponent(

    user_id

):


    player = get_player(

        user_id

    )


    level = player.get(

        "boss_progress",

        0

    ) + 1





    if level not in BOSSES:


        return None





    boss = BOSSES[level]



    return {


        "level":

        level,


        "name":

        boss["name"],


        "car":

        boss["car"],


        "power":

        boss["power"]

    }
    
    
    # =========================
# DEFEAT OPPONENT
# =========================


def defeat_opponent(

    user_id

):


    player = get_player(

        user_id

    )



    current_level = player.get(

        "boss_progress",

        0

    ) + 1





    if current_level not in BLACKLIST_REWARDS:


        return {


            "success":False,

            "text":

            "🏆 Все соперники побеждены"

        }







    reward = BLACKLIST_REWARDS[current_level]





    add_coins(

        user_id,

        reward["coins"]

    )


    add_xp(

        user_id,

        reward["xp"]

    )






    player = get_player(

        user_id

    )



    player["boss_progress"] = current_level





    if "defeated_bosses" not in player:


        player["defeated_bosses"] = []





    opponent = BOSSES[current_level]





    if opponent["name"] not in player["defeated_bosses"]:


        player["defeated_bosses"].append(

            opponent["name"]

        )






    update_player(

        user_id,

        player

    )





    return {


        "success":True,


        "level":

        current_level,


        "reward":

        reward

    }








# =========================
# CHECK UNLOCKED LEVEL
# =========================


def is_level_unlocked(

    user_id,

    level

):


    player = get_player(

        user_id

    )


    progress = player.get(

        "boss_progress",

        0

    )



    return level <= progress + 1







# =========================
# GET PLAYER BLACKLIST DATA
# =========================


def get_blacklist_progress(

    user_id

):


    player = get_player(

        user_id

    )


    progress = player.get(

        "boss_progress",

        0

    )



    return {


        "current":

        progress,


        "total":

        len(

            BLACKLIST_REWARDS

        ),


        "defeated":

        player.get(

            "defeated_bosses",

            []

        )

    }








# =========================
# MINI APP DATA
# =========================


def get_blacklist_cards(

    user_id

):


    progress = get_blacklist_progress(

        user_id

    )



    result = []



    for level, boss in BOSSES.items():


        result.append(

            {


                "level":

                level,


                "name":

                boss["name"],


                "car":

                boss["car"],


                "power":

                boss["power"],


                "unlocked":

                is_level_unlocked(

                    user_id,

                    level

                ),


                "defeated":

                level <= progress["current"]

            }

        )



    return result