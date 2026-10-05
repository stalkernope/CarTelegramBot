import json
import os
from datetime import datetime



EVENT_FILE = "events.json"




# =========================
# СОБЫТИЯ
# =========================


EVENTS = [

    {

        "id": "weekend_race",

        "name": "🏁 Гонка выходного дня",

        "description":

        "Выиграй 10 гонок и получи редкий кейс",

        "type":

        "wins",

        "need":

        10,

        "reward":

        "💎 Rare Case"

    },


    {

        "id": "collector",

        "name": "🚗 Неделя коллекционера",

        "description":

        "Собери 5 новых машин",

        "type":

        "cars",

        "need":

        5,

        "reward":

        "🔥 Legendary Case"

    },


    {

        "id": "champion",

        "name": "👑 Чемпион сезона",

        "description":

        "Получи 50 побед",

        "type":

        "wins",

        "need":

        50,

        "reward":

        "🏎 Эксклюзивная машина"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_events():

    if not os.path.exists(EVENT_FILE):

        return {}



    try:

        with open(
            EVENT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_events(data):

    with open(
        EVENT_FILE,
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
# ТЕКУЩИЕ СОБЫТИЯ
# =========================


def active_events():

    return EVENTS




# =========================
# ПРОГРЕСС
# =========================


def get_event_progress(user_id):

    data = load_events()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "completed": []

        }


        save_events(
            data
        )



    return data[uid]




# =========================
# ПРОВЕРКА СОБЫТИЯ
# =========================


def check_event(
    player,
    event
):


    if event["type"] == "wins":

        return (

            player["wins"]

            >=

            event["need"]

        )



    if event["type"] == "cars":

        return (

            len(player["garage"])

            >=

            event["need"]

        )



    return False




# =========================
# ПРОВЕРИТЬ ВСЕ
# =========================


def check_events(
    user_id,
    player
):

    data = load_events()


    progress = get_event_progress(
        user_id
    )


    completed = []



    for event in EVENTS:


        if event["id"] in progress["completed"]:

            continue



        if check_event(

            player,

            event

        ):


            progress["completed"].append(

                event["id"]

            )


            completed.append(

                event

            )



    data[str(user_id)] = progress


    save_events(
        data
    )


    return completed




# =========================
# ТЕКСТ
# =========================


def events_text():

    text = (

        "🔥 <b>АКТИВНЫЕ СОБЫТИЯ</b>\n\n"

    )



    for event in EVENTS:


        text += (

            f"{event['name']}\n"

            f"📌 {event['description']}\n"

            f"🎁 {event['reward']}\n\n"

        )



    return text