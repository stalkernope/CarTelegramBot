import json
import os



ACH_FILE = "achievements.json"



# =========================
# ДОСТИЖЕНИЯ
# =========================


ACHIEVEMENTS = [

    {
        "id": "first_win",

        "name": "🏁 Первая победа",

        "description":
        "Выиграть первую гонку",

        "type":
        "wins",

        "need":
        1,

        "reward":
        100,

        "rarity":
        "Common"
    },


    {
        "id": "racer_10",

        "name": "🔥 Гонщик",

        "description":
        "Получить 10 побед",

        "type":
        "wins",

        "need":
        10,

        "reward":
        500,

        "rarity":
        "Rare"
    },


    {
        "id": "collector",

        "name":
        "🚗 Коллекционер",

        "description":
        "Собрать 20 машин",

        "type":
        "cars",

        "need":
        20,

        "reward":
        1000,

        "rarity":
        "Epic"
    },


    {
        "id": "legend",

        "name":
        "👑 Легенда трассы",

        "description":
        "100 побед",

        "type":
        "wins",

        "need":
        100,

        "reward":
        10000,

        "rarity":
        "Legendary"
    },


    {
        "id":
        "garage_master",

        "name":
        "🏠 Король гаража",

        "description":
        "Максимальный гараж",

        "type":
        "garage",

        "need":
        5,

        "reward":
        5000,

        "rarity":
        "Mythic"
    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_achievements():

    if not os.path.exists(ACH_FILE):

        return {}


    try:

        with open(
            ACH_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_achievements(data):

    with open(
        ACH_FILE,
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
# ПРОФИЛЬ
# =========================


def get_achievement_player(user_id):

    data = load_achievements()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "completed": [],

            "points": 0

        }


        save_achievements(data)



    return data[uid]




# =========================
# ПРОВЕРКА
# =========================


def check_condition(
    player,
    achievement
):


    if achievement["type"] == "wins":

        return (

            player.get(
                "wins",
                0
            )

            >=

            achievement["need"]

        )



    if achievement["type"] == "cars":

        return (

            len(
                player.get(
                    "garage",
                    []
                )
            )

            >=

            achievement["need"]

        )



    if achievement["type"] == "garage":

        return (

            player.get(
                "garage_level",
                1
            )

            >=

            achievement["need"]

        )



    return False




# =========================
# ПРОВЕРИТЬ ВСЕ
# =========================


def check_achievements(

    user_id,

    player

):

    data = load_achievements()


    profile = get_achievement_player(
        user_id
    )


    completed = []



    for ach in ACHIEVEMENTS:


        if ach["id"] in profile["completed"]:

            continue



        if check_condition(

            player,

            ach

        ):


            profile["completed"].append(

                ach["id"]

            )


            profile["points"] += ach["reward"]



            completed.append(
                ach
            )



    data[str(user_id)] = profile


    save_achievements(data)



    return completed




# =========================
# ТЕКСТ
# =========================


def achievement_text(user_id):

    player = get_achievement_player(
        user_id
    )


    text = (

        "🏆 <b>ДОСТИЖЕНИЯ</b>\n\n"

        f"⭐ Очки: {player['points']}\n\n"

    )


    for ach in ACHIEVEMENTS:


        if ach["id"] in player["completed"]:

            status = "✅"

        else:

            status = "🔒"



        text += (

            f"{status} {ach['name']}\n"

            f"💎 {ach['rarity']}\n\n"

        )



    return text