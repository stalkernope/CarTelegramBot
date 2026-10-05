import json
import os
import random



CHAMP_FILE = "championship.json"




# =========================
# ЧЕМПИОНАТЫ
# =========================


CHAMPIONSHIPS = [

    {

        "id":

        "street_cup",

        "name":

        "🏁 Street Cup",

        "entry":

        0,

        "reward":

        10000

    },


    {

        "id":

        "speed_master",

        "name":

        "🔥 Speed Masters",

        "entry":

        5000,

        "reward":

        50000

    },


    {

        "id":

        "legend_tournament",

        "name":

        "👑 Legend Tournament",

        "entry":

        50000,

        "reward":

        500000

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_championship():

    if not os.path.exists(CHAMP_FILE):

        return {}



    try:

        with open(

            CHAMP_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_championship(data):

    with open(

        CHAMP_FILE,

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
# ПРОФИЛЬ ЧЕМПИОНАТА
# =========================


def get_player_champ(user_id):

    data = load_championship()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "cups":

            0,


            "points":

            0,


            "wins":

            0,


            "joined":

            []

        }


        save_championship(data)



    return data[uid]




# =========================
# ВСТУПИТЬ
# =========================


def join_championship(

    user_id,

    champ_id

):

    data = load_championship()


    player = get_player_champ(

        user_id

    )


    for champ in CHAMPIONSHIPS:


        if champ["id"] == champ_id:


            if champ_id in player["joined"]:

                return False



            player["joined"].append(

                champ_id

            )


            data[str(user_id)] = player


            save_championship(data)



            return True



    return False




# =========================
# РЕЗУЛЬТАТ ГОНКИ
# =========================


def championship_race(

    user_id,

    champ_id

):

    data = load_championship()


    player = get_player_champ(

        user_id

    )


    if champ_id not in player["joined"]:

        return False




    result = random.randint(

        1,

        100

    )



    if result <= 40:


        player["wins"] += 1

        player["points"] += 100



        outcome = "🏆 Победа!"



    else:


        player["points"] += 20


        outcome = "❌ Поражение"



    data[str(user_id)] = player


    save_championship(data)



    return outcome




# =========================
# ТОП ЧЕМПИОНАТА
# =========================


def championship_top(limit=10):

    data = load_championship()


    players = []



    for uid, player in data.items():


        players.append(

            {

                "id":

                uid,

                "points":

                player["points"],

                "wins":

                player["wins"]

            }

        )



    players.sort(

        key=lambda x:

        x["points"],

        reverse=True

    )


    return players[:limit]




# =========================
# ТЕКСТ
# =========================


def championship_text():

    text = (

        "🏆 <b>ЧЕМПИОНАТЫ</b>\n\n"

    )



    for champ in CHAMPIONSHIPS:


        text += (

            f"{champ['name']}\n"

            f"🎁 Награда: {champ['reward']}\n"

            f"💰 Вход: {champ['entry']}\n\n"

        )



    return text