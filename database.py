# =========================
# DATABASE FINAL COMPLETE
# CAR LEGENDS
# =========================


import json
import os
from datetime import datetime





DATABASE_FILE = "players.json"






# =========================
# CREATE PLAYER
# =========================


def create_player(user_id):

    return {


        # BASIC

        "id": user_id,

        "username": "",

        "created":

        str(datetime.now()),



        # ECONOMY

        "coins": 5000,

        "gems": 50,

        "tokens": 0,



        # LEVEL

        "level": 1,

        "xp": 0,

        "reputation": 0,



        # GARAGE

        "garage": [],

        "main_car": None,



        # CARS DATA

        "car_upgrades": {},

        "owned_skins": [],



        # RACE STATS

        "wins": 0,

        "losses": 0,

        "draws": 0,



        "race_history": [],



        # BATTLE

        "battle_history": [],

        "rating": 1000,



        # CLAN

        "clan": None,

        "clan_role": None,



        # PETS

        "pets": [],

        "active_pet": None,



        # TUNING

        "tuning_parts": [],



        # ACHIEVEMENTS

        "achievements": [],



        # TITLES

        "titles": [],

        "active_title": None,



        # CAREER

        "career_stage": 1,

        "career_progress": 0,



        # BLACKLIST

        "boss_progress": 0,

        "defeated_bosses": [],



        # DAILY

        "daily_claim":

        None,



        "daily_car":

        None,



        # CASES

        "opened_cases": 0,



        # PREMIUM

        "premium": False,


        "premium_until": None,



        # SOCIAL

        "friends": [],

        "messages": [],



        # SEASON

        "season_xp": 0,

        "battle_pass_level": 1


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



    return True







# =========================
# ECONOMY
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



    return player["coins"]







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







def add_gems(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    player["gems"] += amount



    update_player(

        user_id,

        player

    )







def remove_gems(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    if player["gems"] < amount:


        return False





    player["gems"] -= amount



    update_player(

        user_id,

        player

    )



    return True







# =========================
# EXPERIENCE
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





    while player["xp"] >= need:


        player["xp"] -= need


        player["level"] += 1


        need = player["level"] * 1000





    update_player(

        user_id,

        player

    )



    return player["level"]







# =========================
# RACE STATS
# =========================


def add_win(

    user_id

):


    player = get_player(

        user_id

    )



    player["wins"] += 1



    player["rating"] += 25



    update_player(

        user_id,

        player

    )






def add_loss(

    user_id

):


    player = get_player(

        user_id

    )



    player["losses"] += 1



    player["rating"] -= 10



    if player["rating"] < 0:


        player["rating"] = 0





    update_player(

        user_id,

        player

    )







def add_draw(

    user_id

):


    player = get_player(

        user_id

    )



    player["draws"] += 1



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



    return True








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



    return True







def set_main_car(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    if car_name not in player["garage"]:


        return False





    player["main_car"] = car_name



    update_player(

        user_id,

        player

    )



    return True
    
    
    # =========================
# TUNING SYSTEM
# =========================


def add_tuning_part(

    user_id,

    part

):


    player = get_player(

        user_id

    )



    if part not in player["tuning_parts"]:


        player["tuning_parts"].append(

            part

        )



    update_player(

        user_id,

        player

    )



    return True







def upgrade_car_data(

    user_id,

    car_name,

    upgrade

):


    player = get_player(

        user_id

    )



    if car_name not in player["garage"]:


        return False





    if car_name not in player["car_upgrades"]:


        player["car_upgrades"][car_name] = {}





    current = player["car_upgrades"][car_name].get(

        upgrade,

        0

    )



    player["car_upgrades"][car_name][upgrade] = current + 1





    update_player(

        user_id,

        player

    )



    return True







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



    return True







def set_active_pet(

    user_id,

    pet

):


    player = get_player(

        user_id

    )



    if pet not in player["pets"]:


        return False





    player["active_pet"] = pet



    update_player(

        user_id,

        player

    )



    return True







# =========================
# ACHIEVEMENTS
# =========================


def add_achievement(

    user_id,

    achievement

):


    player = get_player(

        user_id

    )



    if achievement not in player["achievements"]:


        player["achievements"].append(

            achievement

        )



    update_player(

        user_id,

        player

    )



    return True







# =========================
# TITLES
# =========================


def add_title(

    user_id,

    title

):


    player = get_player(

        user_id

    )



    if title not in player["titles"]:


        player["titles"].append(

            title

        )



    update_player(

        user_id,

        player

    )



    return True







def set_title(

    user_id,

    title

):


    player = get_player(

        user_id

    )



    if title not in player["titles"]:


        return False





    player["active_title"] = title



    update_player(

        user_id,

        player

    )



    return True







# =========================
# CLAN
# =========================


def set_clan(

    user_id,

    clan

):


    player = get_player(

        user_id

    )



    player["clan"] = clan



    update_player(

        user_id,

        player

    )



    return True







def remove_clan(

    user_id

):


    player = get_player(

        user_id

    )



    player["clan"] = None



    player["clan_role"] = None



    update_player(

        user_id,

        player

    )



    return True







# =========================
# HISTORY
# =========================


def add_race_history(

    user_id,

    result

):


    player = get_player(

        user_id

    )



    player["race_history"].append(

        result

    )



    player["race_history"] = player["race_history"][-50:]



    update_player(

        user_id,

        player

    )



    return True







def add_battle_history(

    user_id,

    result

):


    player = get_player(

        user_id

    )



    player["battle_history"].append(

        result

    )



    player["battle_history"] = player["battle_history"][-50:]



    update_player(

        user_id,

        player

    )



    return True







# =========================
# DAILY SYSTEM
# =========================


def set_daily_claim(

    user_id,

    date

):


    player = get_player(

        user_id

    )



    player["daily_claim"] = date



    update_player(

        user_id,

        player

    )








def set_daily_car(

    user_id,

    car

):


    player = get_player(

        user_id

    )



    player["daily_car"] = car



    update_player(

        user_id,

        player

    )








# =========================
# SEASON
# =========================


def add_season_xp(

    user_id,

    amount

):


    player = get_player(

        user_id

    )



    player["season_xp"] += amount



    if player["season_xp"] >= 1000:


        player["season_xp"] -= 1000


        player["battle_pass_level"] += 1





    update_player(

        user_id,

        player

    )



    return player["battle_pass_level"]







# =========================
# BACKUP
# =========================


def backup_database():


    data = load_database()



    backup_file = (

        "players_backup.json"

    )



    with open(

        backup_file,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )



    return True