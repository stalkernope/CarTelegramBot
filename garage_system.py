from database import (
    get_player,
    update_player
)


from car_database import (
    get_car
)




# =========================
# РЕДКОСТЬ
# =========================


RARITY_POINTS = {

    "⚪ Common": 20,

    "🔵 Rare": 50,

    "🟣 Rare": 60,

    "💎 Legendary": 100,

    "🔥 Mythic": 200

}




# =========================
# МАШИНЫ ИГРОКА
# =========================


def get_garage_cars(user_id):

    player = get_player(
        user_id
    )


    cars = []


    for name in player.get(
        "garage",
        []
    ):


        car = get_car(
            name
        )


        if car:

            cars.append(
                car
            )


    return cars




# =========================
# СТОИМОСТЬ
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
# СДЕЛАТЬ ГЛАВНОЙ
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


    cars = get_garage_cars(

        user_id

    )



    text = (

        "🏢 <b>CAR LEGENDS GARAGE</b>\n\n"

        f"🚗 Машин: {stats['count']}\n"

        f"💰 Стоимость: {stats['value']}$\n"

        f"⭐ Рейтинг: {stats['rating']}/100\n\n"

    )



    if not cars:


        text += (

            "🚗 Гараж пуст\n\n"

            "Купи первую машину в автосалоне"

        )


        return text




    text += "🚘 <b>ТВОИ МАШИНЫ:</b>\n\n"



    for car in cars:


        if car["name"] == stats["main"]:

            mark = "👑"

        else:

            mark = "🚗"



        text += (

            f"{mark} {car['name']}\n"

            f"⚡ Мощность: {car.get('power',0)}\n"

            f"🚀 Скорость: {car.get('speed',0)}\n"

            f"💎 {car.get('rarity','')}\n\n"

        )



    text += (

        "👑 Главная машина:\n"

        f"{stats['main'] or 'Не выбрана'}"

    )



    return text