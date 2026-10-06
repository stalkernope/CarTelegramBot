import json
import os
import random



from database import (
    get_player,
    add_coins,
    add_xp,
    add_win,
    add_loss
)


from car_database import (
    get_car
)





RACE_HISTORY = "race_history.json"








# =========================
# BLACKLIST BOSSES
# =========================


BOSSES = [


    {

        "id":"15",

        "name":"🌑 Razor",

        "car":"Shadow GT",

        "power":2500,

        "reward":5000

    },


    {

        "id":"10",

        "name":"⚡ Bull",

        "car":"Lightning X",

        "power":5000,

        "reward":10000

    },


    {

        "id":"5",

        "name":"🔥 Ronnie",

        "car":"Supra X",

        "power":7500,

        "reward":20000

    },


    {

        "id":"1",

        "name":"👑 Black King",

        "car":"Legend X1",

        "power":12000,

        "reward":50000

    }

]







# =========================
# NPC
# =========================


NPC = [


    {

        "name":"Honda Civic",

        "power":500

    },


    {

        "name":"BMW M3",

        "power":1500

    },


    {

        "name":"Supra MK5",

        "power":3000

    },


    {

        "name":"Bugatti",

        "power":7000

    }

]








# =========================
# HISTORY
# =========================


def load_history():


    if not os.path.exists(

        RACE_HISTORY

    ):


        return {}



    try:


        with open(

            RACE_HISTORY,

            "r",

            encoding="utf-8"

        ) as f:


            return json.load(f)



    except:


        return {}








def save_history(data):


    with open(

        RACE_HISTORY,

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            data,

            f,

            ensure_ascii=False,

            indent=4

        )









