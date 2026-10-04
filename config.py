import os
from zoneinfo import ZoneInfo


# 🔐 Telegram настройки
TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = os.environ["CHANNEL_ID"]

ADMIN_ID = int(
    os.environ.get("ADMIN_ID", 0)
)


# 📸 Instagram
INSTAGRAM = os.environ.get(
    "INSTAGRAM_URL",
    "https://instagram.com/"
)


# 🤖 Имя бота
BOT_USERNAME = os.environ.get(
    "BOT_USERNAME",
    "CarLegendsBot"
)


# 🌍 Часовой пояс
TZ = ZoneInfo(
    "Europe/Amsterdam"
)


# 💾 Файлы базы данных
USERS_FILE = "data/users.json"

GARAGE_FILE = "data/garage.json"

VOTES_FILE = "data/votes.json"

CARS_FILE = "data/cars.json"