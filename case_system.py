# =========================
# CASE SYSTEM FINAL
# =========================


import random



from database import (
    get_player,
    update_player
)


from car_database import (
    get_all_cars
)








# =========================
# CASES
# =========================


CASES = {


    "normal_case": {

        "name":
        "Обычный кейс",

        "price":
        1000,

        "currency":
        "coins"

    },


    "premium_case": {

        "name":
        "Премиум кейс",

        "price":
        5000,

        "currency":
        "coins"

    },


    "legend_case": {

        "name":
        "Легендарный кейс",

        "price":
        1,

        "currency":
        "gems"

    }

}








# =========================
# GET CASES
# =========================


def get_cases():


    return CASES







# =========================
# RANDOM CAR
# =========================


def random_case_car(case_type):


    cars = get_all_cars()



    if not cars:

        return None




    if case_type == "legend_case":


        cars = [

            c for c in cars

            if c.get(
                "power",
                0
            ) >= 600

        ]



        if not cars:

            cars = get_all_cars()





    elif case_type == "premium_case":


        cars = [

            c for c in cars

            if c.get(
                "power",
                0
            ) >= 400

        ]



        if not cars:

            cars = get_all_cars()



    return random.choice(

        cars

    )








# =========================
# OPEN CASE
# =========================


def open_case(

    user_id,

    case_type="normal_case"

):


    if case_type not in CASES:


        raise Exception(

            "Кейс не найден"

        )





    player = get_player(

        user_id

    )



    case = CASES[case_type]






    if case["currency"] == "coins":


        if player.get(

            "coins",

            0

        ) < case["price"]:


            raise Exception(

                "Недостаточно монет"

            )



        player["coins"] -= case["price"]






    if case["currency"] == "gems":


        if player.get(

            "gems",

            0

        ) < case["price"]:


            raise Exception(

                "Недостаточно кристаллов"

            )



        player["gems"] -= case["price"]







    car = random_case_car(

        case_type

    )



    if not car:


        raise Exception(

            "Нет машин"

        )





    if "garage" not in player:


        player["garage"] = []





    player["garage"].append(

        car["name"]

    )





    update_player(

        user_id,

        player

    )





    return car







# =========================
# CASE RESULT TEXT
# =========================


def case_result_text(car):


    return f"""

🎁 <b>КЕЙС ОТКРЫТ</b>


🚗 Вы получили:

<b>{car['name']}</b>


⚡ POWER:
{car.get('power',0)}


🚀 SPEED:
{car.get('speed',0)}

"""