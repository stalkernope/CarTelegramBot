from shop import (
    get_car_price,
    case_info
)


def shop_text():

    return """

🛒 <b>CAR LEGENDS SHOP</b>


🎁 LEGEND CASE

Попробуй получить редкую машину!


🔥 Mythic — 5%

💎 Legendary — 20%

🔵 Rare — 75%


Покупай, открывай и собирай коллекцию легенд 🏎

"""



def car_buy_text(car):

    price = get_car_price(
        car
    )


    return (

        "🛒 <b>ПОКУПКА МАШИНЫ</b>\n\n"

        f"🏎 {car['name']}\n\n"

        f"💎 Редкость: {car['rarity']}\n"

        f"💰 Цена: {price} 🪙\n\n"

        "Купить эту легенду?"

    )