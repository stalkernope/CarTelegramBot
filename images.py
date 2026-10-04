import urllib.parse


# =========================
# ФОТО МАШИН
# =========================

# Здесь можно потом добавлять свои прямые ссылки
# на фотографии машин

CAR_IMAGES = {

    "Bugatti Chiron Super Sport":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Bugatti%20Chiron%20Super%20Sport",


    "Koenigsegg Jesko Absolut":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Koenigsegg%20Jesko%20Absolut",


    "Pagani Huayra BC":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Pagani%20Huayra%20BC",


    "Ferrari LaFerrari":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Ferrari%20LaFerrari",


    "Lamborghini Aventador SVJ":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Lamborghini%20Aventador%20SVJ",


    "Porsche 911 GT3 RS":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Porsche%20911%20GT3%20RS",


    "McLaren Senna":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=McLaren%20Senna",


    "Mercedes AMG One":
    "https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Mercedes%20AMG%20One"

}



# =========================
# ПОЛУЧЕНИЕ ФОТО
# =========================


def get_car_image(car):


    # если в базе машины уже есть своё фото

    if "photo" in car:

        if car["photo"]:

            return car["photo"]



    # берём по названию

    name = car.get(
        "name",
        ""
    )


    if name in CAR_IMAGES:

        return CAR_IMAGES[name]



    # запасной поиск

    query = urllib.parse.quote(

        name + " car"

    )


    return (

        "https://commons.wikimedia.org/"

        "w/index.php?search="

        + query

        + "&title=Special:MediaSearch"

    )