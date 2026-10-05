# =========================
# PROFILE SYSTEM 2.0
# =========================


def profile_text(user):


    if not user:

        return "❌ Профиль не найден"



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


    coins = user.get(
        "coins",
        0
    )


    level = user.get(
        "level",
        1
    )


    xp = user.get(
        "xp",
        0
    )


    title = user.get(
        "title",
        "🚗 Новичок"
    )



    return (

        "👤 <b>CAR LEGENDS PROFILE</b>\n\n"

        f"👑 Титул: {title}\n"

        f"⭐ Уровень: {level}\n"

        f"🔥 XP: {xp}\n\n"

        f"🪙 Монеты: {coins}\n\n"

        "🏆 Статистика:\n"

        f"⚔️ Победы: {wins}\n"

        f"❌ Поражения: {losses}\n\n"

        "🏎 Коллекция:\n"

        f"🚘 Машин: {len(garage)}"

    )



# =========================
# КОРОТКИЙ ПРОФИЛЬ
# =========================


def short_profile(user):


    return (

        f"👤 {user.get('title','')}\n"

        f"⭐ LVL {user.get('level',1)}\n"

        f"🏎 Машин: {len(user.get('garage',[]))}"

    )