# =========================
# BATTLES COMPLETE
# CAR LEGENDS
# =========================


import random
import time



from database import (
    get_player,
    update_player
)



from Battle_system import (
    start_battle,
    find_opponent
)







# =========================
# CONFIG
# =========================


ARENA_REWARD = 1000


WIN_STREAK_REWARD = 5000


TOURNAMENT_PLAYERS = 8







# =========================
# ARENA QUEUE
# =========================


ARENA_QUEUE = []







# =========================
# JOIN ARENA
# =========================


def join_arena(

    user_id

):


    if user_id not in ARENA_QUEUE:


        ARENA_QUEUE.append(

            user_id

        )



    return {


        "success":

        True,


        "players":

        len(

            ARENA_QUEUE

        )

    }









# =========================
# LEAVE ARENA
# =========================


def leave_arena(

    user_id

):


    if user_id in ARENA_QUEUE:


        ARENA_QUEUE.remove(

            user_id

        )



    return True







# =========================
# FIND ARENA MATCH
# =========================


def find_match(

):


    if len(ARENA_QUEUE) < 2:


        return None





    player_one = ARENA_QUEUE.pop(0)


    player_two = ARENA_QUEUE.pop(0)





    return {


        "player_one":

        player_one,


        "player_two":

        player_two

    }







# =========================
# START ARENA BATTLE
# =========================


def start_arena_battle(

    player_one,

    player_two

):


    result = start_battle(

        player_one,

        player_two

    )



    return result
    
    # =========================
# WIN STREAK
# =========================


def update_win_streak(

    user_id,

    win

):


    player = get_player(

        user_id

    )



    if "win_streak" not in player:


        player["win_streak"] = 0





    if win:


        player["win_streak"] += 1



    else:


        player["win_streak"] = 0






    update_player(

        user_id,

        player

    )



    return player["win_streak"]








# =========================
# ARENA REWARD
# =========================


def get_arena_reward(

    streak

):


    reward = ARENA_REWARD



    if streak >= 5:


        reward += WIN_STREAK_REWARD





    return reward







# =========================
# TOURNAMENT CREATE
# =========================


def create_tournament(

    players

):


    if len(players) < TOURNAMENT_PLAYERS:


        return {


            "success":False,

            "text":

            "❌ Недостаточно игроков"

        }







    return {


        "success":

        True,


        "players":

        players[:TOURNAMENT_PLAYERS],


        "round":

        1

    }








# =========================
# TOURNAMENT ROUND
# =========================


def tournament_round(

    tournament

):


    players = tournament.get(

        "players",

        []

    )



    random.shuffle(

        players

    )



    pairs = []



    for i in range(

        0,

        len(players),

        2

    ):


        pairs.append(

            {


                "player_one":

                players[i],


                "player_two":

                players[i+1]

            }

        )



    return pairs








# =========================
# ARENA PROFILE
# =========================


def get_arena_profile(

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

        ),


        "streak":

        player.get(

            "win_streak",

            0

        )

    }








# =========================
# MINI APP DATA
# =========================


def get_battles_data(

    user_id

):


    return {


        "arena":

        get_arena_profile(

            user_id

        ),


        "queue":

        len(

            ARENA_QUEUE

        )

    }