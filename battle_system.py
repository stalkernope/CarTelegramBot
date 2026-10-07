# =========================
# BATTLE SYSTEM FINAL COMPLETE
# CAR LEGENDS
# =========================


import random



from database import (
    get_player,
    add_win,
    add_loss,
    add_coins,
    add_xp,
    add_battle_history,
    update_player
)



from garage_system import (
    get_race_car
)



from tuning import (
    get_upgraded_car_stats
)







# =========================
# BATTLE REWARDS
# =========================


REWARDS = {


    "win_coins":5000,

    "win_xp":250,


    "lose_xp":50

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
# GET PLAYER BATTLE DATA
# =========================


def get_battle_power(

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
# CREATE BATTLE
# =========================


def create_battle(

    player_one,

    player_two

):


    return {


        "player_one":

        player_one,


        "player_two":

        player_two,


        "status":

        "waiting"

    }
    
    
    # =========================
# FIGHT
# =========================


def fight(

    player_one,

    player_two

):


    p1 = get_battle_power(

        player_one

    )


    p2 = get_battle_power(

        player_two

    )



    if not p1["car"] or not p2["car"]:


        return {


            "success":False,

            "text":

            "❌ У игрока нет машины"

        }







    power_one = p1["power"]

    power_two = p2["power"]






    chance_one = (

        power_one

        /

        (

            power_one

            +

            power_two

        )

    )





    if random.random() < chance_one:


        winner = player_one

        loser = player_two



    else:


        winner = player_two

        loser = player_one








    add_win(

        winner

    )


    add_loss(

        loser

    )



    add_coins(

        winner,

        REWARDS["win_coins"]

    )



    add_xp(

        winner,

        REWARDS["win_xp"]

    )



    add_xp(

        loser,

        REWARDS["lose_xp"]

    )







    result = {


        "winner":

        winner,


        "loser":

        loser,


        "cars":

        {


            player_one:

            p1["car"],


            player_two:

            p2["car"]

        }

    }







    add_battle_history(

        player_one,

        result

    )


    add_battle_history(

        player_two,

        result

    )






    return {


        "success":

        True,


        "result":

        result,


        "power":

        {


            player_one:

            power_one,


            player_two:

            power_two

        }

    }









# =========================
# CHANGE RATING
# =========================


def update_rating(

    user_id,

    value

):


    player = get_player(

        user_id

    )



    player["rating"] = max(

        0,

        player.get(

            "rating",

            1000

        )

        +

        value

    )



    update_player(

        user_id,

        player

    )



    return player["rating"]








# =========================
# GET BATTLE HISTORY
# =========================


def get_battle_history(

    user_id

):


    player = get_player(

        user_id

    )


    return player.get(

        "battle_history",

        []

    )








# =========================
# PROFILE RATING
# =========================


def get_profile_rating(

    user_id

):


    player = get_player(

        user_id

    )



    return {


        "rating":

        player.get(

            "rating",

            1000

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

        )

    }








# =========================
# MINI APP DATA
# =========================


def get_battle_card(

    user_id

):


    data = get_profile_rating(

        user_id

    )


    return {


        "rating":

        data["rating"],


        "wins":

        data["wins"],


        "losses":

        data["losses"],


        "history":

        get_battle_history(

            user_id

        )

    }