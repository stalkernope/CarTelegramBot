from cars import random_car


def daily_car_text():

    car = random_car()


    text = (

        "━━━━━━━━━━━━━━\n\n"

        "🔥 <b>CAR OF THE DAY</b>\n\n"

        f"🏎 <b>{car['name']}</b>\n\n"

        f"🏷 Бренд:\n"
        f"{car['brand']}\n\n"

        f"⚡ Мощность:\n"
        f"{car['power']}\n\n"

        f"🚀 Скорость:\n"
        f"{car['speed']}\n\n"

        f"💎 Редкость:\n"
        f"{car['rarity']}\n\n"

        f"💰 Цена:\n"
        f"{car['price']}\n\n"

        "📖 История:\n"

        f"{car['description']}\n\n"

        "━━━━━━━━━━━━━━\n"

        "👑 Car Legends Club"

    )


    return text, car