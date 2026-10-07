# =========================
# BATTLE SYSTEM FINAL
# =========================


import random



from database import (
    get_player,
    add_win,
    add_loss,
    add_coins,
    add_xp
)


from car_database import (
    get_car
)








# =========================
# PLAYER POWER
# =========================


def get_car_power(car_name):


    car = get_car(

        car_name

    )



    if not car:


        return 0



    power = (

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

    )


    return power







# =========================
# BATTLE START
# =========================


def start_battle(

    player_id,

    enemy_id

):


    player = get_player(

        player_id

    )


    enemy = get_player(

        enemy_id

    )





    player_car = player.get(

        "main_car"

    )


    enemy_car = enemy.get(

        "main_car"

    )





    if not player_car:


        return {


            "success":

            False,


            "message":

            "Нет главной машины"

        }






    if not enemy_car:


        return {


            "success":

            False,


            "message":

            "У противника нет машины"

        }







    player_power = get_car_power(

        player_car

    )



    enemy_power = get_car_power(

        enemy_car

    )





    player_bonus = random.randint(

        -100,

        100

    )



    enemy_bonus = random.randint(

        -100,

        100

    )





    final_player = player_power + player_bonus



    final_enemy = enemy_power + enemy_bonus






    if final_player >= final_enemy:


        winner = player_id

        loser = enemy_id

        win = True



    else:


        winner = enemy_id

        loser = player_id

        win = False






    add_win(

        winner

    )


    add_loss(

        loser

    )



    add_coins(

        winner,

        2000

    )


    add_xp(

        winner,

        300

    )





    return {


        "success":

        True,


        "winner":

        winner,


        "loser":

        loser,


        "player_power":

        final_player,


        "enemy_power":

        final_enemy,


        "win":

        win

    }









# =========================
# BATTLE TEXT
# =========================


def battle_text(result, user_id):


    if not result.get(

        "success"

    ):


        return result.get(

            "message"

        )





    if result["winner"] == user_id:


        return f"""

🏆 <b>ПОБЕДА</b>


⚡ Твоя сила:

{result['player_power']}


💰 Награда:

+2000 монет


🔥 XP:

+300

"""



    else:


        return f"""

❌ <b>ПОРАЖЕНИЕ</b>


Противник оказался сильнее.


Твоя сила:

{result['player_power']}

Сила врага:

{result['enemy_power']}

"""








# =========================
# QUICK BATTLE
# =========================


def quick_battle(

    user_id,

    enemy_id

):


    return start_battle(

        user_id,

        enemy_id

    )