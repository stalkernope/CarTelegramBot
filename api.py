from flask import (
    Flask,
    jsonify,
    request,
    send_from_directory
)

import os



# =========================
# DATABASE
# =========================


from database import (
    get_player,
    update_player
)





# =========================
# CARS
# =========================


from car_database import (
    get_car,
    get_all_cars
)





# =========================
# SHOP
# =========================


from shop_cars import (
    get_shop_cars,
    buy_car
)





# =========================
# RACES
# =========================


from boss_race_system import (
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


    player = get_player(

        user_id

    )


    return jsonify(

        player

    )







# =========================
# CAR
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

        ),404



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


    result = []



    for car_name in player.get(

        "garage",

        []

    ):


        car = get_car(

            car_name

        )


        if car:


            result.append(

                car

            )



    return jsonify(

        result

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



    if car not in player.get(

        "garage",

        []

    ):


        return jsonify(

            {

                "success":False,

                "error":
                "Car not owned"

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


@app.route(

    "/api/shop"

)

def shop_api():


    return jsonify(

        get_shop_cars()

    )








@app.route(

    "/api/shop/buy",

    methods=["POST"]

)

def shop_buy_api():


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
# NPC RACE
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

            "text":

            race_result_text(

                result

            )

        }

    )









# =========================
# BOSS RACE
# =========================


@app.route(

    "/api/race/boss",

    methods=["POST"]

)

def boss_race_api():


    data = request.json



    result = fight_boss(

        int(data["user_id"]),

        data["car"],

        data.get(

            "boss",

            1

        )

    )



    return jsonify(

        {

            "result":result,

            "text":

            race_result_text(

                result

            )

        }

    )









# =========================
# UPDATE PLAYER
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
# HEALTH CHECK
# =========================


@app.route(

    "/health"

)

def health():


    return jsonify(

        {

            "status":

            "ok"

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