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
    get_all_cars,
    get_car
)


from shop_cars import (
    get_shop_cars,
    buy_car
)



app = Flask(

    __name__,

    static_folder="webapp"

)



# =========================
# MINI APP ГЛАВНАЯ
# =========================


@app.route("/")
def home():

    return send_from_directory(

        "webapp",

        "index.html"

    )




# =========================
# СТАТИКА
# =========================


@app.route(
    "/<path:path>"
)

def static_files(path):


    return send_from_directory(

        "webapp",

        path

    )




# =========================
# ПРОФИЛЬ
# =========================


@app.route(

    "/api/player/<user_id>"

)

def player_data(user_id):


    player = get_player(

        int(user_id)

    )


    return jsonify(

        player

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


    for car_name in player["garage"]:


        car = get_car(

            car_name

        )


        if car:

            cars.append(

                car

            )


    return jsonify(

        cars

    )




# =========================
# МАГАЗИН
# =========================


@app.route(

    "/api/shop"

)

def shop():


    cars = get_shop_cars()



    return jsonify(

        cars

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


    car_name = data.get(

        "car"

    )



    try:


        car = buy_car(

            user_id,

            car_name

        )


        return jsonify(

            {

                "success":

                True,

                "car":

                car

            }

        )


    except Exception as e:


        return jsonify(

            {

                "success":

                False,

                "error":

                str(e)

            }

        )




# =========================
# СОХРАНЕНИЕ
# =========================


@app.route(

    "/api/update",

    methods=["POST"]

)

def update():


    data = request.json


    user_id = data["user_id"]


    player = data["player"]



    update_player(

        user_id,

        player

    )



    return jsonify(

        {

            "success":

            True

        }

    )




# =========================
# ЗАПУСК
# =========================


def run_api():


    app.run(

        host="0.0.0.0",

        port=int(

            os.environ.get(

                "PORT",

                5000

            )

        )

    )