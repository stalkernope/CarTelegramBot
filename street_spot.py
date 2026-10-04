import os
import json
from datetime import datetime


STREET_FILE = "data/street_spots.json"



def create_file():

    os.makedirs(
        "data",
        exist_ok=True
    )

    if not os.path.exists(STREET_FILE):

        with open(
            STREET_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                [],
                f,
                ensure_ascii=False,
                indent=4
            )



def load_spots():

    create_file()

    with open(
        STREET_FILE,
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_spots(data):

    with open(
        STREET_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def add_spot(
    user_id,
    car_name,
    photo_id
):

    spots = load_spots()


    spot = {

        "user": user_id,

        "car": car_name,

        "photo": photo_id,

        "date":
        str(datetime.now())

    }


    spots.append(
        spot
    )


    save_spots(
        spots
    )



def spot_text(car_name):

    return (

        "━━━━━━━━━━━━━━\n\n"

        "📸 <b>STREET SPOT</b>\n\n"

        f"🏎 <b>{car_name}</b>\n\n"

        "🔥 Автомобиль замечен на улице\n\n"

        "⭐ Оценка сообщества:\n"
        "★★★★★\n\n"

        "👑 Car Legends Club\n"

        "━━━━━━━━━━━━━━"

    )