def add_history(

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
# POWER
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



    return (

        car.get(

            "power",

            0

        )

        +

        car.get(

            "speed",

            0

        )

        +

        car.get(

            "handling",

            0

        )

    )








# =========================
# RANDOM NPC
# =========================


def get_enemy():


    return random.choice(

        NPC

    )








# =========================
# PLAYER RACE
# =========================


def race_npc(

    user_id,

    car_name

):


    player_power = calculate_power(

        user_id,

        car_name

    )



    enemy = get_enemy()



    player_score = (

        player_power

        +

        random.randint(

            -300,

            300

        )

    )



    enemy_score = (

        enemy["power"]

        +

        random.randint(

            -300,

            300

        )

    )





    if player_score >= enemy_score:


        reward = random.randint(

            1000,

            5000

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


            "win":True,


            "enemy":enemy["name"],


            "player_power":player_power,


            "enemy_power":enemy["power"],


            "reward":reward


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


            "win":False,


            "enemy":enemy["name"],


            "player_power":player_power,


            "enemy_power":enemy["power"],


            "reward":0


        }




    add_history(

        user_id,

        result

    )



    return result








# =========================
# BOSS FIGHT
# =========================


def fight_boss(

    user_id,

    car_name,

    boss_id

):


    boss = None



    for b in BOSSES:


        if b["id"] == boss_id:


            boss = b



    if not boss:


        boss = random.choice(

            BOSSES

        )



    power = calculate_power(

        user_id,

        car_name

    )



    score = power + random.randint(

        -500,

        500

    )



    boss_score = boss["power"] + random.randint(

        -500,

        500

    )



    if score >= boss_score:


        add_coins(

            user_id,

            boss["reward"]

        )


        add_xp(

            user_id,

            1000

        )


        add_win(

            user_id

        )


        result = {


            "win":True,


            "boss":boss["name"],


            "player_power":power,


            "boss_power":boss["power"],


            "reward":boss["reward"]


        }


    else:


        add_loss(

            user_id

        )


        result = {


            "win":False,


            "boss":boss["name"],


            "player_power":power,


            "boss_power":boss["power"],


            "reward":0

        }




    add_history(

        user_id,

        result

    )



    return result








# =========================
# TEXT
# =========================


def race_result_text(result):


    if result["win"]:


        text = "🏆 ПОБЕДА!\n\n"


    else:


        text = "❌ ПОРАЖЕНИЕ\n\n"



    if "enemy" in result:


        text += (

            f"🏎 Соперник: {result['enemy']}\n"

        )



    if "boss" in result:


        text += (

            f"👑 Босс: {result['boss']}\n"

        )



    text += (

        f"\n⚡ Твоя сила: {result['player_power']}\n"

        f"⚔️ Сила врага: {result.get('enemy_power', result.get('boss_power'))}\n"

    )



    if result.get("reward"):


        text += (

            f"\n💰 Награда: {result['reward']}"

        )



    return text
    
    # =========================
# BOSS RACE FIX
# =========================


import random


from database import (
    get_player,
    add_coins,
    add_xp,
    add_win,
    add_loss
)


from car_database import (
    get_car
)





# =========================
# BOSSES
# =========================


BOSSES = [

    {
        "id": 15,
        "name": "🌑 Razor",
        "car": "Shadow GT",
        "power": 2500,
        "reward": 5000
    },


    {
        "id": 10,
        "name": "🔥 Ronnie",
        "car": "Supra MK5",
        "power": 6000,
        "reward": 15000
    },


    {
        "id": 5,
        "name": "👑 Baron",
        "car": "Black Phantom",
        "power": 9000,
        "reward": 30000
    },


    {
        "id": 1,
        "name": "🏆 Black King",
        "car": "Legend X1",
        "power": 15000,
        "reward": 100000
    }

]





# =========================
# GET BOSS
# =========================


def get_boss():


    return random.choice(

        BOSSES

    )







# =========================
# CAR POWER
# =========================


def get_power(car_name):


    car = get_car(

        car_name

    )


    if not car:


        return 0



    return (

        car.get("power",0)

        +

        car.get("speed",0)

        +

        car.get("handling",0)

    )









# =========================
# NPC RACE
# =========================


def race_npc(

    user_id,

    car_name

):


    player_power = get_power(

        car_name

    )



    enemy_power = random.randint(

        500,

        5000

    )



    if player_power + random.randint(-200,200) >= enemy_power:


        reward = random.randint(

            1000,

            5000

        )


        add_coins(

            user_id,

            reward

        )


        add_xp(

            user_id,

            200

        )


        add_win(

            user_id

        )


        return {

            "win": True,

            "enemy_power": enemy_power,

            "player_power": player_power,

            "reward": reward

        }


    else:


        add_loss(

            user_id

        )


        return {

            "win": False,

            "enemy_power": enemy_power,

            "player_power": player_power,

            "reward": 0

        }







# =========================
# BOSS FIGHT
# =========================


def fight_boss(

    user_id,

    car_name,

    boss_id

):


    boss = None



    for b in BOSSES:


        if b["id"] == boss_id:


            boss = b



    if not boss:


        boss = get_boss()



    power = get_power(

        car_name

    )



    if power + random.randint(-500,500) >= boss["power"]:


        add_coins(

            user_id,

            boss["reward"]

        )


        add_xp(

            user_id,

            500

        )


        add_win(

            user_id

        )


        return {


            "win": True,

            "boss": boss["name"],

            "player_power": power,

            "boss_power": boss["power"],

            "reward": boss["reward"]

        }



    else:


        add_loss(

            user_id

        )


        return {


            "win": False,

            "boss": boss["name"],

            "player_power": power,

            "boss_power": boss["power"],

            "reward": 0

        }








# =========================
# RESULT TEXT
# =========================


def race_result_text(result):


    if result.get("win"):


        text = "🏆 ПОБЕДА!\n\n"


    else:


        text = "❌ ПОРАЖЕНИЕ\n\n"



    if "boss" in result:


        text += (

            f"👑 Босс: {result['boss']}\n"

        )



    text += (

        f"⚡ Твоя сила: {result.get('player_power',0)}\n"

    )



    if "enemy_power" in result:


        text += (

            f"🚗 Соперник: {result['enemy_power']}\n"

        )


    if "boss_power" in result:


        text += (

            f"👑 Сила босса: {result['boss_power']}\n"

        )


    if result.get("reward"):


        text += (

            f"\n💰 Награда: {result['reward']}"

        )


    return text