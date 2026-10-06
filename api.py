from flask import (
    Flask,
    jsonify,
    request,
    send_from_directory
)

import os


from database import (
    get_player,
    update_player
)


from car_database import (
    get_car
)


from shop_cars import (
    get_shop_cars,
    buy_car
)


from race_system import (
    race_npc,
    fight_boss,
    race_result_text
)





# =========================
# APP
# =========================


app = Flask(

    __name__,

    static_folder="webapp"

)





# =========================
# MINI APP
# =========================


@app.route("/")

def home():

    return send_from_directory(

        "webapp",

        "index.html"

    )





@app.route("/<path:path>")

def files(path):

    return send_from_directory(

        "webapp",

        path

    )







# =========================
# PLAYER
# =========================


@app.route(

    "/api/player/<user_id>"

)

def player(user_id):


    return jsonify(

        get_player(

            int(user_id)

        )

    )








# =========================
# GARAGE
# =========================


@app.route(

    "/api/garage/<user_id>"

)

def garage(user_id):


    player = get_player(

        int(user_id)

    )


    cars = []


    for name in player.get(

        "garage",

        []

    ):


        car = get_car(

            name

        )


        if car:

            cars.append(

                car

            )



    return jsonify(

        cars

    )








# =========================
# MAIN CAR
# =========================


@app.route(

    "/api/set_main_car",

    methods=["POST"]

)

def set_main_car():


    data = request.json


    user_id = data["user_id"]

    car = data["car"]



    player = get_player(

        int(user_id)

    )



    if car not in player["garage"]:


        return jsonify(

            {

                "success":False,

                "error":"Нет такой машины"

            }

        )



    player["main_car"] = car



    update_player(

        int(user_id),

        player

    )


    return jsonify(

        {

            "success":True,

            "main_car":car

        }

    )








# =========================
# SHOP
# =========================


@app.route(

    "/api/shop"

)

def shop():


    return jsonify(

        get_shop_cars()

    )







@app.route(

    "/api/buy",

    methods=["POST"]

)

def buy():


    data = request.json


    try:


        car = buy_car(

            int(data["user_id"]),

            data["car"]

        )


        return jsonify(

            {

                "success":True,

                "car":car

            }

        )



    except Exception as e:


        return jsonify(

            {

                "success":False,

                "error":str(e)

            }

        )








# =========================
# RACE NPC
# =========================


@app.route(

    "/api/race/npc",

    methods=["POST"]

)

def race_npc_api():


    data = request.json



    result = race_npc(

        int(data["user_id"]),

        data["car"]

    )



    return jsonify(

        {

            "result":result,

            "text":race_result_text(result)

        }

    )








# =========================
# BOSS RACE
# =========================


@app.route(

    "/api/race/boss",

    methods=["POST"]

)

def race_boss_api():


    data = request.json



    result = fight_boss(

        int(data["user_id"]),

        data["car"],

        data["boss"]

    )



    return jsonify(

        {

            "result":result,

            "text":race_result_text(result)

        }

    )








# =========================
# UPDATE PLAYER
# =========================


@app.route(

    "/api/update",

    methods=["POST"]

)

def update():


    data = request.json



    update_player(

        int(data["user_id"]),

        data["player"]

    )



    return jsonify(

        {

            "success":True

        }

    )








# =========================
# RUN
# =========================


def run_api():


    app.run(

        host="0.0.0.0",

        port=int(

            os.environ.get(

                "PORT",

                10000

            )

        )

    )