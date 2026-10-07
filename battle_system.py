# =========================
# BATTLE SYSTEM COMPLETE FINAL
# CAR LEGENDS
# =========================


import random
import time



from database import (
    get_player,
    update_player,
    add_win,
    add_loss,
    add_coins,
    add_xp,
    add_battle_history
)



from garage_system import (
    get_race_car
)



from tuning import (
    get_upgraded_car_stats
)







# =========================
# CONFIG
# =========================


WIN_REWARD = 5000

WIN_XP = 250

LOSE_XP = 50


START_RATING = 1000


BATTLE_COOLDOWN = 60







# =========================
# CAR POWER
# =========================


def calculate_power(car):


    if not car:

        return 0



    return (

        car.get("power", 0)

        +

        car.get("speed", 0)

        +

        car.get("handling", 0)

        +

        car.get("nitro", 0)

    )







# =========================
# PLAYER BATTLE DATA
# =========================


def get_battle_power(user_id):


    car = get_race_car(

        user_id

    )



    if not car:


        return {


            "car": None,

            "power": 0

        }






    stats = get_upgraded_car_stats(

        user_id,

        car["name"]

    )



    return {


        "car": car["name"],

        "power": calculate_power(stats)

    }







# =========================
# CHECK COOLDOWN
# =========================


def check_cooldown(user_id):


    player = get_player(

        user_id

    )


    last = player.get(

        "last_battle",

        0

    )



    return (

        time.time()

        -

        last

    ) >= BATTLE_COOLDOWN
    
    
    # =========================
# ELO RATING
# =========================


def calculate_elo(

    winner_rating,

    loser_rating

):


    k = 32



    expected_win = (

        1

        /

        (

            1

            +

            10 ** (

                (

                    loser_rating

                    -

                    winner_rating

                )

                /

                400

            )

        )

    )



    change = int(

        k

        *

        (

            1

            -

            expected_win

        )

    )



    return change







# =========================
# FIND OPPONENT
# =========================


def find_opponent(

    user_id,

    players

):


    player = get_player(

        user_id

    )


    rating = player.get(

        "rating",

        START_RATING

    )



    candidates = []



    for opponent_id in players:


        if str(opponent_id) == str(user_id):


            continue





        opponent = get_player(

            opponent_id

        )



        opponent_rating = opponent.get(

            "rating",

            START_RATING

        )



        if abs(

            rating - opponent_rating

        ) <= 300:


            candidates.append(

                opponent_id

            )





    if not candidates:


        return None





    return random.choice(

        candidates

    )









# =========================
# START BATTLE
# =========================


def start_battle(

    player_one,

    player_two

):


    if str(player_one) == str(player_two):


        return {


            "success":False,

            "text":

            "❌ Нельзя сражаться с собой"

        }






    if not check_cooldown(

        player_one

    ):


        return {


            "success":False,

            "text":

            "⏳ Подожди перед следующим боем"

        }






    if not check_cooldown(

        player_two

    ):


        return {


            "success":False,

            "text":

            "⏳ Соперник недавно играл"

        }







    first = get_battle_power(

        player_one

    )


    second = get_battle_power(

        player_two

    )





    if not first["car"] or not second["car"]:


        return {


            "success":False,

            "text":

            "❌ Нет активной машины"

        }







    if first["power"] >= second["power"]:


        winner = player_one

        loser = player_two



    else:


        winner = player_two

        loser = player_one






    return finish_battle(

        winner,

        loser,

        first,

        second

    )
    
    
    # =========================
# FINISH BATTLE
# =========================


def finish_battle(

    winner,

    loser,

    first,

    second

):


    winner_data = get_player(

        winner

    )


    loser_data = get_player(

        loser

    )



    winner_rating = winner_data.get(

        "rating",

        START_RATING

    )


    loser_rating = loser_data.get(

        "rating",

        START_RATING

    )



    elo_change = calculate_elo(

        winner_rating,

        loser_rating

    )





    update_rating(

        winner,

        elo_change

    )


    update_rating(

        loser,

        -elo_change

    )





    add_win(

        winner

    )


    add_loss(

        loser

    )



    add_coins(

        winner,

        WIN_REWARD

    )


    add_xp(

        winner,

        WIN_XP

    )


    add_xp(

        loser,

        LOSE_XP

    )






    now = time.time()



    winner_player = get_player(

        winner

    )


    loser_player = get_player(

        loser

    )



    winner_player["last_battle"] = now

    loser_player["last_battle"] = now



    update_player(

        winner,

        winner_player

    )


    update_player(

        loser,

        loser_player

    )






    result = {


        "winner":

        winner,


        "loser":

        loser,


        "winner_car":

        first["car"],


        "loser_car":

        second["car"],


        "reward":

        WIN_REWARD,


        "time":

        now

    }






    add_battle_history(

        winner,

        result

    )


    add_battle_history(

        loser,

        result

    )






    return {


        "success":

        True,


        "winner":

        winner,


        "loser":

        loser,


        "reward":

        WIN_REWARD,


        "rating_change":

        elo_change

    }








# =========================
# UPDATE RATING
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

            START_RATING

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


def get_history(

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
# PROFILE DATA
# =========================


def get_battle_profile(

    user_id

):


    player = get_player(

        user_id

    )



    return {


        "rating":

        player.get(

            "rating",

            START_RATING

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



        "history":

        get_history(

            user_id

        )

    }








# =========================
# MINI APP DATA
# =========================


def get_battle_card(

    user_id

):


    profile = get_battle_profile(

        user_id

    )



    return {


        "rating":

        profile["rating"],


        "wins":

        profile["wins"],


        "losses":

        profile["losses"],


        "history":

        profile["history"]

    }