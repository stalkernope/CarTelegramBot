import random


from database import (
    add_coins,
    add_xp,
    add_win,
    add_loss,
    get_player
)


from missions_system import (
    check_all_missions
)


from achievement_system import (
    check_achievements
)



# =========================
# ТРАССЫ
# =========================


TRACKS = [

    {
        "name": "🌆 Город",
        "bonus": "speed"
    },

    {
        "name": "🏔 Горы",
        "bonus": "power"
    },

    {
        "name": "🏁 Трек",
        "bonus": "balance"
    },

    {
        "name": "🏜 Пустыня",
        "bonus": "random"
    }

]




# =========================
# ПОГОДА
# =========================


WEATHER = [

    "☀️ Солнце",

    "🌧 Дождь",

    "❄️ Снег",

    "🌪 Шторм"

]




# =========================
# УСЛОВИЯ
# =========================


def get_race_conditions():

    return {

        "track":
        random.choice(TRACKS),

        "weather":
        random.choice(WEATHER)

    }




# =========================
# СИЛА МАШИНЫ
# =========================


def car_strength(car):

    if not car:

        return 0


    power = car.get(
        "power",
        0
    )


    speed = car.get(
        "speed",
        0
    )


    rarity = car.get(
        "rarity",
        ""
    )


    bonus = 0


    if "Mythic" in rarity:

        bonus = 500


    elif "Legendary" in rarity:

        bonus = 300


    elif "Rare" in rarity:

        bonus = 100



    return (

        power * 0.5

        +

        speed * 2

        +

        bonus

        +

        random.randint(
            -100,
            100
        )

    )




# =========================
# БИТВА
# =========================


def battle(car1, car2):

    conditions = get_race_conditions()


    score1 = car_strength(car1)

    score2 = car_strength(car2)



    critical = random.randint(
        1,
        100
    )



    if critical <= 10:


        if score1 >= score2:

            score1 += 300

        else:

            score2 += 300




    if score1 >= score2:


        return {

            "winner": car1,

            "loser": car2,

            "conditions": conditions,

            "critical": critical <= 10

        }



    return {

        "winner": car2,

        "loser": car1,

        "conditions": conditions,

        "critical": critical <= 10

    }




# =========================
# ПОБЕДА
# =========================


def reward_win(user_id):


    player = get_player(
        user_id
    )


    coins = 500



    streak = player.get(
        "win_streak",
        0
    )


    if streak >= 5:

        coins += 500



    add_coins(

        user_id,

        coins

    )


    add_xp(

        user_id,

        200

    )


    add_win(

        user_id

    )



    updated_player = get_player(

        user_id

    )



    missions = check_all_missions(

        user_id,

        updated_player

    )


    achievements = check_achievements(

        user_id,

        updated_player

    )



    return {

        "coins":

        coins,


        "missions":

        missions,


        "achievements":

        achievements

    }




# =========================
# ПОРАЖЕНИЕ
# =========================


def reward_loss(user_id):


    add_loss(

        user_id

    )


    return {

        "coins": 0,

        "missions": [],

        "achievements": []

    }




# =========================
# ТЕКСТ
# =========================


def battle_result_text(result):


    winner = result["winner"]

    loser = result["loser"]



    text = (

        "⚔️ <b>LEGEND RACE</b>\n\n"

        f"🏁 Трасса: "

        f"{result['conditions']['track']['name']}\n"

        f"🌦 Погода: "

        f"{result['conditions']['weather']}\n\n"

        f"🏆 Победитель:\n"

        f"{winner['name']}\n\n"

        f"❌ Проиграл:\n"

        f"{loser['name']}"

    )



    if result["critical"]:


        text += (

            "\n\n🔥 КРИТИЧЕСКАЯ ПОБЕДА!"

        )



    return text