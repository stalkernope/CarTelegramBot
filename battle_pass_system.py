import json
import os



PASS_FILE = "battle_pass.json"




# =========================
# НАГРАДЫ
# =========================


PASS_REWARDS = [

    {
        "level": 1,

        "free":
        "💰 1000 монет",

        "premium":
        "🎁 Rare Case"

    },


    {
        "level": 5,

        "free":
        "🔩 10 металла",

        "premium":
        "🔥 Turbo Part"

    },


    {
        "level": 10,

        "free":
        "💎 5000 монет",

        "premium":
        "🚗 Exclusive Car"

    },


    {
        "level": 25,

        "free":
        "🎁 Legendary Case",

        "premium":
        "👑 Mythic Car"

    },


    {
        "level": 50,

        "free":
        "🏆 Season Trophy",

        "premium":
        "🚀 Ultimate Car"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_pass():

    if not os.path.exists(PASS_FILE):

        return {}


    try:

        with open(
            PASS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_pass(data):

    with open(
        PASS_FILE,
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
# ИГРОК
# =========================


def get_player_pass(user_id):

    data = load_pass()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "xp": 0,

            "level": 1,

            "premium": False,

            "claimed": []

        }


        save_pass(data)



    return data[uid]




# =========================
# ДОБАВИТЬ ОПЫТ
# =========================


def add_pass_xp(

    user_id,

    amount

):

    data = load_pass()


    player = get_player_pass(

        user_id

    )


    uid = str(user_id)



    player["xp"] += amount



    need = player["level"] * 200



    if player["xp"] >= need:


        player["xp"] -= need

        player["level"] += 1



    data[uid] = player


    save_pass(data)



    return player




# =========================
# КУПИТЬ PREMIUM
# =========================


def activate_premium(user_id):

    data = load_pass()


    player = get_player_pass(

        user_id

    )


    player["premium"] = True



    data[str(user_id)] = player


    save_pass(data)



    return True




# =========================
# ДОСТУПНЫЕ НАГРАДЫ
# =========================


def available_rewards(user_id):

    player = get_player_pass(

        user_id

    )


    rewards = []



    for reward in PASS_REWARDS:


        if player["level"] >= reward["level"]:


            if reward["level"] not in player["claimed"]:


                rewards.append(

                    reward

                )



    return rewards




# =========================
# ПОЛУЧИТЬ НАГРАДУ
# =========================


def claim_reward(

    user_id,

    level

):

    data = load_pass()


    player = get_player_pass(

        user_id

    )



    for reward in PASS_REWARDS:


        if reward["level"] == level:


            if level in player["claimed"]:

                return False



            player["claimed"].append(

                level

            )


            data[str(user_id)] = player


            save_pass(data)



            return reward



    return False




# =========================
# ТЕКСТ
# =========================


def battle_pass_text(user_id):

    player = get_player_pass(

        user_id

    )


    status = (

        "💎 PREMIUM"

        if player["premium"]

        else

        "🆓 FREE"

    )



    return (

        "🎟 <b>BATTLE PASS</b>\n\n"

        f"⭐ Уровень: {player['level']}\n"

        f"✨ XP: {player['xp']}\n"

        f"🎫 Тип: {status}\n\n"

        "🎁 Получай награды за прогресс!"

    )