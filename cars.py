# =========================
# CAR LEGENDS CLUB
# CARS DATABASE 5.0
# =========================


CARS = [

    {
        "name": "Bugatti Chiron Super Sport",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Bugatti_Chiron_Super_Sport_300%2B.jpg",
        "power": 1600,
        "speed": 440,
        "price": 3900000,
        "type": "Гиперкар",
        "rarity": "🔥 Mythic",
        "chance": 5
    },


    {
        "name": "Koenigsegg Jesko Absolut",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/4/42/Koenigsegg_Jesko_Absolut.jpg",
        "power": 1600,
        "speed": 500,
        "price": 3000000,
        "type": "Гиперкар",
        "rarity": "🔥 Mythic",
        "chance": 5
    },


    {
        "name": "Pagani Huayra BC",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/5/50/Pagani_Huayra_BC.jpg",
        "power": 800,
        "speed": 370,
        "price": 3500000,
        "type": "Эксклюзив",
        "rarity": "💎 Legendary",
        "chance": 10
    },


    {
        "name": "Ferrari LaFerrari",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/2/21/Ferrari_LaFerrari.jpg",
        "power": 963,
        "speed": 350,
        "price": 1500000,
        "type": "Гибридный суперкар",
        "rarity": "💎 Legendary",
        "chance": 10
    },


    {
        "name": "Lamborghini Aventador SVJ",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Lamborghini_Aventador_SVJ.jpg",
        "power": 770,
        "speed": 350,
        "price": 600000,
        "type": "Суперкар",
        "rarity": "🟣 Rare",
        "chance": 20
    },


    {
        "name": "Porsche 911 GT3 RS",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Porsche_911_GT3_RS.jpg",
        "power": 525,
        "speed": 296,
        "price": 250000,
        "type": "Спорткар",
        "rarity": "🔵 Rare",
        "chance": 25
    },


    {
        "name": "McLaren Senna",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/6/69/McLaren_Senna.jpg",
        "power": 800,
        "speed": 340,
        "price": 1000000,
        "type": "Трековый гиперкар",
        "rarity": "💎 Legendary",
        "chance": 15
    },


    {
        "name": "Mercedes-AMG ONE",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Mercedes-AMG_One.jpg",
        "power": 1049,
        "speed": 352,
        "price": 2700000,
        "type": "F1 для дороги",
        "rarity": "🔥 Mythic",
        "chance": 10
    }

]



def get_all_cars():

    return CARS



def get_car_by_name(name):

    for car in CARS:

        if car["name"] == name:

            return car

    return None