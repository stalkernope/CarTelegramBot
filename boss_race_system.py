# =========================
# BOSS RACE SYSTEM FINAL COMPLETE
# CAR LEGENDS
# =========================


import random



from database import (
    get_player,
    add_win,
    add_loss,
    add_coins,
    add_xp,
    add_race_history,
    update_player
)



from garage_system import (
    get_race_car
)



from tuning import (
    get_upgraded_car_stats
)



from car_database import (
    get_car
)







# =========================
# BOSSES
# =========================


BOSSES = {


    1: {


        "name":
        "Shadow Racer",


        "car":
        "Nissan Skyline R34",


        "power":
        1200,


        "reward":
        10000

    },


    2: {


        "name":
        "Night King",


        "car":
        "Lamborghini Aventador SVJ",


        "power":
        1800,


        "reward":
        25000

    },


    3: {


        "name":
        "Black Legend",


        "car":
        "Bugatti Chiron",


        "power":
        2500,


        "reward":
        50000

    }

}








# =========================
# CALCULATE POWER
# =========================


def calculate_power(car):


    if not car:


        return 0




    return (

        car.get(
            "power",
            0
        )

        +

        car.get(
            "speed",
            0
        )

        +

        car.get(
            "handling",
            0
        )

        +

        car.get(
            "nitro",
            0
        )

    )








# =========================
# PLAYER POWER
# =========================


def get_player_power(

    user_id

):


    car = get_race_car(

        user_id

    )



    if not car:


        return {


            "car":

            None,


            "power":

            0

        }





    stats = get_upgraded_car_stats(

        user_id,

        car["name"]

    )



    return {


        "car":

        car["name"],


        "power":

        calculate_power(

            stats

        )

    }
    
    
    # =========================
# STREET RACE
# =========================


def start_street_race(

    user_id

):


    player = get_player_power(

        user_id

    )



    if not player["car"]:


        return {


            "success":False,

            "text":

            "❌ Выбери машину для гонки"

        }






    enemy_power = random.randint(

        player["power"] - 300,

        player["power"] + 300

    )



    enemy_power = max(

        enemy_power,

        500

    )





    win_chance = (

        player["power"]

        /

        (

            player["power"]

            +

            enemy_power

        )

    )



    win = random.random() < win_chance






    if win:


        reward = random.randint(

            3000,

            7000

        )



        add_win(

            user_id

        )


        add_coins(

            user_id,

            reward

        )


        add_xp(

            user_id,

            150

        )



        result = {


            "result":

            "WIN",


            "coins":

            reward

        }



    else:


        add_loss(

            user_id

        )



        add_xp(

            user_id,

            50

        )


        result = {


            "result":

            "LOSE",


            "coins":

            0

        }







    add_race_history(

        user_id,

        result

    )



    return {


        "success":

        True,


        "player_car":

        player["car"],



        "player_power":

        player["power"],



        "enemy_power":

        enemy_power,



        "result":

        result

    }









# =========================
# GET CURRENT BOSS
# =========================


def get_current_boss(

    user_id

):


    player = get_player(

        user_id

    )



    progress = player.get(

        "boss_progress",

        0

    )



    boss_id = progress + 1





    if boss_id not in BOSSES:


        return None





    return BOSSES[boss_id]









# =========================
# BOSS RACE
# =========================


def start_boss_race(

    user_id

):


    boss = get_current_boss(

        user_id

    )



    if not boss:


        return {


            "success":False,

            "text":

            "🏆 Все боссы побеждены"

        }








    player = get_player_power(

        user_id

    )



    if not player["car"]:


        return {


            "success":False,

            "text":

            "❌ Нет активной машины"

        }







    player_power = player["power"]



    boss_power = boss["power"]






    win_chance = (

        player_power

        /

        (

            player_power

            +

            boss_power

        )

    )





    win = random.random() < win_chance
    
    
    # =========================
# FINISH BOSS RACE
# =========================


    if win:


        reward = boss["reward"]



        add_win(

            user_id

        )


        add_coins(

            user_id,

            reward

        )


        add_xp(

            user_id,

            500

        )



        player_data = get_player(

            user_id

        )



        player_data["boss_progress"] = (

            player_data.get(

                "boss_progress",

                0

            )

            +

            1

        )



        if boss["car"] not in player_data.get(

            "defeated_bosses",

            []

        ):


            player_data.setdefault(

                "defeated_bosses",

                []

            ).append(

                boss["car"]

            )



        update_player(

            user_id,

            player_data

        )



        result = {


            "result":

            "WIN",


            "boss":

            boss["name"],


            "reward":

            reward

        }





    else:


        add_loss(

            user_id

        )


        add_xp(

            user_id,

            100

        )



        result = {


            "result":

            "LOSE",


            "boss":

            boss["name"],


            "reward":

            0

        }







    add_race_history(

        user_id,

        result

    )



    return {


        "success":

        True,


        "boss":

        boss["name"],


        "boss_car":

        boss["car"],


        "player_car":

        player["car"],


        "player_power":

        player_power,


        "boss_power":

        boss_power,


        "result":

        result

    }







# =========================
# GET ALL BOSSES
# MINI APP
# =========================


def get_boss_list(

    user_id

):


    player = get_player(

        user_id

    )



    progress = player.get(

        "boss_progress",

        0

    )



    result = []



    for boss_id, boss in BOSSES.items():


        result.append(


            {


                "id":

                boss_id,


                "name":

                boss["name"],


                "car":

                boss["car"],


                "power":

                boss["power"],


                "reward":

                boss["reward"],


                "unlocked":

                boss_id <= progress + 1,


                "defeated":

                boss_id <= progress

            }


        )



    return result








# =========================
# BOSS PROGRESS
# =========================


def get_boss_progress(

    user_id

):


    player = get_player(

        user_id

    )



    return {


        "current":

        player.get(

            "boss_progress",

            0

        ),


        "total":

        len(

            BOSSES

        )

    }
    
    
    # =========================
# COMPATIBILITY FUNCTION
# API COMPATIBILITY
# =========================

def race_npc(user_id, boss_id=None):

    if boss_id:

        boss = BOSSES.get(boss_id)

        if not boss:
            return {
                "success": False,
                "text": "Boss not found"
            }


    return start_boss_race(user_id)
    
    
    # =========================
# API COMPATIBILITY
# FIGHT BOSS
# =========================

def fight_boss(user_id, boss_id=None):

    if boss_id is not None:

        boss = BOSSES.get(boss_id)

        if not boss:
            return {
                "success": False,
                "text": "❌ Босс не найден"
            }


    return start_boss_race(user_id)