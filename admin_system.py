import json
import os
import time



ADMIN_FILE = "admin.json"




# =========================
# НАСТРОЙКИ
# =========================


ADMINS = [

    123456789

]




# =========================
# ЗАГРУЗКА
# =========================


def load_admin():

    if not os.path.exists(ADMIN_FILE):

        return {

            "banned": [],

            "logs": []

        }



    try:

        with open(

            ADMIN_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {

            "banned": [],

            "logs": []

        }




# =========================
# СОХРАНЕНИЕ
# =========================


def save_admin(data):

    with open(

        ADMIN_FILE,

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
# ПРОВЕРКА АДМИНА
# =========================


def is_admin(user_id):

    return user_id in ADMINS




# =========================
# БАН
# =========================


def ban_player(

    admin_id,

    user_id

):

    if not is_admin(admin_id):

        return False



    data = load_admin()



    if user_id not in data["banned"]:


        data["banned"].append(

            user_id

        )



    data["logs"].append(

        {

            "admin":

            admin_id,

            "action":

            "ban",

            "player":

            user_id,

            "time":

            time.time()

        }

    )



    save_admin(data)



    return True




# =========================
# РАЗБАН
# =========================


def unban_player(

    admin_id,

    user_id

):

    if not is_admin(admin_id):

        return False



    data = load_admin()



    if user_id in data["banned"]:


        data["banned"].remove(

            user_id

        )



    save_admin(data)



    return True




# =========================
# ПРОВЕРКА БАНА
# =========================


def is_banned(user_id):

    data = load_admin()



    return user_id in data["banned"]




# =========================
# ЛОГ
# =========================


def add_admin_log(

    admin_id,

    action

):

    data = load_admin()



    data["logs"].append(

        {

            "admin":

            admin_id,

            "action":

            action,

            "time":

            time.time()

        }

    )



    save_admin(data)




# =========================
# СТАТИСТИКА
# =========================


def server_stats():

    return (

        "📊 <b>СТАТИСТИКА СЕРВЕРА</b>\n\n"

        "👥 Игроков: подсчёт БД\n"

        "🚗 Машин: подсчёт гаражей\n"

        "🏆 Побед: подсчёт гонок\n"

        "⚔️ Кланов: подсчёт кланов"

    )