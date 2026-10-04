# =========================
# CAR LEGENDS PROFILE
# =========================



def get_title(level):

    if level >= 50:

        return "👑 Автомобильный Бог"


    if level >= 30:

        return "🔥 Легенда дорог"


    if level >= 15:

        return "💎 Коллекционер легенд"


    if level >= 5:

        return "🏆 Опытный владелец"


    return "🚗 Новичок"





def profile_text(user):


    level = user.get(
        "level",
        1
    )


    xp = user.get(
        "xp",
        0
    )


    coins = user.get(
        "coins",
        0
    )


    garage = user.get(
        "garage",
        []
    )


    wins = user.get(
        "wins",
        0
    )


    losses = user.get(
        "losses",
        0
    )



    title = get_title(
        level
    )



    need_xp = level * 200



    return (

        "👤 <b>CAR LEGENDS PROFILE</b>\n\n"

        f"🎖 Титул:\n{title}\n\n"

        f"⭐ Уровень: {level}\n"

        f"🔥 XP: {xp}/{need_xp}\n\n"

        f"💰 Монеты: {coins}\n\n"

        f"🏎 Машин в гараже: {len(garage)}\n\n"

        f"⚔️ Победы: {wins}\n"

        f"❌ Поражения: {losses}"

    )