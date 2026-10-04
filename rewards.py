import json
import os
from datetime import datetime


REWARDS_FILE = "rewards.json"



def load_rewards():

    if not os.path.exists(REWARDS_FILE):

        return {}


    with open(
        REWARDS_FILE,
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_rewards(data):

    with open(
        REWARDS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )



def daily_reward(user_id):

    data = load_rewards()

    uid = str(user_id)


    today = str(
        datetime.now().date()
    )


    if uid not in data:

        data[uid] = {

            "last": "",

            "streak": 0

        }



    if data[uid]["last"] == today:

        return {

            "success": False,

            "message":
            "🎁 Ты уже получил награду сегодня"

        }



    data[uid]["last"] = today

    data[uid]["streak"] += 1



    save_rewards(data)



    coins = 500 + (
        data[uid]["streak"] * 50
    )


    return {

        "success": True,

        "coins": coins,

        "streak": data[uid]["streak"]

    }