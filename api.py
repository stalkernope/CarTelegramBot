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





@app.route(

    "/<path:path>"

)

def files(path):


    return send_from_directory(

        "webapp",

        path

    )








# =========================
# ИГРОК
# =========================


@app.route(

    "/api/player/<user_id>"

)

def player(user_id):


    data = get_player(

        int(user_id)

    )


    return jsonify(

        data

    )








# =========================
# ГАРАЖ
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
# ГЛАВНАЯ МАШИНА
# =========================


@app.route(

    "/api/set_main_car",

    methods=["POST"]

)

def set_main_car():


    data = request.json



    user_id = data.get(

        "user_id"

    )


    car_name = data.get(

        "car"

    )



    player = get_player(

        int(user_id)

    )



    if car_name not in player.get(

        "garage",

        []

    ):


        return jsonify(

            {

                "success": False,

                "error": "Машины нет в гараже"

            }

        )



    player["main_car"] = car_name



    update_player(

        int(user_id),

        player

    )



    return jsonify(

        {

            "success": True,

            "main_car": car_name

        }

    )








# =========================
# МАГАЗИН
# =========================


@app.route(

    "/api/shop"

)

def shop():


    return jsonify(

        get_shop_cars()

    )








# =========================
# ПОКУПКА
# =========================


@app.route(

    "/api/buy",

    methods=["POST"]

)

def buy():


    data = request.json



    user_id = data.get(

        "user_id"

    )


    car = data.get(

        "car"

    )



    try:


        result = buy_car(

            int(user_id),

            car

        )



        return jsonify(

            {

                "success": True,

                "car": result

            }

        )


    except Exception as e:


        return jsonify(

            {

                "success": False,

                "error": str(e)

            }

        )








# =========================
# ОБНОВЛЕНИЕ
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

            "success": True

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