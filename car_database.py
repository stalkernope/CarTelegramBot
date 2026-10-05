import json
import os
import random



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



    except Exception as e:

        print(
            "Ошибка загрузки машин:",
            e
        )



    return []



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
# РЕЙТИНГ
# =========================


RARITY_POINTS = {


    "🔥 Mythic": 100,


    "💎 Legendary": 80,


    "🟣 Rare": 60,


    "🔵 Rare": 50


}



def calculate_rating(car):


    power = car.get(

        "power",

        0

    )


    speed = car.get(

        "speed",

        0

    )


    rarity = car.get(

        "rarity",

        ""

    )



    rarity_score = RARITY_POINTS.get(

        rarity,

        40

    )



    rating = (

        power / 20

        +

        speed / 5

        +

        rarity_score

    ) / 3



    if rating > 100:

        rating = 100



    return round(
        rating
    )



# =========================
# ДОПОЛНИТЬ ДАННЫЕ
# =========================


def prepare_car(car):


    if "rating" not in car:

        car["rating"] = calculate_rating(
            car
        )



    return car



# =========================
# СЛУЧАЙНАЯ МАШИНА
# =========================


def get_random_car():

    cars = load_cars()


    if not cars:

        return None



    car = random.choice(
        cars
    )


    return prepare_car(
        car
    )



# =========================
# НАЙТИ МАШИНУ
# =========================


def get_car(name):


    cars = load_cars()



    for car in cars:


        if car.get("name") == name:


            return prepare_car(
                car
            )



    return None



# =========================
# ВСЕ МАШИНЫ
# =========================


def get_all_cars():

    cars = load_cars()


    return [

        prepare_car(car)

        for car in cars

    ]



# =========================
# ДОБАВИТЬ НОВУЮ
# =========================


def add_new_car(car):


    cars = load_cars()


    cars.append(
        prepare_car(car)
    )


    save_cars(
        cars
    )
    
    # =========================
# ГАРАЖ ИГРОКА
# =========================


def player_has_car(
    player,
    car_name
):

    return car_name in player.get(
        "garage",
        []
    )




# =========================
# КУПИТЬ МАШИНУ
# =========================


def buy_car(
    player,
    car_name
):

    car = get_car(
        car_name
    )


    if not car:

        return False



    if player_has_car(
        player,
        car_name
    ):

        return False



    player["garage"].append(

        car_name

    )



    if player["main_car"] is None:

        player["main_car"] = car_name



    return True




# =========================
# ПРОДАТЬ МАШИНУ
# =========================


def sell_car(

    player,

    car_name

):


    if not player_has_car(

        player,

        car_name

    ):

        return False



    player["garage"].remove(

        car_name

    )



    if player["main_car"] == car_name:


        player["main_car"] = (

            player["garage"][0]

            if player["garage"]

            else None

        )



    return True




# =========================
# ВЫБОР ОСНОВНОЙ
# =========================


def set_main_car(

    player,

    car_name

):


    if not player_has_car(

        player,

        car_name

    ):

        return False



    player["main_car"] = car_name



    return True