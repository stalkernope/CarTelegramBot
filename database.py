import json
import os



DATABASE_FILE = "players.json"




# =========================
# СОЗДАНИЕ ИГРОКА
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


        "pets": [],

        "active_pet": None,


        "tuning_parts": [],


        "wins": 0,

        "losses": 0,


        "clan": None,


        "achievements": [],

        "titles": [],


        "premium": False

    }




# =========================
# ЗАГРУЗКА БАЗЫ
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



    except:


        return {}




# =========================
# СОХРАНЕНИЕ БАЗЫ
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
# ПОЛУЧИТЬ ИГРОКА
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
# ОБНОВИТЬ ИГРОКА
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
# МОНЕТЫ
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
# ОПЫТ
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
# ПОБЕДЫ
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
# ДОБАВИТЬ МАШИНУ
# =========================


def add_car(

    user_id,

    car

):


    player = get_player(

        user_id

    )


    if car not in player["garage"]:


        player["garage"].append(

            car

        )



    if player["main_car"] is None:


        player["main_car"] = car



    update_player(

        user_id,

        player

    )




# =========================
# ДОБАВИТЬ ПИТОМЦА
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