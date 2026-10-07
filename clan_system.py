# =========================
# CLAN SYSTEM FINAL
# =========================


import json
import os



from database import (
    get_player,
    update_player
)







# =========================
# DATABASE
# =========================


CLAN_FILE = "clans.json"








def load_clans():


    if not os.path.exists(

        CLAN_FILE

    ):


        return {}



    try:


        with open(

            CLAN_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except:


        return {}








def save_clans(data):


    with open(

        CLAN_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









# =========================
# CREATE CLAN
# =========================


def create_clan(

    user_id,

    name

):


    clans = load_clans()



    for clan in clans.values():


        if clan["name"].lower() == name.lower():


            return False






    clan_id = str(

        len(clans)+1

    )



    clans[clan_id] = {


        "id":

        clan_id,


        "name":

        name,


        "leader":

        user_id,


        "members":

        [

            user_id

        ],


        "level":

        1,


        "power":

        100

    }



    save_clans(

        clans

    )





    player = get_player(

        user_id

    )


    player["clan"] = clan_id



    update_player(

        user_id,

        player

    )



    return clans[clan_id]









# =========================
# JOIN CLAN
# =========================


def join_clan(

    user_id,

    clan_id

):


    clans = load_clans()



    if clan_id not in clans:


        return False





    clan = clans[clan_id]



    if user_id not in clan["members"]:


        clan["members"].append(

            user_id

        )



    clans[clan_id] = clan



    save_clans(

        clans

    )





    player = get_player(

        user_id

    )


    player["clan"] = clan_id



    update_player(

        user_id,

        player

    )



    return True







# =========================
# LEAVE CLAN
# =========================


def leave_clan(user_id):


    player = get_player(

        user_id

    )


    clan_id = player.get(

        "clan"

    )



    if not clan_id:


        return False





    clans = load_clans()



    if clan_id in clans:


        if user_id in clans[clan_id]["members"]:


            clans[clan_id]["members"].remove(

                user_id

            )



        save_clans(

            clans

        )





    player["clan"] = None



    update_player(

        user_id,

        player

    )



    return True







# =========================
# GET PLAYER CLAN
# =========================


def get_player_clan(user_id):


    player = get_player(

        user_id

    )


    clan_id = player.get(

        "clan"

    )



    if not clan_id:


        return None





    clans = load_clans()



    return clans.get(

        clan_id

    )









# =========================
# CLAN TEXT
# =========================


def clan_text(user_id):


    clan = get_player_clan(

        user_id

    )



    if not clan:


        return """

⚔️ <b>КЛАН</b>


У тебя нет клана.


Создай свой или вступи в существующий.

"""





    return f"""

⚔️ <b>{clan['name']}</b>


👑 Лидер:

{clan['leader']}


👥 Участники:

{len(clan['members'])}


⭐ Уровень:

{clan['level']}


🔥 Сила:

{clan['power']}

"""









# =========================
# TOP CLANS
# =========================


def top_clans():


    clans = load_clans()



    result = list(

        clans.values()

    )



    result.sort(

        key=lambda x:

        x.get(

            "power",

            0

        ),

        reverse=True

    )



    return result[:10]