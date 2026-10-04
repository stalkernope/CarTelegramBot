# =========================
# ОТОБРАЖЕНИЕ МАШИН
# =========================


def car_text(car):

    if not car:

        return "❌ Машина не найдена"



    return (

        "🏎 <b>CAR LEGENDS</b>\n\n"

        f"🚘 {car.get('name','')}\n"

        f"🏭 {car.get('brand','')}\n"

        f"🌍 {car.get('country','')}\n\n"

        f"⚡ Мощность: {car.get('power',0)} л.с.\n"

        f"🚀 Скорость: {car.get('speed',0)} км/ч\n"

        f"💰 Цена: {car.get('price',0)}$\n"

        f"💎 Редкость: {car.get('rarity','')}\n\n"

        f"📝 {car.get('description','')}"

    )





def car_short(car):

    if not car:

        return "Нет машины"



    return (

        f"🏎 {car.get('name','')}\n"

        f"💎 {car.get('rarity','')}\n"

        f"⚡ {car.get('power',0)} л.с.\n"

        f"🚀 {car.get('speed',0)} км/ч"

    )