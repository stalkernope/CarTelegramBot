import json
import os



COLLECTION_FILE = "collections.json"




# =========================
# КОЛЛЕКЦИИ
# =========================


COLLECTIONS = [

    {

        "id": "japan_legends",

        "name": "🇯🇵 Японские легенды",

        "cars": [

            "Skyline",

            "Supra",

            "RX-7"

        ],

        "reward":

        "🔥 +10% скорость"

    },


    {

        "id": "german_power",

        "name": "🇩🇪 Немецкая мощь",

        "cars": [

            "M3",

            "AMG",

            "911"

        ],

        "reward":

        "⚡ +10% мощность"

    },


    {

        "id": "hyper_collection",

        "name": "👑 Hyper Collection",

        "cars": [

            "Chiron",

            "Agera",

            "Jesko"

        ],

        "reward":

        "💎 Эксклюзивный титул"

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_collections():

    if not os.path.exists(COLLECTION_FILE):

        return {}



    try:

        with open(

            COLLECTION_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_collections(data):

    with open(

        COLLECTION_FILE,

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


def get_collection_player(user_id):

    data = load_collections()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "completed": [],

            "bonuses": []

        }


        save_collections(data)



    return data[uid]




# =========================
# ПРОВЕРКА
# =========================


def check_collections(

    user_id,

    garage

):

    data = load_collections()


    player = get_collection_player(

        user_id

    )


    completed = []



    for collection in COLLECTIONS:


        if collection["id"] in player["completed"]:

            continue



        ready = True



        for car in collection["cars"]:


            if car not in garage:

                ready = False



        if ready:


            player["completed"].append(

                collection["id"]

            )


            player["bonuses"].append(

                collection["reward"]

            )


            completed.append(

                collection

            )



    data[str(user_id)] = player


    save_collections(data)



    return completed




# =========================
# БОНУСЫ
# =========================


def collection_bonus(user_id):

    player = get_collection_player(

        user_id

    )


    return len(

        player["bonuses"]

    ) * 10




# =========================
# ТЕКСТ
# =========================


def collection_text(user_id):

    player = get_collection_player(

        user_id

    )


    text = (

        "🚗 <b>КОЛЛЕКЦИИ</b>\n\n"

    )



    for collection in COLLECTIONS:


        if collection["id"] in player["completed"]:

            status = "✅"

        else:

            status = "🔒"



        text += (

            f"{status} {collection['name']}\n"

            f"🎁 {collection['reward']}\n\n"

        )



    text += (

        f"🔥 Общий бонус: +{collection_bonus(user_id)}%"

    )



    return text