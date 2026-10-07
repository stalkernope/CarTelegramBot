# =========================
# BLACKLIST SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player
)







# =========================
# BLACKLIST BOSSES
# =========================


BLACKLIST = [


    {


        "id":1,


        "name":

        "Shadow",


        "car":

        "Nissan GTR",


        "need_wins":

        0,


        "reward":

        5000,


        "power":

        600

    },



    {


        "id":2,


        "name":

        "Night Wolf",


        "car":

        "BMW M4",


        "need_wins":

        5,


        "reward":

        10000,


        "power":

        850

    },



    {


        "id":3,


        "name":

        "Dark Legend",


        "car":

        "Bugatti Chiron",


        "need_wins":

        15,


        "reward":

        25000,


        "power":

        1300

    },


    {


        "id":4,


        "name":

        "Final Boss",


        "car":

        "Koenigsegg Jesko",


        "need_wins":

        30,


        "reward":

        100000,


        "power":

        1800

    }

]








# =========================
# GET BLACKLIST
# =========================


def get_blacklist():


    return BLACKLIST







# =========================
# CURRENT BOSS
# =========================


def get_current_boss(user_id):


    player = get_player(

        user_id

    )



    wins = player.get(

        "wins",

        0

    )



    available = None





    for boss in BLACKLIST:


        if wins >= boss["need_wins"]:


            available = boss



    if not available:


        available = BLACKLIST[0]



    return available








# =========================
# BLACKLIST TEXT
# =========================


def blacklist_text(user_id):


    player = get_player(

        user_id

    )


    wins = player.get(

        "wins",

        0

    )



    text = (

        "🏆 <b>BLACKLIST</b>\n\n"

    )



    for boss in BLACKLIST:



        if wins >= boss["need_wins"]:


            status = "🔓"



        else:


            status = "🔒"





        text += (

            f"{status} {boss['name']}\n"

            f"🚗 {boss['car']}\n"

            f"⚡ Power: {boss['power']}\n"

            f"🏁 Нужно побед: {boss['need_wins']}\n\n"

        )



    return text







# =========================
# DEFEAT BOSS
# =========================


def defeat_boss(

    user_id,

    boss_id

):


    player = get_player(

        user_id

    )



    if "bosses" not in player:


        player["bosses"] = []





    if boss_id not in player["bosses"]:


        player["bosses"].append(

            boss_id

        )



    update_player(

        user_id,

        player

    )



    for boss in BLACKLIST:


        if boss["id"] == boss_id:


            return boss



    return None







# =========================
# CHECK DEFEATED
# =========================


def is_boss_defeated(

    user_id,

    boss_id

):


    player = get_player(

        user_id

    )


    return boss_id in player.get(

        "bosses",

        []

    )