import json
import os


from database import (
    get_player,
    update_player
)



PET_FILE = "pets.json"




# =========================
# БАЗА ПИТОМЦЕВ
# =========================


PETS = {


    "drift_dog": {


        "name": "🐺 Дрифт-пёс",

        "rarity": "⚪ Common",

        "bonus": {

            "handling": 5

        }

    },


    "speed_hawk": {


        "name": "🦅 Сокол скорости",

        "rarity": "🔵 Rare",

        "bonus": {

            "speed": 20

        }

    },


    "turbo_bot": {


        "name": "🤖 Турбо-бот",

        "rarity": "💎 Legendary",

        "bonus": {

            "power": 50

        }

    },


    "fire_dragon": {


        "name": "🐉 Огненный дракон",

        "rarity": "🔥 Mythic",

        "bonus": {

            "power": 100,

            "speed": 50,

            "critical": 10

        }

    }

}




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
# ПОЛУЧИТЬ ПИТОМЦЕВ ИГРОКА
# =========================


def get_player_pets(user_id):


    player = get_player(

        user_id

    )


    return player.get(

        "pets",

        []

    )




# =========================
# ДОБАВИТЬ ПИТОМЦА
# =========================


def add_pet(

    user_id,

    pet_id

):


    player = get_player(

        user_id

    )


    if pet_id not in PETS:


        return False



    player["pets"].append(

        {

            "id": pet_id,

            "level": 1

        }

    )



    if player["active_pet"] is None:


        player["active_pet"] = pet_id



    update_player(

        user_id,

        player

    )


    return True




# =========================
# АКТИВНЫЙ ПИТОМЕЦ
# =========================


def set_active_pet(

    user_id,

    pet_id

):


    player = get_player(

        user_id

    )


    for pet in player["pets"]:


        if pet["id"] == pet_id:


            player["active_pet"] = pet_id


            update_player(

                user_id,

                player

            )


            return True



    return False




# =========================
# БОНУСЫ
# =========================


def get_pet_bonus(user_id):


    player = get_player(

        user_id

    )


    active = player.get(

        "active_pet"

    )


    bonus = {


        "power": 0,

        "speed": 0,

        "handling": 0,

        "critical": 0

    }



    if not active:


        return bonus



    for pet in player["pets"]:


        if pet["id"] == active:


            data = PETS[active]


            level = pet["level"]



            for stat,value in data["bonus"].items():


                bonus[stat] = value * level



    return bonus




# =========================
# ПРОКАЧКА
# =========================


def upgrade_pet(

    user_id,

    pet_id

):


    player = get_player(

        user_id

    )


    for pet in player["pets"]:


        if pet["id"] == pet_id:


            if pet["level"] >= 10:


                return False



            price = pet["level"] * 2000



            if player["coins"] < price:


                return False



            player["coins"] -= price



            pet["level"] += 1



            update_player(

                user_id,

                player

            )


            return True



    return False




# =========================
# ТЕКСТ
# =========================


def pets_text(user_id):


    player = get_player(

        user_id

    )


    text = (

        "🐾 <b>ПИТОМЦЫ</b>\n\n"

    )



    if not player["pets"]:


        return text + "У тебя нет питомцев"



    for pet in player["pets"]:


        data = PETS[pet["id"]]


        active = ""


        if player["active_pet"] == pet["id"]:


            active = " 👑"



        text += (

            f"{data['name']}{active}\n"

            f"{data['rarity']}\n"

            f"⭐ Уровень: "

            f"{pet['level']}/10\n\n"

        )



    return text