import json
import os



DATABASE_FILE = "players.json"






# =========================
# CREATE PLAYER
# =========================


def create_player(user_id):


    return {


        "id": user_id,


        "coins": 5000,


        "gems": 0,


        "level": 1,


        "xp": 0,



        "garage": [],


        "main_car": None,



        "wins": 0,


        "losses": 0,



        "pets": [],


        "active_pet": None,



        "tuning_parts": [],



        "achievements": [],


        "titles": [],



        "clan": None,



        "premium": False


    }








# =========================
# LOAD DATABASE
# =========================


def load_database():


    if not os.path.exists(

        DATABASE_FILE

    ):


        return {}




    try:


        with open(

            DATABASE_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except Exception:


        return {}









# =========================
# SAVE DATABASE
# =========================


def save_database(data):


    with open(

        DATABASE_FILE,

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
# GET PLAYER
# =========================


def get_player(user_id):


    data = load_database()



    uid = str(user_id)



    if uid not in data:


        data[uid] = create_player(

            user_id

        )


        save_database(

            data

        )



    return data[uid]









# =========================
# UPDATE PLAYER
# =========================


def update_player(

    user_id,

    player

):


    data = load_database()



    data[str(user_id)] = player



    save_database(

        data

    )









# =========================
# COINS
# =========================


def add_coins(

    user_id,

    amount

):


    player = get_player(

        user_id

    )


    player["coins"] += amount



    update_player(

        user_id,

        player

    )







def remove_coins(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    if player["coins"] < amount:


        return False



    player["coins"] -= amount



    update_player(

        user_id,

        player

    )



    return True







# =========================
# XP
# =========================


def add_xp(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    player["xp"] += amount



    need = player["level"] * 1000



    if player["xp"] >= need:


        player["xp"] -= need


        player["level"] += 1



    update_player(

        user_id,

        player

    )








# =========================
# WINS
# =========================


def add_win(user_id):


    player = get_player(

        user_id

    )



    player["wins"] += 1



    update_player(

        user_id,

        player

    )








def add_loss(user_id):


    player = get_player(

        user_id

    )



    player["losses"] += 1



    update_player(

        user_id,

        player

    )








# =========================
# GARAGE
# =========================


def add_car(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    if car_name not in player["garage"]:


        player["garage"].append(

            car_name

        )



    if player["main_car"] is None:


        player["main_car"] = car_name



    update_player(

        user_id,

        player

    )








def remove_car(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    if car_name in player["garage"]:


        player["garage"].remove(

            car_name

        )



    if player["main_car"] == car_name:


        player["main_car"] = None



    update_player(

        user_id,

        player

    )








# =========================
# PETS
# =========================


def add_pet(

    user_id,

    pet

):


    player = get_player(

        user_id

    )



    if pet not in player["pets"]:


        player["pets"].append(

            pet

        )



    update_player(

        user_id,

        player

    )