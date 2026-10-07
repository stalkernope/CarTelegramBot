import json
import os


DATABASE_FILE = "players.json"


START_CAR = "BMW M3 GTR"





# =========================
# CREATE PLAYER
# =========================


def create_player(user_id):

    return {

        "id": user_id,

        "username": "PLAYER",

        "coins": 5000,

        "gems": 0,

        "rep": 0,


        "level": 1,

        "xp": 0,


        "garage": [

            START_CAR

        ],


        "main_car": START_CAR,


        "wins": 0,

        "losses": 0,


        "pets": [],

        "active_pet": None,


        "tuning_parts": {},


        "achievements": [],

        "titles": [],


        "clan": None,


        "premium": False

    }







# =========================
# LOAD DATABASE
# =========================


def load_database():


    if not os.path.exists(DATABASE_FILE):

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






# совместимость

def load_players():

    return load_database()







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
# UPDATE OLD PLAYER
# =========================


def migrate_player(player):


    defaults = {


        "username": "PLAYER",

        "coins": 5000,

        "gems": 0,

        "rep": 0,


        "level": 1,

        "xp": 0,


        "garage": [],

        "main_car": None,


        "wins": 0,

        "losses": 0,


        "pets": [],

        "active_pet": None,


        "tuning_parts": {},


        "achievements": [],

        "titles": [],


        "clan": None,


        "premium": False

    }



    for key, value in defaults.items():

        if key not in player:

            player[key] = value



    if not player["garage"]:

        player["garage"] = [

            START_CAR

        ]



    if player["main_car"] is None:

        player["main_car"] = START_CAR



    return player







# =========================
# GET PLAYER
# =========================


def get_player(user_id):


    database = load_database()


    uid = str(user_id)



    if uid not in database:


        database[uid] = create_player(

            user_id

        )


        save_database(database)



    else:


        database[uid] = migrate_player(

            database[uid]

        )


        save_database(database)



    return database[uid]







# =========================
# UPDATE PLAYER
# =========================


def update_player(

    user_id,

    player

):


    database = load_database()


    database[str(user_id)] = player


    save_database(database)







# =========================
# COINS
# =========================


def add_coins(

    user_id,

    amount

):


    player = get_player(user_id)


    player["coins"] += amount


    update_player(

        user_id,

        player

    )






def remove_coins(

    user_id,

    amount

):


    player = get_player(user_id)



    if player["coins"] < amount:

        return False



    player["coins"] -= amount


    update_player(

        user_id,

        player

    )


    return True







# =========================
# GEMS
# =========================


def add_gems(

    user_id,

    amount

):


    player = get_player(user_id)


    player["gems"] += amount


    update_player(

        user_id,

        player

    )






def remove_gems(

    user_id,

    amount

):


    player = get_player(user_id)


    if player["gems"] < amount:

        return False


    player["gems"] -= amount


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


    player = get_player(user_id)


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
# REP
# =========================


def add_rep(

    user_id,

    amount

):


    player = get_player(user_id)


    player["rep"] += amount


    update_player(

        user_id,

        player

    )






def remove_rep(

    user_id,

    amount

):


    player = get_player(user_id)


    player["rep"] = max(

        0,

        player["rep"] - amount

    )


    update_player(

        user_id,

        player

    )







# =========================
# WINS / LOSSES
# =========================


def add_win(user_id):


    player = get_player(user_id)


    player["wins"] += 1


    update_player(

        user_id,

        player

    )







def add_loss(user_id):


    player = get_player(user_id)


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


    player = get_player(user_id)



    if car_name not in player["garage"]:


        player["garage"].append(

            car_name

        )



    if not player["main_car"]:


        player["main_car"] = car_name



    update_player(

        user_id,

        player

    )







def remove_car(

    user_id,

    car_name

):


    player = get_player(user_id)



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


    player = get_player(user_id)


    if pet not in player["pets"]:


        player["pets"].append(

            pet

        )


    update_player(

        user_id,

        player

    )







def remove_pet(

    user_id,

    pet

):


    player = get_player(user_id)


    if pet in player["pets"]:


        player["pets"].remove(

            pet

        )


    update_player(

        user_id,

        player

    )







# =========================
# TUNING
# =========================


def add_tuning(

    user_id,

    part

):


    player = get_player(user_id)


    if part not in player["tuning_parts"]:


        player["tuning_parts"][part] = 1


    else:


        player["tuning_parts"][part] += 1



    update_player(

        user_id,

        player

    )






def remove_tuning(

    user_id,

    part

):


    player = get_player(user_id)


    if part in player["tuning_parts"]:


        del player["tuning_parts"][part]


    update_player(

        user_id,

        player

    )







# =========================
# ACHIEVEMENTS
# =========================


def add_achievement(

    user_id,

    achievement

):


    player = get_player(user_id)


    if achievement not in player["achievements"]:


        player["achievements"].append(

            achievement

        )


    update_player(

        user_id,

        player

    )







def add_title(

    user_id,

    title

):


    player = get_player(user_id)


    if title not in player["titles"]:


        player["titles"].append(

            title

        )


    update_player(

        user_id,

        player

    )







# =========================
# CLAN
# =========================


def set_clan(

    user_id,

    clan

):


    player = get_player(user_id)


    player["clan"] = clan


    update_player(

        user_id,

        player

    )