import os
import json
import random
import logging

from datetime import time

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


logging.basicConfig(
    level=logging.INFO
)


TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = "@toway2m"

INSTAGRAM = os.environ.get(
    "INSTAGRAM_URL",
    "https://instagram.com/"
)


USERS_FILE = "users.json"



CARS = [

    {
        "name": "Bugatti Chiron Super Sport",
        "power": "1600 л.с.",
        "speed": "440 км/ч",
        "price": "3 900 000$",
        "type": "Гиперкар",
        "rarity": "🔥 Mythic"
    },

    {
        "name": "Koenigsegg Jesko Absolut",
        "power": "1600 л.с.",
        "speed": "500+ км/ч",
        "price": "3 000 000$",
        "type": "Гиперкар",
        "rarity": "🔥 Mythic"
    },

    {
        "name": "Lamborghini Aventador SVJ",
        "power": "770 л.с.",
        "speed": "350 км/ч",
        "price": "600 000$",
        "type": "Суперкар",
        "rarity": "💎 Legendary"
    },

    {
        "name": "Ferrari LaFerrari",
        "power": "963 л.с.",
        "speed": "350 км/ч",
        "price": "1 500 000$",
        "type": "Гибрид",
        "rarity": "💎 Legendary"
    },

    {
        "name": "McLaren Senna",
        "power": "800 л.с.",
        "speed": "340 км/ч",
        "price": "1 000 000$",
        "type": "Трековый",
        "rarity": "💎 Legendary"
    },

    {
        "name": "Mercedes AMG One",
        "power": "1049 л.с.",
        "speed": "352 км/ч",
        "price": "2 700 000$",
        "type": "F1 для дороги",
        "rarity": "🔥 Mythic"
    }

]


MATCH_TEXT = [

    "🔥 Ты любишь внимание. Тебе нужна машина, которую замечают все.",

    "🏁 Ты создан для скорости и эмоций.",

    "💎 Твой стиль — редкость и эксклюзив.",

    "🌙 Ночной город, мощный звук и спорткар.",

    "👑 Ты выбираешь легенды."
]

# =========================
# БАЗА ПОЛЬЗОВАТЕЛЕЙ
# =========================


