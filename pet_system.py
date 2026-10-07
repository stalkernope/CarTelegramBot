# =========================
# PET SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player
)







# =========================
# PET DATABASE
# =========================


PETS = {


    "dog": {


        "name":
        "🐕 Гончая",


        "bonus":
        "Больше опыта",


        "xp_bonus":
        10

    },



    "cat": {


        "name":
        "🐈 Кибер-кот",


        "bonus":
        "Больше монет",


        "coin_bonus":
        10

    },



    "dragon": {


        "name":
        "🐉 Дракон",


        "bonus":
        "Бонус к гонкам",


        "race_bonus":
        15

    }

}








# =========================
# GET PETS TEXT
# =========================


def pets_text(user_id):


    player = get_player(

        user_id

    )


    owned = player.get(

        "pets",

        []

    )


    active = player.get(

        "active_pet",

        None

    )



    text = (

        "🐾 <b>ПИТОМЦЫ</b>\n\n"

    )



    if not owned:


        return (

            text +

            "У тебя нет питомцев"

        )






    for pet in owned:


        data = PETS.get(

            pet

        )


        if data:


            mark = (

                "⭐ "

                if active == pet

                else ""

            )


            text += (

                f"{mark}"

                f"{data['name']}\n"

                f"Бонус: {data['bonus']}\n\n"

            )



    return text







# =========================
# ADD PET
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





    if "pets" not in player:


        player["pets"] = []





    if pet_id not in player["pets"]:


        player["pets"].append(

            pet_id

        )



    update_player(

        user_id,

        player

    )



    return True







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



    if pet_id not in player.get(

        "pets",

        []

    ):


        return False





    player["active_pet"] = pet_id



    update_player(

        user_id,

        player

    )



    return True







# =========================
# GET BONUS
# =========================


def get_pet_bonus(

    user_id,

    bonus_type

):


    player = get_player(

        user_id

    )



    active = player.get(

        "active_pet"

    )



    if not active:


        return 0





    pet = PETS.get(

        active

    )



    if not pet:


        return 0





    return pet.get(

        bonus_type,

        0

    )