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


    with open(
        CARS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



# =========================
# СОХРАНЕНИЕ
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
# СЛУЧАЙНАЯ МАШИНА
# =========================


def get_random_car():

    cars = load_cars()


    if not cars:

        return None


    return random.choice(cars)



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
# ДОБАВЛЕНИЕ НОВОЙ МАШИНЫ В БАЗУ
# =========================


def add_new_car(car):

    cars = load_cars()


    cars.append(car)


    save_cars(cars)