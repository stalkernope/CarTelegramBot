import json
import random
import os


CARS_FILE = "cars.json"



# =========================
# ЗАГРУЗКА МАШИН
# =========================


def load_cars():

    if not os.path.exists(CARS_FILE):

        return []


    try:

        with open(
            CARS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            cars = json.load(file)


            if isinstance(cars, list):

                return cars


            return []


    except Exception as e:

        print(
            "Ошибка cars.json:",
            e
        )


        return []




# =========================
# СОХРАНЕНИЕ
# =========================


def save_cars(cars):

    try:

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


    except Exception as e:

        print(

            "Ошибка сохранения машин:",

            e

        )




# =========================
# СЛУЧАЙНАЯ МАШИНА
# =========================


def get_random_car():

    cars = load_cars()


    if not cars:

        return None


    return random.choice(
        cars
    )




# =========================
# ПОИСК МАШИНЫ
# =========================


def get_car(name):

    cars = load_cars()


    for car in cars:


        if car.get("name") == name:

            return car



    return None




# =========================
# ДОБАВЛЕНИЕ МАШИНЫ
# =========================


def add_new_car(car):

    if not car:

        return



    cars = load_cars()


    cars.append(
        car
    )


    save_cars(
        cars
    )