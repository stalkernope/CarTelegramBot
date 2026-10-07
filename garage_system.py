# =========================
# GARAGE SYSTEM FINAL
# =========================


from database import (
    get_player,
    update_player
)


from car_database import (
    get_car
)








# =========================
# GET GARAGE CARS
# =========================


def get_garage_cars(user_id):


    player = get_player(

        user_id

    )


    cars = []



    for car_name in player.get(

        "garage",

        []

    ):


        car = get_car(

            car_name

        )


        if car:


            cars.append(

                car

            )



    return cars







# =========================
# GARAGE TEXT
# =========================


def garage_text(user_id):


    player = get_player(

        user_id

    )



    cars = player.get(

        "garage",

        []

    )



    main = player.get(

        "main_car",

        "нет"

    )



    text = (

        "🚗 <b>ГАРАЖ</b>\n\n"

        f"Всего машин: {len(cars)}\n\n"

        f"👑 Главная:\n{main}\n\n"

    )



    if not cars:


        text += "Гараж пуст"



    else:


        for i, car in enumerate(

            cars,

            1

        ):


            text += (

                f"{i}. 🚘 {car}\n"

            )



    return text







# =========================
# CAR TEXT
# =========================


def car_text(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    if car_name not in player.get(

        "garage",

        []

    ):


        return (

            "❌ Машина не найдена"

        )



    car = get_car(

        car_name

    )



    if not car:


        return (

            "❌ Данные машины отсутствуют"

        )





    return f"""

🚗 <b>{car['name']}</b>


⚡ POWER:
{car.get('power',0)}


🚀 SPEED:
{car.get('speed',0)}


🎯 CONTROL:
{car.get('handling',0)}


💰 Цена:
{car.get('price',0)}

"""








# =========================
# SET MAIN CAR
# =========================


def set_main_car(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )



    if car_name not in player.get(

        "garage",

        []

    ):


        return False





    player["main_car"] = car_name



    update_player(

        user_id,

        player

    )



    return True







# =========================
# REMOVE FROM GARAGE
# =========================


def remove_from_garage(

    user_id,

    car_name

):


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



    return True