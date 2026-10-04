import random



RARITY_SCORE = {

    "🔥 Mythic": 100,

    "💎 Legendary": 80,

    "🟣 Rare": 60,

    "🔵 Rare": 50

}



def get_score(car):

    power = car.get(
        "power",
        0
    )


    speed = car.get(
        "speed",
        0
    )


    rarity = RARITY_SCORE.get(

        car.get(
            "rarity",
            ""
        ),

        40

    )


    return (

        power * 0.5

        +

        speed * 2

        +

        rarity

    )



def fight(car1, car2):


    score1 = get_score(
        car1
    )


    score2 = get_score(
        car2
    )


    if score1 > score2:

        winner = car1

        loser = car2


    else:

        winner = car2

        loser = car1



    return {

        "winner": winner,

        "loser": loser,

        "score":

        abs(
            score1-score2
        )

    }



def battle_text(result):


    winner = result["winner"]


    loser = result["loser"]



    return (

        "⚔️ <b>LEGEND BATTLE</b>\n\n"

        f"🏎 Победитель:\n"

        f"<b>{winner['name']}</b>\n\n"

        f"⚡ Мощность: {winner['power']}\n"

        f"🚀 Скорость: {winner['speed']}\n"

        f"💎 {winner['rarity']}\n\n"

        "🔥 Победа по характеристикам!"

    )