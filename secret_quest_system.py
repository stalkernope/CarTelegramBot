import json
import os



QUEST_FILE = "secret_quests.json"




# =========================
# СЕКРЕТНЫЕ КВЕСТЫ
# =========================


SECRET_QUESTS = [

    {

        "id":

        "first_shadow",

        "name":

        "🌑 Тень ночи",

        "description":

        "Победи Night King",

        "condition":

        "boss_night",

        "reward":

        "Shadow X"

    },


    {

        "id":

        "collector_path",

        "name":

        "🚗 Тайный коллекционер",

        "description":

        "Собери 50 машин",

        "condition":

        "cars_50",

        "reward":

        "Legend Case"

    },


    {

        "id":

        "street_master",

        "name":

        "🏁 Король улиц",

        "description":

        "Выиграй 100 гонок",

        "condition":

        "wins_100",

        "reward":

        "Street Crown"

    },


    {

        "id":

        "unknown",

        "name":

        "❓ Неизвестный вызов",

        "description":

        "Открой все регионы карты",

        "condition":

        "world_complete",

        "reward":

        "Secret Car"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_quests():

    if not os.path.exists(QUEST_FILE):

        return {}



    try:

        with open(

            QUEST_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_quests(data):

    with open(

        QUEST_FILE,

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


def get_secret_player(user_id):

    data = load_quests()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "completed": [],

            "progress": {}

        }


        save_quests(data)



    return data[uid]




# =========================
# ПРОВЕРКА УСЛОВИЙ
# =========================


def check_secret_condition(

    quest,

    stats

):


    condition = quest["condition"]



    if condition == "boss_night":

        return stats.get(

            "night_king",

            False

        )



    if condition == "cars_50":

        return stats.get(

            "cars",

            0

        ) >= 50



    if condition == "wins_100":

        return stats.get(

            "wins",

            0

        ) >= 100



    if condition == "world_complete":

        return stats.get(

            "regions",

            0

        ) >= 10



    return False




# =========================
# ПРОВЕРИТЬ КВЕСТЫ
# =========================


def check_secret_quests(

    user_id,

    stats

):

    data = load_quests()


    player = get_secret_player(

        user_id

    )



    completed = []



    for quest in SECRET_QUESTS:


        if quest["id"] in player["completed"]:

            continue



        if check_secret_condition(

            quest,

            stats

        ):


            player["completed"].append(

                quest["id"]

            )


            completed.append(

                quest

            )



    data[str(user_id)] = player


    save_quests(data)



    return completed




# =========================
# ТЕКСТ
# =========================


def secret_quest_text(user_id):

    player = get_secret_player(

        user_id

    )


    text = (

        "🕵️ <b>СЕКРЕТНЫЕ ЗАДАНИЯ</b>\n\n"

    )



    for quest in SECRET_QUESTS:


        if quest["id"] in player["completed"]:

            status = "✅"

        else:

            status = "🔒"



        text += (

            f"{status} {quest['name']}\n"

            f"🎁 Награда: {quest['reward']}\n\n"

        )



    return text