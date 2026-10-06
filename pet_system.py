from database import (
    get_player,
    update_player,
    remove_coins
)





# =========================
# PETS
# =========================


PETS = {


    "dog": {


        "name": "🐕 Street Dog",


        "price": 5000,


        "power": 100,


        "speed": 20


    },



    "cat": {


        "name": "🐈 Turbo Cat",


        "price": 15000,


        "power": 250,


        "speed": 50


    },



    "hawk": {


        "name": "🦅 Racing Hawk",


        "price": 40000,


        "power": 600,


        "speed": 100


    },



    "dragon": {


        "name": "🐉 Neon Dragon",


        "price": 100000,


        "power": 1500,


        "speed": 200


    }

}







# =========================
# ALL PETS
# =========================


def get_pets():


    return PETS








# =========================
# BUY PET
# =========================


def buy_pet(

    user_id,

    pet_id

):


    if pet_id not in PETS:


        raise Exception(

            "Питомец не найден"

        )



    pet = PETS[pet_id]



    player = get_player(

        user_id

    )





    if pet_id in player["pets"]:


        raise Exception(

            "Питомец уже есть"

        )





    if player["coins"] < pet["price"]:


        raise Exception(

            "Недостаточно монет"

        )





    remove_coins(

        user_id,

        pet["price"]

    )





    player["pets"].append(

        pet_id

    )



    update_player(

        user_id,

        player

    )



    return pet








# =========================
# SET ACTIVE PET
# =========================


def set_active_pet(

    user_id,

    pet_id

):


    player = get_player(

        user_id

    )



    if pet_id not in player["pets"]:


        raise Exception(

            "Питомца нет"

        )





    player["active_pet"] = pet_id



    update_player(

        user_id,

        player

    )



    return True








# =========================
# BONUS
# =========================


def get_pet_bonus(

    user_id

):


    player = get_player(

        user_id

    )



    pet_id = player.get(

        "active_pet"

    )



    if not pet_id:


        return {


            "power":0,


            "speed":0


        }





    pet = PETS.get(

        pet_id

    )



    if not pet:


        return {


            "power":0,


            "speed":0


        }






    return {


        "power":pet["power"],


        "speed":pet["speed"]


    }