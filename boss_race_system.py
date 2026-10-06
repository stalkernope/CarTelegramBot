import json
import os
import random


from database import (
    get_player,
    add_coins,
    add_xp,
    add_win,
    add_loss,
    add_tuning_part,
    add_car
)


from car_database import (
    get_car
)


from tuning import (
    tuning_bonus
)


from pet_system import (
    get_pet_bonus
)



RACE_FILE = "race_history.json"




# =========================
# БОССЫ
# =========================


BOSSES = [

    {
        "id": "night_king",

        "name": "🌑 Night King",

        "car": "Shadow GT",

        "power": 2000,

        "reward": "🔥 Shadow Engine"
    },


    {
        "id": "speed_lord",

        "name": "⚡ Speed Lord",

        "car": "Lightning X",

        "power": 5000,

        "reward": "🚀 Turbo Ultimate"
    },


    {
        "id": "car_legend",

        "name": "👑 Car Legend",

        "car": "Legend X1",

        "power": 10000,

        "reward": "🏆 Legendary Car"
    }

]




# =========================
# NPC
# =========================


NPC_CARS = [

    {
        "name": "🚗 Honda Civic",

        "power": 500
    },


    {
        "name": "🏎 BMW M3",

        "power": 1500
    },


    {
        "name": "🔥 Supra MK5",

        "power": 3000
    },


    {
        "name": "👑 Bugatti X",

        "power": 7000
    }

]




# =========================
# СОХРАНЕНИЕ
# =========================


