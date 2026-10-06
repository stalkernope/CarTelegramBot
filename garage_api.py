from flask import (
    Blueprint,
    request,
    jsonify
)


from database import (
    get_player,
    update_player
)



garage_api = Blueprint(

    "garage_api",

    __name__

)




# =========================
# СДЕЛАТЬ ГЛАВНОЙ
# =========================


@garage_api.route(

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



    if car_name not in player["garage"]:


        return jsonify(

            {

                "success": False,

                "error": "Машины нет в гараже"

            }

        )



    player["main_car"] = car_name



    update_player(

        user_id,

        player

    )



    return jsonify(

        {

            "success": True,

            "main_car": car_name

        }

    )