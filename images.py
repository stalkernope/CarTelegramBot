import urllib.parse



# =========================
# ПОЛУЧЕНИЕ ФОТО МАШИНЫ
# =========================


def get_car_image(car):

    # если фото уже есть в базе

    if "photo" in car:

        if car["photo"]:

            return car["photo"]



    # запасной вариант:
    # ссылка на поиск изображения

    name = car["name"]


    query = urllib.parse.quote(
        name + " car"
    )


    return (
        "https://commons.wikimedia.org/"
        "w/index.php?search="
        + query
        + "&title=Special:MediaSearch"
    )



# =========================
# КАРТОЧКА ДЛЯ ФОТО
# =========================


def photo_caption(car):

    return (

        f"🏎 <b>{car['name']}</b>\n\n"

        f"🏭 Бренд: {car.get('brand','')}\n"

        f"🌍 Страна: {car.get('country','')}\n"

        f"⚡ Мощность: {car.get('power','')} л.с.\n"

        f"🚀 Скорость: {car.get('speed','')} км/ч\n"

        f"💎 Редкость: {car.get('rarity','')}\n\n"

        "🔥 Car Legends Club"

    )