def load_history():

    if not os.path.exists(RACE_FILE):

        return {}


    try:

        with open(

            RACE_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




def save_history(data):

    with open(

        RACE_FILE,

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
# СИЛА МАШИНЫ
# =========================


def calculate_power(

    user_id,

    car_name

):


    car = get_car(

        car_name

    )


    if not car:

        return 0



    power = (

        car.get(

            "power",

            0

        )

        +

        car.get(

            "speed",

            0

        )

    )



    tune = tuning_bonus(

        user_id,

        car_name

    )



    power += (

        tune.get(

            "power",

            0

        )

        +

        tune.get(

            "speed",

            0

        )

    )



    pet = get_pet_bonus(

        user_id

    ) or {

        "power": 0,

        "speed": 0

    }



    power += (

        pet.get(

            "power",

            0

        )

        +

        pet.get(

            "speed",

            0

        )

    )



    return power




# =========================
# NPC
# =========================


def get_npc():


    return random.choice(

        NPC_CARS

    )




# =========================
# СОХРАНЕНИЕ РЕЗУЛЬТАТА
# =========================


def save_race_result(

    user_id,

    result

):


    data = load_history()


    uid = str(user_id)



    if uid not in data:


        data[uid] = []



    data[uid].append(

        result

    )



    save_history(

        data

    )




# =========================
# NPC ГОНКА
# =========================


def race_npc(

    user_id,

    car_name

):


    player_power = calculate_power(

        user_id,

        car_name

    )



    enemy = get_npc()



    enemy_power = enemy["power"]



    player_score = (

        player_power

        +

        random.randint(

            -300,

            300

        )

    )



    enemy_score = (

        enemy_power

        +

        random.randint(

            -300,

            300

        )

    )



    if player_score >= enemy_score:


        reward = random.randint(

            1000,

            3000

        )


        add_coins(

            user_id,

            reward

        )


        add_xp(

            user_id,

            300

        )


        add_win(

            user_id

        )



        result = {


            "type":

            "npc",


            "win":

            True,


            "enemy":

            enemy["name"],


            "player_power":

            player_power,


            "enemy_power":

            enemy_power,


            "reward":

            reward

        }



    else:


        add_loss(

            user_id

        )


        add_xp(

            user_id,

            100

        )



        result = {


            "type":

            "npc",


            "win":

            False,


            "enemy":

            enemy["name"],


            "player_power":

            player_power,


            "enemy_power":

            enemy_power,


            "reward":

            0

        }



    save_race_result(

        user_id,

        result

    )



    return result
    
    # =========================
# БОССЫ
# =========================


def get_boss(

    boss_id=None

):


    if boss_id:


        for boss in BOSSES:


            if boss["id"] == boss_id:


                return boss



    return random.choice(

        BOSSES

    )




# =========================
# НАГРАДА БОССА
# =========================


def give_boss_reward(

    user_id,

    reward

):


    if "Car" in reward:


        add_car(

            user_id,

            reward

        )


    else:


        add_tuning_part(

            user_id,

            reward

        )




# =========================
# БИТВА С БОССОМ
# =========================


def fight_boss(

    user_id,

    car_name,

    boss_id

):


    boss = get_boss(

        boss_id

    )



    player_power = calculate_power(

        user_id,

        car_name

    )



    boss_power = boss["power"]



    player_score = (

        player_power

        +

        random.randint(

            -500,

            500

        )

    )



    boss_score = (

        boss_power

        +

        random.randint(

            -500,

            500

        )

    )



    if player_score >= boss_score:


        reward = boss["reward"]



        give_boss_reward(

            user_id,

            reward

        )



        add_coins(

            user_id,

            5000

        )


        add_xp(

            user_id,

            1000

        )


        add_win(

            user_id

        )



        result = {


            "type":

            "boss",


            "win":

            True,


            "boss":

            boss["name"],


            "reward":

            reward,


            "player_power":

            player_power,


            "boss_power":

            boss_power

        }



    else:


        add_loss(

            user_id

        )



        result = {


            "type":

            "boss",


            "win":

            False,


            "boss":

            boss["name"],


            "reward":

            None,


            "player_power":

            player_power,


            "boss_power":

            boss_power

        }



    save_race_result(

        user_id,

        result

    )



    return result
    
    # =========================
# ТЕКСТ РЕЗУЛЬТАТА
# =========================


def race_result_text(result):


    if result["win"]:


        text = (

            "🏆 <b>ПОБЕДА!</b>\n\n"

        )


    else:


        text = (

            "❌ <b>ПОРАЖЕНИЕ</b>\n\n"

        )



    text += (

        f"🚗 Твоя сила:\n"

        f"⚡ {result.get('player_power',0)}\n\n"

    )



    if result.get("enemy"):


        text += (

            "🏎 Соперник:\n"

            f"{result['enemy']}\n\n"

        )



    if result.get("boss"):


        text += (

            "👑 Босс:\n"

            f"{result['boss']}\n\n"

        )



    text += (

        "⚔️ Сила соперника:\n"

        f"{result.get('enemy_power', result.get('boss_power',0))}\n"

    )



    if result.get("reward"):


        text += (

            "\n🎁 Награда:\n"

            f"{result['reward']}"

        )



    if isinstance(

        result.get("reward"),

        int

    ):


        text += (

            "\n\n💰 Монеты: "

            f"{result['reward']}"

        )



    return text




# =========================
# ИСТОРИЯ
# =========================


def get_race_history(

    user_id

):


    data = load_history()


    return data.get(

        str(user_id),

        []

    )




# =========================
# СТАТИСТИКА
# =========================


def race_stats(

    user_id

):


    history = get_race_history(

        user_id

    )


    wins = 0

    losses = 0



    for race in history:


        if race.get("win"):

            wins += 1

        else:

            losses += 1



    return {

        "races": len(history),

        "wins": wins,

        "losses": losses

    }




# =========================
# PVP
# =========================


def pvp_race(

    player_one,

    player_two

):


    power_one = player_one.get(

        "power",

        0

    )


    power_two = player_two.get(

        "power",

        0

    )



    if power_one >= power_two:


        return {


            "winner":

            player_one,


            "loser":

            player_two

        }



    return {


        "winner":

        player_two,


        "loser":

        player_one

    }