from database import get_player
from car_database import get_car



# =========================
# РЕДКОСТЬ
# =========================


RARITY_POINTS = {

    "🔵 Rare": 50,

    "🟣 Rare": 60,

    "💎 Legendary": 100,

    "🔥 Mythic": 200

}




# =========================
# ПОЛУЧИТЬ МАШИНЫ
# =========================


def get_garage_cars(user_id):

    player = get_player(
        user_id
    )


    cars = []


    for name in player["garage"]:

        car = get_car(
            name
        )


        if car:

            cars.append(
                car
            )


    return cars




# =========================
# СТОИМОСТЬ ГАРАЖА
# =========================


def garage_value(user_id):

    cars = get_garage_cars(
        user_id
    )


    total = 0


    for car in cars:

        total += car.get(
            "price",
            0
        )


    return total




# =========================
# РЕЙТИНГ ГАРАЖА
# =========================


def garage_rating(user_id):

    cars = get_garage_cars(
        user_id
    )


    if not cars:

        return 0



    score = 0



    for car in cars:


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

            20

        )



        score += (

            power / 20

            +

            speed / 5

            +

            rarity_score

        )



    rating = score / len(cars)



    if rating > 100:

        rating = 100



    return round(
        rating
    )




# =========================
# ГЛАВНАЯ МАШИНА
# =========================


def set_main_car(
    user_id,
    car_name
):

    player = get_player(
        user_id
    )


    if car_name in player["garage"]:

        player["main_car"] = car_name



    from database import update_player


    update_player(

        user_id,

        player

    )




# =========================
# СТАТИСТИКА
# =========================


def garage_stats(user_id):

    player = get_player(
        user_id
    )


    cars = get_garage_cars(
        user_id
    )


    return {

        "count":

        len(cars),


        "value":

        garage_value(
            user_id
        ),


        "rating":

        garage_rating(
            user_id
        ),


        "main":

        player.get(
            "main_car"
        )

    }




# =========================
# ТЕКСТ ГАРАЖА
# =========================


def garage_text(user_id):

    stats = garage_stats(
        user_id
    )


    text = (

        "🏢 <b>CAR LEGENDS GARAGE</b>\n\n"

        f"🚗 Машин: {stats['count']}\n"

        f"💰 Стоимость: {stats['value']}$\n"

        f"⭐ Рейтинг: {stats['rating']}/100\n\n"

    )


    if stats["main"]:

        text += (

            "👑 Главная машина:\n"

            +

            stats["main"]

        )

    else:

        text += "👑 Главная машина не выбрана"



    return text