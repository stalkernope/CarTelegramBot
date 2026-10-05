from database import (
    get_player,
    update_player
)


from car_database import (
    get_car
)


from upgrade_system import (
    get_car_upgrade
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
# ХАРАКТЕРИСТИКИ С ПРОКАЧКОЙ
# =========================


def get_car_stats(

    user_id,

    car

):


    upgrade = get_car_upgrade(

        user_id,

        car["name"]

    )



    return {


        "power":

        car.get(

            "power",

            0

        )

        +

        upgrade.get(

            "power",

            0

        ),



        "speed":

        car.get(

            "speed",

            0

        )

        +

        upgrade.get(

            "speed",

            0

        ),



        "level":

        upgrade.get(

            "level",

            1

        )

    }




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
# РЕЙТИНГ
# =========================


def garage_rating(user_id):


    cars = get_garage_cars(

        user_id

    )



    if not cars:

        return 0



    score = 0



    for car in cars:


        stats = get_car_stats(

            user_id,

            car

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

            stats["power"] / 20

            +

            stats["speed"] / 5

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
# КАРТОЧКА МАШИНЫ
# =========================


def car_card_text(

    user_id,

    car

):


    player = get_player(

        user_id

    )


    stats = get_car_stats(

        user_id,

        car

    )



    if player.get(

        "main_car"

    ) == car["name"]:


        main = "👑 Главная машина"


    else:


        main = "🚗 Не выбрана"



    return (

        f"{car['name']}\n\n"

        f"💎 Редкость: {car.get('rarity','')}\n\n"

        f"⭐ Уровень: "

        f"{stats['level']}/10\n\n"

        f"⚡ Мощность: "

        f"{stats['power']}\n"

        f"🚀 Скорость: "

        f"{stats['speed']}\n\n"

        f"💰 Цена: "

        f"{car.get('price',0)}$\n\n"

        f"{main}"

    )




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

            "Купи машину в автосалоне"

        )


        return text




    text += (

        "🚘 <b>АВТОПАРК:</b>\n\n"

    )



    for car in cars:


        stats_car = get_car_stats(

            user_id,

            car

        )



        if car["name"] == stats["main"]:


            icon = "👑"


        else:


            icon = "🚗"



        text += (

            f"{icon} {car['name']}\n"

            f"⭐ Ур. {stats_car['level']}/10\n"

            f"⚡ {stats_car['power']} "

            f"🚀 {stats_car['speed']}\n\n"

        )



    return text