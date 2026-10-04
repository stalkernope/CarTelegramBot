def car_text(car):

    return (

        f"🏎 <b>{car['name']}</b>\n\n"

        f"🏭 Бренд: {car['brand']}\n"

        f"🌍 Страна: {car['country']}\n"

        f"📅 Год: {car['year']}\n\n"

        f"⚡ Мощность: {car['power']} л.с.\n"

        f"🚀 Скорость: {car['speed']} км/ч\n"

        f"💰 Цена: {car['price']}$\n"

        f"💎 Редкость: {car['rarity']}\n\n"

        f"📝 {car['description']}"

    )