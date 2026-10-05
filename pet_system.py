import json
import os
import random



PET_FILE = "pets.json"




# =========================
# ПИТОМЦЫ
# =========================


PETS = [

    {
        "name": "🐕 Гоночный пёс",

        "rarity": "🔵 Rare",

        "bonus": 5
    },


    {
        "name": "🐺 Волк трассы",

        "rarity": "💎 Legendary",

        "bonus": 10
    },


    {
        "name": "🦅 Орёл скорости",

        "rarity": "💎 Legendary",

        "bonus": 15
    },


    {
        "name": "🐉 Дракон мотора",

        "rarity": "🔥 Mythic",

        "bonus": 30
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


def get_player_pet(user_id):

    data = load_pets()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "pet": None,

            "level": 1,

            "xp": 0

        }


        save_pets(data)



    return data[uid]




# =========================
# ВЫПАДЕНИЕ ПИТОМЦА
# =========================


def open_pet_box(user_id):

    data = load_pets()


    uid = str(user_id)



    pet = random.choice(

        PETS

    )



    data[uid] = {

        "pet":

        pet["name"],

        "rarity":

        pet["rarity"],

        "bonus":

        pet["bonus"],

        "level":

        1,

        "xp":

        0

    }



    save_pets(
        data
    )


    return pet




# =========================
# ОПЫТ ПИТОМЦА
# =========================


def add_pet_xp(
    user_id,
    amount
):

    data = load_pets()


    uid = str(user_id)



    if uid not in data:

        return



    data[uid]["xp"] += amount



    need = (

        data[uid]["level"]

        *

        100

    )



    if data[uid]["xp"] >= need:


        data[uid]["xp"] = 0

        data[uid]["level"] += 1



        data[uid]["bonus"] += 5



    save_pets(
        data
    )




# =========================
# БОНУС
# =========================


def pet_bonus(user_id):

    pet = get_player_pet(

        user_id

    )


    if not pet["pet"]:

        return 0



    return (

        pet["bonus"]

        *

        pet["level"]

    )




# =========================
# ТЕКСТ
# =========================


def pet_text(user_id):

    pet = get_player_pet(

        user_id

    )


    if not pet["pet"]:

        return (

            "🐾 У тебя нет питомца"

        )



    return (

        "🐾 <b>ПИТОМЕЦ</b>\n\n"

        f"{pet['pet']}\n"

        f"💎 Редкость: {pet['rarity']}\n"

        f"⭐ Уровень: {pet['level']}\n"

        f"✨ Опыт: {pet['xp']}\n"

        f"🔥 Бонус: +{pet['bonus']}"

    )