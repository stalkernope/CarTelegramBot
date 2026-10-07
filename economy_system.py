# =========================
# ECONOMY SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player
)







# =========================
# COINS
# =========================


def get_coins(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "coins",

        0

    )







def add_coins(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    player["coins"] = (

        player.get(

            "coins",

            0

        )

        +

        amount

    )



    update_player(

        user_id,

        player

    )



    return player["coins"]







def spend_coins(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    if player.get(

        "coins",

        0

    ) < amount:


        return False





    player["coins"] -= amount



    update_player(

        user_id,

        player

    )



    return True







# =========================
# GEMS
# =========================


def get_gems(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "gems",

        0

    )








def add_gems(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    player["gems"] = (

        player.get(

            "gems",

            0

        )

        +

        amount

    )



    update_player(

        user_id,

        player

    )



    return player["gems"]







def spend_gems(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    if player.get(

        "gems",

        0

    ) < amount:


        return False





    player["gems"] -= amount



    update_player(

        user_id,

        player

    )



    return True







# =========================
# RACE REWARD
# =========================


def give_race_reward(

    user_id,

    win=True

):


    if win:


        coins = 1000

        gems = 5

        xp = 200



    else:


        coins = 200

        gems = 0

        xp = 50





    player = get_player(

        user_id

    )



    player["coins"] += coins



    player["gems"] += gems



    player["xp"] += xp



    update_player(

        user_id,

        player

    )



    return {


        "coins":

        coins,


        "gems":

        gems,


        "xp":

        xp

    }








# =========================
# DAILY REWARD
# =========================


def daily_reward(user_id):


    player = get_player(

        user_id

    )



    if "daily" not in player:


        player["daily"] = False





    if player["daily"]:


        return {


            "success":

            False,


            "message":

            "Сегодня уже получено"

        }







    player["daily"] = True



    player["coins"] += 3000



    player["gems"] += 10



    update_player(

        user_id,

        player

    )



    return {


        "success":

        True,


        "coins":

        3000,


        "gems":

        10

    }








# =========================
# RESET DAILY
# =========================


def reset_daily(user_id):


    player = get_player(

        user_id

    )


    player["daily"] = False



    update_player(

        user_id,

        player

    )