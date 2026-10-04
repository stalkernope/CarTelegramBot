# =========================
# РЕЙТИНГ МАШИН
# =========================


RARITY_SCORE = {

    "🔥 Mythic": 100,

    "💎 Legendary": 80,

    "🟣 Rare": 60,

    "🔵 Rare": 50

}




def get_rating(car):


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


    rarity_points = RARITY_SCORE.get(

        rarity,

        40

    )



    rating = (

        power / 20

        +

        speed / 5

        +

        rarity_points

    ) / 3



    if rating > 100:

        rating = 100



    return round(
        rating
    )





def rating_text(car):


    return (

        f"⭐ Рейтинг машины: "

        f"{get_rating(car)}/100"

    )