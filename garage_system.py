from database import (
    get_player,
    update_player
)


from car_database import (
    get_car
)




# =========================
# МАШИНЫ ИГРОКА
# =========================


def get_garage_cars(user_id):


    player = get_player(

        user_id

    )


    cars = []



    for car_name in player.get("garage", []):


        car = get_car(

            car_name

        )


        if car:

            cars.append(car)



    return cars




# =========================
# ТЕКСТ ГАРАЖА
# =========================


def garage_text(user_id):


    player = get_player(

        user_id

    )


    text = (

        "🚗 <b>ГАРАЖ</b>\n\n"

    )



    text += (

        f"🚘 Машин: "

        f"{len(player['garage'])}\n\n"

    )



    if player["main_car"]:


        text += (

            "👑 Главная машина:\n"

            f"{player['main_car']}\n"

        )


    else:


        text += (

            "❌ Главная машина не выбрана\n"

        )



    return text




# =========================
# КАРТОЧКА МАШИНЫ
# =========================


def car_text(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )


    car = get_car(

        car_name

    )



    if not car:


        return "❌ Машина не найдена"



    text = (

        f"{car['name']}\n\n"

        f"💎 Редкость: "

        f"{car.get('rarity','-')}\n\n"

        f"⭐ Уровень: "

        f"{car.get('level',1)}\n\n"

        f"⚡ Мощность: "

        f"{car.get('power',0)}\n"

        f"🚀 Скорость: "

        f"{car.get('speed',0)}\n"

        f"🎯 Управление: "

        f"{car.get('handling',0)}\n\n"

    )



    if player["main_car"] == car_name:


        text += (

            "👑 Главная машина\n"

        )



    else:


        text += (

            "🚗 Не выбрана"

        )



    return text




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


    if car_name not in player["garage"]:


        return False



    player["main_car"] = car_name



    update_player(

        user_id,

        player

    )


    return True




# =========================
# ДОБАВИТЬ МАШИНУ
# =========================


def add_car_to_garage(

    user_id,

    car_name

):


    player = get_player(

        user_id

    )


    if car_name not in player["garage"]:


        player["garage"].append(

            car_name

        )



    if player["main_car"] is None:


        player["main_car"] = car_name



    update_player(

        user_id,

        player

    )


    return True