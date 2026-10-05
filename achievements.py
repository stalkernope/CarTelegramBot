from database import (
    get_player,
    update_player,
    add_coins,
    add_xp
)



# =========================
# СПИСОК ДОСТИЖЕНИЙ
# =========================


ACHIEVEMENTS = [

    {
        "id": "first_car",

        "name": "🚗 Первая машина",

        "description":
        "Получи свою первую машину",

        "reward_coins": 500,

        "reward_xp": 100
    },


    {
        "id": "ten_cars",

        "name": "🏎 Коллекционер",

        "description":
        "Собери 10 машин",

        "reward_coins": 5000,

        "reward_xp": 500
    },


    {
        "id": "first_win",

        "name": "🏆 Первая победа",

        "description":
        "Выиграй первую битву",

        "reward_coins": 1000,

        "reward_xp": 200
    },


    {
        "id": "ten_wins",

        "name": "🔥 Боец",

        "description":
        "Получить 10 побед",

        "reward_coins": 5000,

        "reward_xp": 1000
    },


    {
        "id": "hundred_wins",

        "name": "👑 Легенда",

        "description":
        "Получить 100 побед",

        "reward_coins": 50000,

        "reward_xp": 5000
    },


    {
        "id": "mythic",

        "name": "🔥 Владелец Mythic",

        "description":
        "Получить Mythic машину",

        "reward_coins": 10000,

        "reward_xp": 2000
    }

]




# =========================
# ПРОВЕРКА УСЛОВИЙ
# =========================


def check_condition(
    achievement_id,
    player
):


    garage = player["garage"]



    if achievement_id == "first_car":

        return len(garage) >= 1



    if achievement_id == "ten_cars":

        return len(garage) >= 10



    if achievement_id == "first_win":

        return player["wins"] >= 1



    if achievement_id == "ten_wins":

        return player["wins"] >= 10



    if achievement_id == "hundred_wins":

        return player["wins"] >= 100



    if achievement_id == "mythic":

        for car in garage:

            if "Mythic" in car:

                return True



    return False




# =========================
# ПРОВЕРКА ВСЕХ
# =========================


def check_achievements(user_id):

    player = get_player(
        user_id
    )


    unlocked = []



    for achievement in ACHIEVEMENTS:


        aid = achievement["id"]



        if aid in player["achievements"]:

            continue



        if check_condition(

            aid,

            player

        ):



            player["achievements"].append(

                aid

            )


            add_coins(

                user_id,

                achievement["reward_coins"]

            )


            add_xp(

                user_id,

                achievement["reward_xp"]

            )


            unlocked.append(

                achievement

            )



    update_player(

        user_id,

        player

    )



    return unlocked




# =========================
# ТЕКСТ
# =========================


def achievements_text(user_id):

    player = get_player(
        user_id
    )


    text = (

        "🎖 <b>ДОСТИЖЕНИЯ</b>\n\n"

    )



    for achievement in ACHIEVEMENTS:


        if achievement["id"] in player["achievements"]:

            text += (

                "✅ "

                +

                achievement["name"]

                +

                "\n"

            )


        else:

            text += (

                "🔒 "

                +

                achievement["name"]

                +

                "\n"

            )



    return text