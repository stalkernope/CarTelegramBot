import json
import os
import random


CAR_FILE = "cars.json"





# =========================
# DEFAULT CARS
# =========================


DEFAULT_CARS = [

    {
        "name": "BMW M3 GTR",
        "price": 0,
        "power": 500,
        "speed": 280,
        "handling": 80
    },

    {
        "name": "Toyota Supra",
        "price": 5000,
        "power": 450,
        "speed": 300,
        "handling": 85
    },

    {
        "name": "Nissan GTR",
        "price": 12000,
        "power": 565,
        "speed": 320,
        "handling": 90
    },

    {
        "name": "Lamborghini Huracan",
        "price": 50000,
        "power": 640,
        "speed": 340,
        "handling": 95
    }

]





# =========================
# LOAD CARS
# =========================


def load_cars():


    if not os.path.exists(CAR_FILE):

        save_cars(

            DEFAULT_CARS

        )

        return DEFAULT_CARS



    try:

        with open(

            CAR_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except Exception:


        return DEFAULT_CARS







# =========================
# SAVE CARS
# =========================


def save_cars(cars):


    with open(

        CAR_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            cars,

            file,

            ensure_ascii=False,

            indent=4

        )







# =========================
# GET ALL CARS
# =========================


def get_all_cars():


    return load_cars()







# =========================
# GET CAR
# =========================


def get_car(car_name):


    cars = load_cars()



    for car in cars:


        if car.get("name") == car_name:


            return car



    return None







# =========================
# RANDOM CAR
# =========================


def get_random_car():


    cars = load_cars()


    return random.choice(

        cars

    )







# =========================
# PLAYER GARAGE
# =========================


def add_car(

    user_id,

    car_name

):


    from database import (

        get_player,

        update_player

    )



    player = get_player(

        user_id

    )



    if "garage" not in player:


        player["garage"] = []




    if car_name not in player["garage"]:


        player["garage"].append(

            car_name

        )



    if not player.get("main_car"):


        player["main_car"] = car_name



    update_player(

        user_id,

        player

    )







def remove_car(

    user_id,

    car_name

):


    from database import (

        get_player,

        update_player

    )



    player = get_player(

        user_id

    )



    if car_name in player.get(

        "garage",

        []

    ):


        player["garage"].remove(

            car_name

        )



    if player.get(

        "main_car"

    ) == car_name:


        player["main_car"] = None



    update_player(

        user_id,

        player

    )