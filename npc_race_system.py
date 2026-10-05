import json
import os
import random



NPC_FILE = "npc_races.json"




# =========================
# NPC СОПЕРНИКИ
# =========================


NPCS = [

    {
        "id": "street_kid",

        "name": "😈 Street Kid",

        "level": 1,

        "power": 300,

        "reward": 500

    },


    {
        "id": "speed_master",

        "name": "🔥 Speed Master",

        "level": 5,

        "power": 800,

        "reward": 3000

    },


    {
        "id": "shadow",

        "name": "🌑 Shadow Racer",

        "level": 10,

        "power": 1500,

        "reward": 10000

    },


    {
        "id": "legend",

        "name": "👑 The Legend",

        "level": 20,

        "power": 3000,

        "reward": 50000

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_npc():

    if not os.path.exists(NPC_FILE):

        return {}


    try:

        with open(

            NPC_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_npc(data):

    with open(

        NPC_FILE,

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
# ПРОФИЛЬ NPC
# =========================


def get_npc_player(user_id):

    data = load_npc()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "wins": 0,

            "bosses": [],

            "defeated": []

        }


        save_npc(data)



    return data[uid]




# =========================
# ВЫБОР СОПЕРНИКА
# =========================


def choose_npc(level):

    available = []


    for npc in NPCS:


        if npc["level"] <= level:

            available.append(npc)



    if not available:

        return NPCS[0]



    return random.choice(

        available

    )




# =========================
# ГОНКА
# =========================


def npc_race(

    user_id,

    player_power,

    level

):

    data = load_npc()


    npc = choose_npc(

        level

    )


    chance = random.randint(

        1,

        100

    )



    player_score = (

        player_power

        +

        random.randint(

            -100,

            100

        )

    )



    npc_score = (

        npc["power"]

        +

        random.randint(

            -100,

            100

        )

    )



    if player_score >= npc_score:


        result = {

            "win": True,

            "enemy": npc["name"],

            "reward": npc["reward"]

        }


        player = get_npc_player(

            user_id

        )


        player["wins"] += 1


        player["defeated"].append(

            npc["id"]

        )



    else:


        result = {

            "win": False,

            "enemy": npc["name"],

            "reward": 0

        }




    data[str(user_id)] = get_npc_player(

        user_id

    )


    save_npc(data)



    return result




# =========================
# БОССЫ
# =========================


def boss_status(user_id):

    player = get_npc_player(

        user_id

    )


    return player["defeated"]




# =========================
# ТЕКСТ
# =========================


def npc_text(user_id):

    player = get_npc_player(

        user_id

    )


    return (

        "🤖 <b>NPC ГОНКИ</b>\n\n"

        f"🏆 Победы: {player['wins']}\n"

        f"👑 Побеждено соперников: "

        f"{len(player['defeated'])}"

    )