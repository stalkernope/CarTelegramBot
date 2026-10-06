from database import (
    get_player,
    update_player
)





# =========================
# BLACKLIST
# =========================


BLACKLIST = [


    {

        "rank":15,

        "name":"🌑 Razor",

        "car":"Shadow GT",

        "power":2500,

        "reward_coins":5000,

        "reward_car":"Shadow GT"

    },


    {

        "rank":14,

        "name":"⚡ Bull",

        "car":"Lightning X",

        "power":3500,

        "reward_coins":7000,

        "reward_car":"Lightning X"

    },


    {

        "rank":10,

        "name":"🔥 Ronnie",

        "car":"Supra MK5",

        "power":6000,

        "reward_coins":15000,

        "reward_car":"Supra MK5"

    },


    {

        "rank":5,

        "name":"👑 Baron",

        "car":"Black Phantom",

        "power":9000,

        "reward_coins":30000,

        "reward_car":"Black Phantom"

    },


    {

        "rank":1,

        "name":"🏆 Black King",

        "car":"Legend X1",

        "power":15000,

        "reward_coins":100000,

        "reward_car":"Legend X1"

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



    defeated = player.get(

        "blacklist_defeated",

        []

    )



    for boss in BLACKLIST:


        if boss["rank"] not in defeated:


            return boss



    return None







# =========================
# BOSS DEFEATED
# =========================


def defeat_boss(

    user_id,

    rank

):


    player = get_player(

        user_id

    )



    if "blacklist_defeated" not in player:


        player["blacklist_defeated"] = []





    if rank not in player["blacklist_defeated"]:


        player["blacklist_defeated"].append(

            rank

        )



    update_player(

        user_id,

        player

    )








# =========================
# CHECK UNLOCK
# =========================


def is_unlocked(

    user_id,

    rank

):


    player = get_player(

        user_id

    )



    defeated = player.get(

        "blacklist_defeated",

        []

    )



    if rank == 15:


        return True



    previous = rank + 1



    return previous in defeated







# =========================
# TEXT
# =========================


def blacklist_text(user_id):


    player = get_player(

        user_id

    )



    defeated = player.get(

        "blacklist_defeated",

        []

    )



    text = (

        "🏆 <b>BLACKLIST</b>\n\n"

    )



    for boss in BLACKLIST:


        status = "✅" if boss["rank"] in defeated else "🔒"



        text += (

            f"{status} #{boss['rank']} "

            f"{boss['name']}\n"

            f"🚗 {boss['car']}\n"

            f"⚡ {boss['power']}\n\n"

        )



    return text