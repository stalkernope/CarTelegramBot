import json
import os



WORLD_FILE = "world.json"




# =========================
# КАРТА МИРА
# =========================


LOCATIONS = [

    {

        "id": "garage_city",

        "name": "🏙 Garage City",

        "level": 1,

        "need":

        0,

        "boss":

        "Нет",

        "reward":

        1000

    },


    {

        "id": "night_street",

        "name": "🌃 Night Street",

        "level": 5,

        "need":

        5,

        "boss":

        "Shadow Racer",

        "reward":

        5000

    },


    {

        "id": "speed_valley",

        "name": "🏔 Speed Valley",

        "level": 10,

        "need":

        10,

        "boss":

        "Turbo King",

        "reward":

        15000

    },


    {

        "id": "legend_island",

        "name": "🏝 Legend Island",

        "level": 20,

        "need":

        20,

        "boss":

        "The Legend",

        "reward":

        50000

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_world():

    if not os.path.exists(WORLD_FILE):

        return {}



    try:

        with open(

            WORLD_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_world(data):

    with open(

        WORLD_FILE,

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
# ПРОФИЛЬ МИРА
# =========================


def get_world_player(user_id):

    data = load_world()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "location":

            "garage_city",


            "opened":

            [

                "garage_city"

            ],


            "bosses":

            []

        }


        save_world(data)



    return data[uid]




# =========================
# ОТКРЫТИЕ РАЙОНА
# =========================


def unlock_location(

    user_id,

    location_id,

    player_level

):

    data = load_world()


    profile = get_world_player(

        user_id

    )


    location = None



    for place in LOCATIONS:


        if place["id"] == location_id:

            location = place



    if not location:

        return False




    if player_level < location["need"]:

        return False




    if location_id in profile["opened"]:

        return False



    profile["opened"].append(

        location_id

    )



    data[str(user_id)] = profile


    save_world(data)



    return location




# =========================
# ПЕРЕЕЗД
# =========================


def travel(

    user_id,

    location_id

):

    data = load_world()


    profile = get_world_player(

        user_id

    )



    if location_id not in profile["opened"]:

        return False



    profile["location"] = location_id



    data[str(user_id)] = profile


    save_world(data)



    return True




# =========================
# БОССЫ
# =========================


def defeat_boss(

    user_id,

    boss

):

    data = load_world()


    profile = get_world_player(

        user_id

    )


    if boss not in profile["bosses"]:


        profile["bosses"].append(

            boss

        )


    data[str(user_id)] = profile


    save_world(data)



# =========================
# ТЕКСТ
# =========================


def world_text(user_id):

    player = get_world_player(

        user_id

    )


    text = (

        "🌍 <b>КАРТА МИРА</b>\n\n"

    )


    text += (

        f"📍 Сейчас: {player['location']}\n\n"

    )



    for location in LOCATIONS:


        if location["id"] in player["opened"]:

            status = "✅"

        else:

            status = "🔒"



        text += (

            f"{status} {location['name']}\n"

            f"⭐ Уровень: {location['level']}\n"

            f"👑 Босс: {location['boss']}\n\n"

        )



    return text