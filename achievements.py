def get_achievements(player):


    garage = player.get(
        "garage",
        []
    )


    wins = player.get(
        "wins",
        0
    )


    result = []


    # первая машина

    if len(garage) >= 1:

        result.append(
            "🚗 Первый автомобиль ✅"
        )

    else:

        result.append(
            "🚗 Первый автомобиль 🔒"
        )



    # коллекция

    if len(garage) >= 10:

        result.append(
            "💎 Коллекционер ✅"
        )

    else:

        result.append(
            f"💎 Коллекционер 🔒 ({len(garage)}/10)"
        )



    # победы

    if wins >= 10:

        result.append(
            "⚔️ Воин арены ✅"
        )

    else:

        result.append(
            f"⚔️ Воин арены 🔒 ({wins}/10)"
        )


    return result



def achievements_text(player):


    text = (

        "🏆 <b>ДОСТИЖЕНИЯ</b>\n\n"

    )


    for item in get_achievements(player):

        text += (

            item

            +

            "\n\n"

        )


    return text