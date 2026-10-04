from database import (
    get_user,
    load_data,
    save_data
)

from config import USERS_FILE


LEVELS = [

    (0, "🚘 Новичок"),

    (100, "🏁 Автоэнтузиаст"),

    (500, "🔥 Auto Expert"),

    (1000, "💎 Car Collector"),

    (2500, "👑 Car Legend")

]


def get_level(xp):

    level = "🚘 Новичок"

    for points, name in LEVELS:

        if xp >= points:
            level = name

    return level



def update_level(user_id):

    users = load_data(USERS_FILE)

    uid = str(user_id)


    if uid in users:

        xp = users[uid]["xp"]

        users[uid]["level"] = get_level(xp)


        save_data(
            USERS_FILE,
            users
        )



def add_achievement(user_id, achievement):

    users = load_data(USERS_FILE)

    uid = str(user_id)


    if uid in users:

        achievements = users[uid].get(
            "achievements",
            []
        )


        if achievement not in achievements:

            achievements.append(
                achievement
            )


        users[uid]["achievements"] = achievements


        save_data(
            USERS_FILE,
            users
        )



def profile_text(user_id):

    user = get_user(user_id)


    cars = user.get(
        "cars",
        []
    )


    achievements = user.get(
        "achievements",
        []
    )


    text = (

        "👤 <b>CAR LEGENDS PROFILE</b>\n\n"

        f"⭐ Уровень:\n"
        f"{user['level']}\n\n"

        f"✨ XP: {user['xp']}\n"

        f"💰 Car Coins: {user['coins']}\n\n"

        f"🏎 Машин в гараже: "
        f"{len(cars)}\n\n"

    )


    if achievements:

        text += "🏅 Достижения:\n"

        for a in achievements:

            text += f"• {a}\n"

    else:

        text += (
            "🏅 Достижения:\n"
            "Пока нет"
        )


    return text