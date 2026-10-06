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

def static_files(path):


    return send_from_directory(

        "webapp",

        path

    )









# =========================
# PLAYER
# =========================


@app.route(

    "/api/player/<int:user_id>"

)

def player_api(user_id):


    return jsonify(

        get_player(

            user_id

        )

    )








# =========================
# CAR INFO
# =========================


@app.route(

    "/api/car/<path:name>"

)

def car_api(name):


    car = get_car(

        name

    )


    if not car:


        return jsonify(

            {

                "error":

                "Car not found"

            }

        )



    return jsonify(

        car

    )









# =========================
# GARAGE
# =========================


@app.route(

    "/api/garage/<int:user_id>"

)

def garage_api(user_id):


    player = get_player(

        user_id

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

    "/api/car/main",

    methods=["POST"]

)

def main_car_api():


    data = request.json



    user_id = int(

        data["user_id"]

    )


    car = data["car"]



    player = get_player(

        user_id

    )



    if car not in player["garage"]:


        return jsonify(

            {

                "success":False

            }

        )



    player["main_car"] = car



    update_player(

        user_id,

        player

    )



    return jsonify(

        {

            "success":True

        }

    )









# =========================
# SHOP
# =========================


@app.route("/api/shop")

def shop_api():


    return jsonify(

        get_shop_cars()

    )







@app.route(

    "/api/shop/buy",

    methods=["POST"]

)

def buy_api():


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
# RACES
# =========================


@app.route(

    "/api/race/npc",

    methods=["POST"]

)

def npc_race_api():


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








@app.route(

    "/api/race/boss",

    methods=["POST"]

)

def boss_race_api():


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
# UPDATE
# =========================


@app.route(

    "/api/player/update",

    methods=["POST"]

)

def update_api():


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