def load_users():

    try:

        with open(
            USERS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:

        return {}



def save_users(users):

    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            users,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_user(user_id):

    users = load_users()

    uid = str(user_id)


    if uid not in users:

        users[uid] = {

            "level": 1,

            "xp": 0,

            "coins": 100,

            "garage": []

        }

        save_users(users)


    return users[uid]



def add_car(user_id, car_name):

    users = load_users()

    uid = str(user_id)


    if uid not in users:

        get_user(user_id)

        users = load_users()



    if car_name not in users[uid]["garage"]:

        users[uid]["garage"].append(
            car_name
        )

        users[uid]["xp"] += 50


        if users[uid]["xp"] >= users[uid]["level"] * 200:

            users[uid]["level"] += 1


        save_users(users)



def random_car():

    return random.choice(
        CARS
    )



def car_card(car):

    return (

        f"🏎 <b>{car['name']}</b>\n\n"

        f"⚡ Мощность: {car['power']}\n"

        f"🚀 Скорость: {car['speed']}\n"

        f"💰 Цена: {car['price']}\n"

        f"🏁 Тип: {car['type']}\n"

        f"💎 Редкость: {car['rarity']}"

    )



# =========================
# МЕНЮ
# =========================


def main_menu():

    buttons = [

        [

            InlineKeyboardButton(
                "🔥 Машина дня",
                callback_data="daily"
            ),

            InlineKeyboardButton(
                "⚔️ Битва машин",
                callback_data="battle"
            )

        ],

        [

            InlineKeyboardButton(
                "🎲 Моя машина",
                callback_data="match"
            )

        ],

        [

            InlineKeyboardButton(
                "🏆 Гараж",
                callback_data="garage"
            ),

            InlineKeyboardButton(
                "👤 Профиль",
                callback_data="profile"
            )

        ],

        [

            InlineKeyboardButton(
                "📸 Instagram",
                url=INSTAGRAM
            )

        ]

    ]


    return InlineKeyboardMarkup(
        buttons
    )
    
    # =========================
# КОМАНДЫ
# =========================


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    get_user(
        user.id
    )


    await update.message.reply_text(

        """
🏎 <b>CAR LEGENDS CLUB</b>

Добро пожаловать в мир легендарных автомобилей 🌎

🔥 Эксклюзивные машины
⚔️ Битвы машин
🎲 Подбор по характеру
🏆 Личный гараж

Выбирай раздел 👇
        """,

        parse_mode="HTML",

        reply_markup=main_menu()

    )



async def car_command(update, ctx):

    user = update.effective_user

    car = random_car()


    add_car(
        user.id,
        car["name"]
    )


    await update.message.reply_text(

        "🔥 <b>Эксклюзивная машина:</b>\n\n"
        + car_card(car),

        parse_mode="HTML"

    )



async def match_command(update, ctx):

    user = update.effective_user

    car = random_car()


    add_car(
        user.id,
        car["name"]
    )


    await update.message.reply_text(

        "🎲 <b>Твоя машина:</b>\n\n"

        + random.choice(MATCH_TEXT)

        + "\n\n"

        + car_card(car),

        parse_mode="HTML"

    )



async def profile_command(update, ctx):

    user = get_user(
        update.effective_user.id
    )


    text = (

        "👤 <b>ТВОЙ ПРОФИЛЬ</b>\n\n"

        f"⭐ Уровень: {user['level']}\n"

        f"🔥 XP: {user['xp']}\n"

        f"💰 Монеты: {user['coins']}\n\n"

        "🏎 Гараж:\n"

    )


    if user["garage"]:

        for car in user["garage"]:

            text += f"• {car}\n"

    else:

        text += "Пусто"



    await update.message.reply_text(

        text,

        parse_mode="HTML"

    )



# =========================
# БИТВА
# =========================


async def battle(message):

    car1 = random_car()

    car2 = random_car()


    while car1["name"] == car2["name"]:

        car2 = random_car()



    keyboard = [

        [

            InlineKeyboardButton(

                "🏎 " + car1["name"],

                callback_data="winner_" + car1["name"]

            )

        ],

        [

            InlineKeyboardButton(

                "🏎 " + car2["name"],

                callback_data="winner_" + car2["name"]

            )

        ]

    ]



    await message.reply_text(

        "⚔️ <b>БИТВА ЛЕГЕНД</b>\n\n"

        + car_card(car1)

        + "\n\n🔥 VS 🔥\n\n"

        + car_card(car2)

        + "\n\nКто победит?",

        parse_mode="HTML",

        reply_markup=InlineKeyboardMarkup(
            keyboard
        )

    )
    
    # =========================
# КНОПКИ
# =========================


async def button_handler(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id



    if query.data == "daily":

        car = random_car()


        await query.message.reply_text(

            "🔥 <b>МАШИНА ДНЯ</b>\n\n"
            + car_card(car),

            parse_mode="HTML"

        )


    elif query.data == "match":

        car = random_car()


        add_car(
            user_id,
            car["name"]
        )


        await query.message.reply_text(

            "🎲 <b>Тебе подходит:</b>\n\n"

            + random.choice(MATCH_TEXT)

            + "\n\n"

            + car_card(car),

            parse_mode="HTML"

        )


    elif query.data == "battle":

        await battle(
            query.message
        )


    elif query.data.startswith("winner_"):

        winner = query.data.replace(
            "winner_",
            ""
        )


        await query.edit_message_text(

            "🏆 <b>Победитель:</b>\n\n"
            + winner
            + "\n\n🔥 Спасибо за голос!",

            parse_mode="HTML"

        )


    elif query.data == "garage":

        user = get_user(
            user_id
        )


        text = "🏆 <b>ТВОЙ ГАРАЖ</b>\n\n"


        if user["garage"]:

            for car in user["garage"]:

                text += "🏎 " + car + "\n"

        else:

            text += "Гараж пуст"



        await query.message.reply_text(

            text,

            parse_mode="HTML"

        )


    elif query.data == "profile":

        user = get_user(
            user_id
        )


        await query.message.reply_text(

            "👤 <b>ПРОФИЛЬ</b>\n\n"

            f"⭐ Уровень: {user['level']}\n"
            f"🔥 XP: {user['xp']}\n"
            f"💰 Монеты: {user['coins']}",

            parse_mode="HTML"

        )



# =========================
# ПОСТЫ В КАНАЛ
# =========================


async def daily_post(
    ctx: ContextTypes.DEFAULT_TYPE
):

    car = random_car()


    await ctx.bot.send_message(

        chat_id=CHANNEL,

        text=

            "🔥 <b>ЭКСКЛЮЗИВ ДНЯ</b>\n\n"

            + car_card(car),

        parse_mode="HTML"

    )



async def battle_post(
    ctx: ContextTypes.DEFAULT_TYPE
):

    await ctx.bot.send_message(

        chat_id=CHANNEL,

        text=

            "⚔️ <b>БИТВА ЛЕГЕНД</b>\n\n"
            "Новая автомобильная битва уже скоро 🔥",

        parse_mode="HTML"

    )
    
    # =========================
# ОБРАБОТКА ОШИБОК
# =========================


async def error_handler(
    update,
    ctx
):

    logging.error(
        "Ошибка бота",
        exc_info=ctx.error
    )



# =========================
# ЗАПУСК
# =========================


def main():

    app = (

        Application

        .builder()

        .token(TOKEN)

        .build()

    )


    # Команды

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        CommandHandler(
            "car",
            car_command
        )
    )


    app.add_handler(
        CommandHandler(
            "match",
            match_command
        )
    )


    app.add_handler(
        CommandHandler(
            "profile",
            profile_command
        )
    )


    # Все кнопки через один обработчик

    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    # Автопосты

    app.job_queue.run_daily(
        daily_post,
        time(
            12,
            0
        )
    )


    app.job_queue.run_daily(
        battle_post,
        time(
            19,
            0
        )
    )


    app.add_error_handler(
        error_handler
    )


    print(
        "🏎 CAR LEGENDS CLUB запущен!"
    )


    app.run_polling()



if __name__ == "__main__":

    main()
    
    