# =========================
# BOSS RACE SYSTEM FINAL
# =========================


import random



from database import (
    get_player,
    add_coins,
    add_xp,
    add_win,
    add_loss
)


from car_database import (
    get_car
)








# =========================
# BOSSES
# =========================


BOSSES = [

    {
        "id":1,

        "name":"Street King",

        "car":"Nissan GTR",

        "power":650,

        "reward":5000,

        "xp":500

    },


    {
        "id":2,

        "name":"Night Hunter",

        "car":"Lamborghini Huracan",

        "power":800,

        "reward":10000,

        "xp":1000

    },


    {
        "id":3,

        "name":"Legend Driver",

        "car":"Bugatti Chiron",

        "power":1200,

        "reward":25000,

        "xp":2000

    }

]







# =========================
# GET BOSS
# =========================


def get_boss():


    return random.choice(

        BOSSES

    )







# =========================
# PLAYER POWER
# =========================


def get_player_power(

    car_name

):


    car = get_car(

        car_name

    )



    if not car:


        return 0



    return (

        car.get(

            "power",

            0

        )

    )








# =========================
# RACE RESULT TEXT
# =========================


def race_result_text(result):


    if result["win"]:


        return f"""

🏆 <b>ПОБЕДА!</b>


🚗 Машина:
{result['car']}


💰 Награда:
+{result['reward']}


⭐ XP:
+{result['xp']}

"""


    else:


        return f"""

❌ <b>ПОРАЖЕНИЕ</b>


🚗 Машина:
{result['car']}


Противник оказался сильнее.

"""








# =========================
# NPC RACE
# =========================


def race_npc(

    user_id,

    car_name

):


    player_car = get_car(

        car_name

    )



    if not player_car:


        return {


            "win":False,

            "car":car_name,

            "reward":0,

            "xp":0

        }






    player_power = player_car.get(

        "power",

        0

    )



    enemy_power = random.randint(

        250,

        700

    )





    chance = (

        player_power /

        (

            player_power +

            enemy_power

        )

    )



    win = random.random() < chance






    if win:


        reward = random.randint(

            500,

            2000

        )


        xp = random.randint(

            100,

            300

        )


        add_coins(

            user_id,

            reward

        )


        add_xp(

            user_id,

            xp

        )


        add_win(

            user_id

        )



    else:


        reward = 0

        xp = 0


        add_loss(

            user_id

        )





    return {


        "win":win,


        "car":car_name,


        "reward":reward,


        "xp":xp

    }









# =========================
# BOSS FIGHT
# =========================


def fight_boss(

    user_id,

    car_name,

    boss_id

):


    boss = None



    for b in BOSSES:


        if b["id"] == boss_id:


            boss = b



    if not boss:


        boss = BOSSES[0]






    car = get_car(

        car_name

    )



    player_power = 0



    if car:


        player_power = car.get(

            "power",

            0

        )






    chance = (

        player_power /

        (

            player_power +

            boss["power"]

        )

    )



    win = random.random() < chance






    if win:


        add_coins(

            user_id,

            boss["reward"]

        )


        add_xp(

            user_id,

            boss["xp"]

        )


        add_win(

            user_id

        )


        reward = boss["reward"]


        xp = boss["xp"]



    else:


        add_loss(

            user_id

        )


        reward = 0

        xp = 0





    return {


        "win":win,


        "car":car_name,


        "boss":boss["name"],


        "reward":reward,


        "xp":xp

    }