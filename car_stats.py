RARITY_POINTS = {

    "🔥 Mythic": 100,

    "💎 Legendary": 80,

    "🟣 Rare": 60,

    "🔵 Rare": 50

}



def get_car_rating(car):


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



def rating_text(car):

    rating = get_car_rating(
        car
    )


    return (

        f"⭐ Рейтинг: {rating}/100"

    )