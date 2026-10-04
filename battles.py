import random
import json
import os

from cars import CARS
from config import VOTES_FILE


BATTLES_FILE = "data/battles.json"



def create_battle_file():

    if not os.path.exists(BATTLES_FILE):

        with open(
            BATTLES_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {},
                f,
                ensure_ascii=False,
                indent=4
            )



def load_battles():

    create_battle_file()

    with open(
        BATTLES_FILE,
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_battles(data):

    with open(
        BATTLES_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def create_battle():

    cars = random.sample(
        CARS,
        2
    )

    return cars



def battle_text(car1, car2):

    return (

        "⚔️ <b>LEGEND BATTLE</b>\n\n"

        f"🏎 <b>{car1['name']}</b>\n"
        f"⚡ {car1['power']}\n"
        f"🚀 {car1['speed']}\n"
        f"💎 {car1['rarity']}\n\n"

        "        VS\n\n"

        f"🏎 <b>{car2['name']}</b>\n"
        f"⚡ {car2['power']}\n"
        f"🚀 {car2['speed']}\n"
        f"💎 {car2['rarity']}\n\n"

        "🔥 Кто победит?"
    )



def save_vote(winner):

    data = load_battles()


    if winner not in data:

        data[winner] = 0


    data[winner] += 1


    save_battles(data)



def top_battles():

    data = load_battles()


    result = sorted(
        data.items(),
        key=lambda x:x[1],
        reverse=True
    )


    return result[:10]