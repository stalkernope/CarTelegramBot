import json
import os
import random



BOSS_FILE = "boss_races.json"




# =========================
# БОССЫ
# =========================


BOSSES = [

    {

        "id":

        "night_king",


        "name":

        "🌑 Night King",


        "car":

        "Shadow GT",


        "power":

        2000,


        "reward":

        "🔥 Shadow Engine"

    },


    {

        "id":

        "speed_lord",


        "name":

        "⚡ Speed Lord",


        "car":

        "Lightning X",


        "power":

        5000,


        "reward":

        "🚀 Turbo Ultimate"

    },


    {

        "id":

        "car_legend",


        "name":

        "👑 Car Legend",


        "car":

        "Legend X1",


        "power":

        10000,


        "reward":

        "🏆 Legendary Car"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_boss():

    if not os.path.exists(BOSS_FILE):

        return {}



    try:

        with open(

            BOSS_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_boss(data):

    with open(

        BOSS_FILE,

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


def get_boss_player(user_id):

    data = load_boss()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "defeated":

            [],


            "wins":

            0,


            "rewards":

            []

        }


        save_boss(data)



    return data[uid]




# =========================
# ВЫБОР БОССА
# =========================


def get_boss(index=None):


    if index is not None:


        return BOSSES[index]



    return random.choice(

        BOSSES

    )




# =========================
# БИТВА С БОССОМ
# =========================


def fight_boss(

    user_id,

    player_power,

    boss_id

):

    data = load_boss()


    player = get_boss_player(

        user_id

    )



    boss = None



    for item in BOSSES:


        if item["id"] == boss_id:

            boss = item



    if not boss:

        return False




    player_score = (

        player_power

        +

        random.randint(

            -500,

            500

        )

    )



    boss_score = (

        boss["power"]

        +

        random.randint(

            -500,

            500

        )

    )



    if player_score >= boss_score:


        if boss_id not in player["defeated"]:


            player["defeated"].append(

                boss_id

            )


            player["rewards"].append(

                boss["reward"]

            )



        player["wins"] += 1



        result = {

            "win":

            True,


            "boss":

            boss["name"],


            "reward":

            boss["reward"]

        }


    else:


        result = {

            "win":

            False,


            "boss":

            boss["name"],


            "reward":

            None

        }




    data[str(user_id)] = player


    save_boss(data)



    return result




# =========================
# ТЕКСТ
# =========================


def boss_text(user_id):

    player = get_boss_player(

        user_id

    )


    return (

        "👑 <b>БОССЫ</b>\n\n"

        f"🏆 Победы: {player['wins']}\n"

        f"🔥 Побеждено боссов: "

        f"{len(player['defeated'])}\n\n"

        "Стань легендой трассы!"

    )