# =========================
# CLAN WAR SYSTEM FINAL
# =========================


import random



from clan_system import (
    load_clans,
    save_clans,
    get_player_clan
)








# =========================
# CLAN WAR CONFIG
# =========================


WAR_REWARDS = {


    "coins":

    25000,


    "xp":

    2000

}








# =========================
# CLAN POWER
# =========================


def get_clan_power(clan):


    if not clan:


        return 0





    power = clan.get(

        "power",

        0

    )



    members = len(

        clan.get(

            "members",

            []

        )

    )



    return power + members * 100







# =========================
# FIND ENEMY
# =========================


def find_enemy_clan(clan_id):


    clans = load_clans()



    if clan_id not in clans:


        return None





    enemies = []



    for cid, clan in clans.items():


        if cid != clan_id:


            enemies.append(

                clan

            )



    if not enemies:


        return None



    return random.choice(

        enemies

    )








# =========================
# START WAR
# =========================


def start_clan_war(user_id):


    clan = get_player_clan(

        user_id

    )



    if not clan:


        return {


            "success":

            False,


            "message":

            "Нет клана"

        }







    enemy = find_enemy_clan(

        clan["id"]

    )



    if not enemy:


        return {


            "success":

            False,


            "message":

            "Нет соперников"

        }







    my_power = get_clan_power(

        clan

    )



    enemy_power = get_clan_power(

        enemy

    )






    if my_power >= enemy_power:


        winner = clan


        loser = enemy


        win = True



    else:


        winner = enemy


        loser = clan


        win = False







    return {


        "success":

        True,


        "winner":

        winner["name"],


        "loser":

        loser["name"],


        "my_power":

        my_power,


        "enemy_power":

        enemy_power,


        "win":

        win

    }









# =========================
# WAR TEXT
# =========================


def clan_war_text(user_id):


    result = start_clan_war(

        user_id

    )



    if not result["success"]:


        return (

            "⚔️ "

            +

            result["message"]

        )





    if result["win"]:


        status = "🏆 ПОБЕДА"



    else:


        status = "❌ ПОРАЖЕНИЕ"






    return f"""

⚔️ <b>ВОЙНА КЛАНОВ</b>


{status}


🔥 Твой клан:

Сила: {result['my_power']}


⚔️ Враг:

Сила: {result['enemy_power']}


🏆 Победитель:

{result['winner']}

"""








# =========================
# SAVE WAR RESULT
# =========================


def save_war_result(

    clan_id,

    result

):


    clans = load_clans()



    if clan_id not in clans:


        return False





    clan = clans[clan_id]



    if "wars" not in clan:


        clan["wars"] = []





    clan["wars"].append(

        result

    )



    clan["wars"] = clan["wars"][-20:]



    clans[clan_id] = clan



    save_clans(

        clans

    )



    return True