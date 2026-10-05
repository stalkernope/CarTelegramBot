import json
import os



MISSION_FILE = "missions.json"




# =========================
# ГЛАВЫ КАРЬЕРЫ
# =========================


CHAPTERS = [

    {

        "id": 1,

        "name": "🏁 Первые шаги",

        "missions": [

            {

                "id": "race_first",

                "name":
                "Первая гонка",

                "type":
                "wins",

                "need":
                1,

                "reward":
                1000

            },


            {

                "id": "collect_three",

                "name":
                "Собрать гараж",

                "type":
                "cars",

                "need":
                3,

                "reward":
                3000

            }

        ]

    },



    {

        "id": 2,

        "name": "🔥 Уличный чемпион",

        "missions": [

            {

                "id": "wins_10",

                "name":
                "10 побед",

                "type":
                "wins",

                "need":
                10,

                "reward":
                10000

            },


            {

                "id": "level_5",

                "name":
                "Получить 5 уровень",

                "type":
                "level",

                "need":
                5,

                "reward":
                15000

            }

        ]

    },



    {

        "id": 3,

        "name": "👑 Легенда трассы",

        "missions": [

            {

                "id":
                "wins_100",

                "name":
                "100 побед",

                "type":
                "wins",

                "need":
                100,

                "reward":
                50000

            }

        ]

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_missions():

    if not os.path.exists(MISSION_FILE):

        return {}



    try:

        with open(
            MISSION_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_missions(data):

    with open(
        MISSION_FILE,
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
# ПРОГРЕСС ИГРОКА
# =========================


def get_progress(
    user_id
):

    data = load_missions()


    uid = str(user_id)



    if uid not in data:

        data[uid] = {

            "completed": []

        }


        save_missions(
            data
        )



    return data[uid]




# =========================
# ПРОВЕРКА МИССИИ
# =========================


def check_mission(
    player,
    mission
):


    if mission["type"] == "wins":

        return (

            player["wins"]

            >=

            mission["need"]

        )



    if mission["type"] == "cars":

        return (

            len(player["garage"])

            >=

            mission["need"]

        )



    if mission["type"] == "level":

        return (

            player["level"]

            >=

            mission["need"]

        )



    return False




# =========================
# ПРОВЕРИТЬ ВСЁ
# =========================


def check_all_missions(
    user_id,
    player
):

    data = load_missions()


    uid = str(user_id)



    progress = get_progress(
        user_id
    )


    completed = []



    for chapter in CHAPTERS:


        for mission in chapter["missions"]:


            mid = mission["id"]



            if mid in progress["completed"]:

                continue



            if check_mission(

                player,

                mission

            ):


                progress["completed"].append(
                    mid
                )


                completed.append(
                    mission
                )



    data[uid] = progress



    save_missions(
        data
    )



    return completed




# =========================
# ТЕКСТ КАРЬЕРЫ
# =========================


def career_text(
    user_id
):

    progress = get_progress(
        user_id
    )


    text = (

        "🏎 <b>CAR LEGENDS CAREER</b>\n\n"

    )



    for chapter in CHAPTERS:


        text += (

            chapter["name"]

            +

            "\n"

        )



        for mission in chapter["missions"]:


            if mission["id"] in progress["completed"]:

                text += (

                    "✅ "

                )

            else:

                text += (

                    "🔒 "

                )



            text += (

                mission["name"]

                +

                "\n"

            )


        text += "\n"



    return text
    
    # =========================
# НАГРАДА ЗА МИССИЮ
# =========================


def claim_mission_reward(
    user_id,
    mission_id,
    player
):

    data = load_missions()

    uid = str(user_id)


    progress = get_progress(
        user_id
    )


    if mission_id not in progress["completed"]:

        return False



    for chapter in CHAPTERS:

        for mission in chapter["missions"]:

            if mission["id"] == mission_id:


                reward = mission["reward"]


                player["money"] += reward


                progress["completed"].remove(
                    mission_id
                )


                data[uid] = progress


                save_missions(
                    data
                )


                return reward



    return False