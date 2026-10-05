import json
import os
import random
import time



TEAM_FILE = "teams.json"




# =========================
# НАСТРОЙКИ
# =========================


TEAM_BONUS = 10




# =========================
# ЗАГРУЗКА
# =========================


def load_teams():

    if not os.path.exists(TEAM_FILE):

        return {}


    try:

        with open(

            TEAM_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_teams(data):

    with open(

        TEAM_FILE,

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
# СОЗДАТЬ КОМАНДУ
# =========================


def create_team(

    user_id,

    name

):

    data = load_teams()


    uid = str(user_id)



    if uid in data:

        return False



    data[uid] = {

        "name":

        name,


        "members":

        [

            user_id

        ],


        "wins":

        0,


        "points":

        0,


        "created":

        time.time()

    }



    save_teams(data)



    return True




# =========================
# ПОЛУЧИТЬ КОМАНДУ
# =========================


def get_team(user_id):

    data = load_teams()


    uid = str(user_id)



    return data.get(

        uid

    )




# =========================
# ДОБАВИТЬ ИГРОКА
# =========================


def add_member(

    owner_id,

    member_id

):

    data = load_teams()


    team = get_team(

        owner_id

    )



    if not team:

        return False



    if member_id not in team["members"]:

        team["members"].append(

            member_id

        )



    data[str(owner_id)] = team


    save_teams(data)



    return True




# =========================
# КОМАНДНАЯ ГОНКА
# =========================


def team_race(

    user_id

):

    data = load_teams()


    team = get_team(

        user_id

    )



    if not team:

        return False



    power = (

        len(team["members"])

        *

        TEAM_BONUS

    )



    chance = random.randint(

        1,

        100

    )



    if chance + power >= 60:


        team["wins"] += 1

        team["points"] += 100



        result = {

            "win":

            True,

            "reward":

            1000

        }


    else:


        team["points"] += 20



        result = {

            "win":

            False,

            "reward":

            100

        }




    data[str(user_id)] = team


    save_teams(data)



    return result




# =========================
# РЕЙТИНГ КОМАНД
# =========================


def team_rating():


    data = load_teams()



    teams = list(

        data.values()

    )



    teams.sort(

        key=lambda x:

        x["points"],

        reverse=True

    )



    return teams




# =========================
# ТЕКСТ
# =========================


def team_text(user_id):

    team = get_team(

        user_id

    )



    if not team:

        return (

            "❌ Ты не состоишь в команде"

        )



    return (

        "🏁 <b>КОМАНДА</b>\n\n"

        f"🔥 Название: {team['name']}\n"

        f"👥 Участники: {len(team['members'])}\n"

        f"🏆 Победы: {team['wins']}\n"

        f"⭐ Очки: {team['points']}"

    )