import json
import os




PET_FILE = "pets.json"




# =========================
# БАЗА ПИТОМЦЕВ
# =========================


PETS = [

    {

        "id": "drift_dog",

        "name": "🐺 Дрифт-пёс",

        "rarity": "⚪ Common",

        "bonus": {

            "control": 10,

            "critical": 5

        }

    },


    {

        "id": "speed_hawk",

        "name": "🦅 Сокол скорости",

        "rarity": "🔵 Rare",

        "bonus": {

            "speed": 20

        }

    },


    {

        "id": "turbo_bot",

        "name": "🤖 Турбо-бот",

        "rarity": "💎 Legendary",

        "bonus": {

            "power": 50

        }

    },


    {

        "id": "fire_dragon",

        "name": "🐉 Огненный дракон",

        "rarity": "🔥 Mythic",

        "bonus": {

            "power": 100,

            "speed": 50,

            "critical": 10

        }

    }

]




# =========================
# ЗАГРУЗКА
# =========================


def load_pets():


    if not os.path.exists(PET_FILE):

        return {}



    try:

        with open(

            PET_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except:


        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_pets(data):


    with open(

        PET_FILE,

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
# ПОЛУЧИТЬ ПИТОМЦА
# =========================


def add_pet(

    user_id,

    pet_id

):


    data = load_pets()


    uid = str(user_id)



    if uid not in data:


        data[uid] = []



    if pet_id not in data[uid]:


        data[uid].append(

            {

                "id": pet_id,

                "level": 1

            }

        )


    save_pets(data)



    return True




# =========================
# СПИСОК ИГРОКА
# =========================


def get_player_pets(user_id):


    data = load_pets()



    return data.get(

        str(user_id),

        []

    )




# =========================
# НАЙТИ ПИТОМЦА
# =========================


def get_pet(

    pet_id

):


    for pet in PETS:


        if pet["id"] == pet_id:


            return pet



    return None




# =========================
# БОНУСЫ
# =========================


def get_pet_bonus(user_id):


    pets = get_player_pets(

        user_id

    )


    bonus = {

        "power": 0,

        "speed": 0,

        "critical": 0,

        "control": 0

    }



    for player_pet in pets:


        pet = get_pet(

            player_pet["id"]

        )



        if not pet:

            continue



        level = player_pet.get(

            "level",

            1

        )



        for key,value in pet["bonus"].items():


            bonus[key] += value * level



    return bonus




# =========================
# ТЕКСТ
# =========================


def pets_text(user_id):


    pets = get_player_pets(

        user_id

    )


    text = (

        "🐾 <b>ПИТОМЦЫ</b>\n\n"

    )



    if not pets:


        return (

            text +

            "У тебя пока нет питомцев"

        )



    for player_pet in pets:


        pet = get_pet(

            player_pet["id"]

        )


        if pet:


            text += (

                f"{pet['name']}\n"

                f"💎 {pet['rarity']}\n"

                f"⭐ Уровень: "

                f"{player_pet['level']}\n\n"

            )



    return text