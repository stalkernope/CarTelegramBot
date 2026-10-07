import random
import json
import os


CAR_FILE = "cars.json"


def load_cars():
    if not os.path.exists(CAR_FILE):
        return [
            {
                "name": "Toyota Supra",
                "price": 5000,
                "power": 300
            },
            {
                "name": "BMW M3",
                "price": 8000,
                "power": 420
            },
            {
                "name": "Nissan GTR",
                "price": 12000,
                "power": 565
            }
        ]

    with open(CAR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_random_car():
    cars = load_cars()

    return random.choice(cars)


def add_car(player_id, car):
    from database import get_player, update_player

    player = get_player(player_id)

    if "cars" not in player:
        player["cars"] = []

    player["cars"].append(car)

    update_player(player_id, player)


def remove_car(player_id, car):
    from database import get_player, update_player

    player = get_player(player_id)

    if car in player.get("cars", []):
        player["cars"].remove(car)

    update_player(player_id, player)