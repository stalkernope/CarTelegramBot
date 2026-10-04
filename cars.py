import random


CARS = [

    {
        "name": "Bugatti Chiron",
        "brand": "Bugatti",
        "power": "1500 л.с.",
        "speed": "420 км/ч",
        "price": "≈ 3 млн $",
        "rarity": "🟡 MYTHIC",
        "type": "Hypercar",
        "description":
        "Одна из самых быстрых машин мира с легендарным W16 двигателем."
    },


    {
        "name": "Ferrari LaFerrari",
        "brand": "Ferrari",
        "power": "963 л.с.",
        "speed": "350 км/ч",
        "price": "≈ 1.5 млн $",
        "rarity": "🟣 LEGENDARY",
        "type": "Supercar",
        "description":
        "Гибридная легенда Ferrari, созданная на основе технологий Формулы-1."
    },


    {
        "name": "Lamborghini Revuelto",
        "brand": "Lamborghini",
        "power": "1015 л.с.",
        "speed": "350 км/ч",
        "price": "≈ 600 000 $",
        "rarity": "🟣 LEGENDARY",
        "type": "Supercar",
        "description":
        "Новый V12 Lamborghini с агрессивным характером."
    },


    {
        "name": "Porsche 911 GT3 RS",
        "brand": "Porsche",
        "power": "525 л.с.",
        "speed": "296 км/ч",
        "price": "≈ 250 000 $",
        "rarity": "🔵 RARE",
        "type": "Track Car",
        "description":
        "Создан для тех, кто любит настоящие эмоции от управления."
    },


    {
        "name": "Pagani Huayra",
        "brand": "Pagani",
        "power": "730 л.с.",
        "speed": "383 км/ч",
        "price": "≈ 3 млн $",
        "rarity": "🟡 MYTHIC",
        "type": "Hypercar",
        "description":
        "Ручная работа искусства и инженерии из Италии."
    },


    {
        "name": "Koenigsegg Jesko",
        "brand": "Koenigsegg",
        "power": "1600 л.с.",
        "speed": "500+ км/ч",
        "price": "≈ 3 млн $",
        "rarity": "🟡 MYTHIC",
        "type": "Hypercar",
        "description":
        "Шведский гиперкар, созданный ради абсолютной скорости."
    },


    {
        "name": "McLaren P1",
        "brand": "McLaren",
        "power": "916 л.с.",
        "speed": "350 км/ч",
        "price": "≈ 1.3 млн $",
        "rarity": "🟣 LEGENDARY",
        "type": "Hybrid Hypercar",
        "description":
        "Одна из легендарной троицы гиперкаров вместе с Ferrari и Porsche."
    },


    {
        "name": "Aston Martin Valkyrie",
        "brand": "Aston Martin",
        "power": "1160 л.с.",
        "speed": "350 км/ч",
        "price": "≈ 3 млн $",
        "rarity": "🟡 MYTHIC",
        "type": "Hypercar",
        "description":
        "Почти гоночный болид для дорог общего пользования."
    }

]



def random_car():

    return random.choice(CARS)



def get_car(name):

    for car in CARS:

        if car["name"] == name:

            return car

    return None



def format_car(car):

    return (

        f"🏎 <b>{car['name']}</b>\n\n"

        f"🏷 Марка: {car['brand']}\n"
        f"⚡ Мощность: {car['power']}\n"
        f"🚀 Скорость: {car['speed']}\n"
        f"💰 Цена: {car['price']}\n"
        f"💎 Редкость: {car['rarity']}\n"
        f"🏁 Класс: {car['type']}\n\n"

        f"📖 {car['description']}"

    )