import json
import os
import random




CARS_FILE = "cars.json"






# =========================
# LOAD CARS
# =========================


def load_cars():


    if not os.path.exists(

        CARS_FILE

    ):


        return []



    try:


        with open(

            CARS_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)



    except Exception:


        return []









# =========================
# SAVE CARS
# =========================


def save_cars(cars):


    with open(

        CARS_FILE,

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
# ALL CARS
# =========================


def get_all_cars():


    return load_cars()







# =========================
# GET CAR
# =========================


def get_car(name):


    cars = load_cars()



    for car in cars:


        if car.get("name") == name:


            return car



    return None








# =========================
# RANDOM CAR
# =========================


def get_random_car():


    cars = load_cars()



    if not cars:


        return None



    return random.choice(

        cars

    )








# =========================
# ADD CAR
# =========================


def add_new_car(car):


    cars = load_cars()



    cars.append(

        car

    )



    save_cars(

        cars

    )








# =========================
# CAR POWER
# =========================


def get_car_power(name):


    car = get_car(

        name

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

    )