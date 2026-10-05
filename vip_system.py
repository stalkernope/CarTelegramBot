import json
import os



VIP_FILE = "vip.json"




# =========================
# VIP УРОВНИ
# =========================


VIP_LEVELS = [

    {

        "level": 1,

        "name": "🥉 VIP Bronze",

        "need": 0,

        "bonus": 5

    },


    {

        "level": 2,

        "name": "🥈 VIP Silver",

        "need": 1000,

        "bonus": 10

    },


    {

        "level": 3,

        "name": "🥇 VIP Gold",

        "need": 5000,

        "bonus": 20

    },


    {

        "level": 4,

        "name": "💎 VIP Diamond",

        "need": 15000,

        "bonus": 35

    },


    {

        "level": 5,

        "name": "👑 VIP Legend",

        "need": 50000,

        "bonus": 50

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_vip():

    if not os.path.exists(VIP_FILE):

        return {}



    try:

        with open(

            VIP_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_vip(data):

    with open(

        VIP_FILE,

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
# ПРОФИЛЬ VIP
# =========================


def get_vip(user_id):

    data = load_vip()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "xp": 0,

            "level": 1,

            "claimed": []

        }


        save_vip(data)



    return data[uid]




# =========================
# ДОБАВИТЬ VIP XP
# =========================


def add_vip_xp(
    user_id,
    amount
):

    data = load_vip()


    uid = str(user_id)



    vip = get_vip(
        user_id
    )


    vip["xp"] += amount



    current = 1



    for level in VIP_LEVELS:


        if vip["xp"] >= level["need"]:

            current = level["level"]



    vip["level"] = current



    data[uid] = vip


    save_vip(data)



    return vip




# =========================
# БОНУС VIP
# =========================


def vip_bonus(user_id):

    vip = get_vip(
        user_id
    )


    bonus = 0



    for level in VIP_LEVELS:


        if level["level"] == vip["level"]:

            bonus = level["bonus"]



    return bonus




# =========================
# VIP СТАТУС
# =========================


def vip_status(user_id):

    vip = get_vip(
        user_id
    )


    current = VIP_LEVELS[

        vip["level"] - 1

    ]



    return (

        "👑 <b>VIP STATUS</b>\n\n"

        f"{current['name']}\n"

        f"⭐ VIP XP: {vip['xp']}\n"

        f"🔥 Бонус: +{current['bonus']}%"

    )




# =========================
# VIP НАГРАДЫ
# =========================


VIP_REWARDS = [

    {

        "level": 1,

        "reward":

        "🎁 1000 🪙"

    },


    {

        "level": 3,

        "reward":

        "💎 Rare Case"

    },


    {

        "level": 5,

        "reward":

        "🔥 Mythic Case"

    }

]




def vip_rewards_text():

    text = (

        "👑 <b>VIP НАГРАДЫ</b>\n\n"

    )


    for reward in VIP_REWARDS:


        text += (

            f"⭐ VIP {reward['level']}\n"

            f"🎁 {reward['reward']}\n\n"

        )


    return text