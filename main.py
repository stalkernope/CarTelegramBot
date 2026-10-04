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


# ==========================
# НАСТРОЙКИ
# ==========================

TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = "@toway2m"

INSTAGRAM = os.environ.get(
    "INSTAGRAM_URL",
    "https://instagram.com/"
)


USERS_FILE = "users.json"


# ==========================
# БАЗА МАШИН
# ==========================

CARS = [

{
"name":"Bugatti Chiron",
"power":"1500 л.с.",
"speed":"420 км/ч",
"price":"3 млн $",
"rarity":"🟡 Mythic"
},

{
"name":"Ferrari SF90 Stradale",
"power":"1000 л.с.",
"speed":"340 км/ч",
"price":"600 000 $",
"rarity":"🟣 Legendary"
},

{
"name":"Lamborghini Revuelto",
"power":"1015 л.с.",
"speed":"350 км/ч",
"price":"700 000 $",
"rarity":"🟣 Legendary"
},

{
"name":"Porsche 911 GT3 RS",
"power":"525 л.с.",
"speed":"296 км/ч",
"price":"250 000 $",
"rarity":"🔵 Rare"
},

{
"name":"Pagani Huayra",
"power":"730 л.с.",
"speed":"383 км/ч",
"price":"3 млн $",
"rarity":"🟡 Mythic"
},

{
"name":"Koenigsegg Jesko",
"power":"1600 л.с.",
"speed":"500+ км/ч",
"price":"3 млн $",
"rarity":"🟡 Mythic"
}

]


# ==========================
# СОХРАНЕНИЕ ПОЛЬЗОВАТЕЛЕЙ
# ==========================


def load_users():

    try:

        with open(
            USERS_FILE,
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:

        return {}



def save_users(data):

    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_user(user_id):

    users = load_users()

    uid = str(user_id)


    if uid not in users:

        users[uid] = {

            "xp":0,
            "coins":100,
            "cars":[]

        }

        save_users(users)


    return users[uid]



def add_car(user_id, car):

    users = load_users()

    uid = str(user_id)


    if uid in users:

        if car not in users[uid]["cars"]:

            users[uid]["cars"].append(car)

            users[uid]["xp"] += 50


    save_users(users)



def random_car():

    return random.choice(CARS)



def car_text(car):

    return (

        f"🏎 <b>{car['name']}</b>\n\n"

        f"⚡ Мощность: {car['power']}\n"
        f"🚀 Скорость: {car['speed']}\n"
        f"💰 Цена: {car['price']}\n"
        f"💎 Редкость: {car['rarity']}"

    )
    
    # ==========================
# КНОПКИ МЕНЮ
# ==========================


def menu():

    keyboard = [

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
            ),

            InlineKeyboardButton(
                "🏆 Мой гараж",
                callback_data="garage"
            )
        ],

        [
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
        keyboard
    )



# ==========================
# START
# ==========================


async def start(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    get_user(
        user.id
    )


    text = (

        "🏎 <b>CAR LEGENDS CLUB</b>\n\n"

        "Добро пожаловать в мир легендарных автомобилей.\n\n"

        "💎 Эксклюзивные машины\n"
        "🔥 Автомобиль дня\n"
        "⚔️ Битвы легенд\n"
        "🎲 Подбор машины\n"
        "🏆 Личный гараж\n\n"

        "Выбирай раздел ниже 👇"

    )


    await update.message.reply_text(

        text,

        parse_mode="HTML",

        reply_markup=menu()

    )



# ==========================
# КОМАНДА /car
# ==========================


async def car_command(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    car = random_car()


    add_car(
        user.id,
        car["name"]
    )


    await update.message.reply_text(

        "🔥 <b>Твоя машина дня:</b>\n\n"
        + car_text(car),

        parse_mode="HTML"

    )



# ==========================
# КОМАНДА /match
# ==========================


async def match_command(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    car = random_car()


    add_car(
        user.id,
        car["name"]
    )


    await update.message.reply_text(

        "🎲 <b>Тебе подходит:</b>\n\n"
        + car_text(car),

        parse_mode="HTML"

    )



# ==========================
# ПРОФИЛЬ
# ==========================


async def profile_command(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user = get_user(
        update.effective_user.id
    )


    text = (

        "👤 <b>CAR LEGENDS PROFILE</b>\n\n"

        f"⭐ XP: {user['xp']}\n"

        f"💰 Coins: {user['coins']}\n\n"

        "🏎 Гараж:\n"

    )


    if user["cars"]:

        for car in user["cars"]:

            text += (
                f"• {car}\n"
            )

    else:

        text += "Пусто"


    await update.message.reply_text(

        text,

        parse_mode="HTML"

    )



# ==========================
# КНОПКИ
# ==========================


async def buttons(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    if query.data == "match":

        car = random_car()

        add_car(
            user_id,
            car["name"]
        )


        await query.message.reply_text(

            "🎲 Твой автомобиль:\n\n"
            + car_text(car),

            parse_mode="HTML"

        )


    elif query.data == "daily":

        car = random_car()


        await query.message.reply_text(

            "🔥 CAR OF THE DAY\n\n"
            + car_text(car),

            parse_mode="HTML"

        )


    elif query.data == "garage":

        user = get_user(user_id)


        text = "🏆 Твой гараж:\n\n"


        if user["cars"]:

            for car in user["cars"]:

                text += f"🏎 {car}\n"

        else:

            text += "Пока пусто"


        await query.message.reply_text(
            text
        )


    elif query.data == "profile":

        user = get_user(user_id)


        await query.message.reply_text(

            f"👤 Профиль\n\n"
            f"⭐ XP: {user['xp']}\n"
            f"💰 Coins: {user['coins']}",

        )



    elif query.data == "battle":

        car1 = random_car()

        car2 = random_car()


        text = (

            "⚔️ <b>LEGEND BATTLE</b>\n\n"

            f"🏎 {car1['name']}\n"
            f"⚡ {car1['power']}\n\n"

            "VS\n\n"

            f"🏎 {car2['name']}\n"
            f"⚡ {car2['power']}\n\n"

            "🔥 Какая победит?"

        )


        await query.message.reply_text(

            text,

            parse_mode="HTML"

        )
        
        # ==========================
# АВТОПОСТЫ В КАНАЛ
# ==========================


async def daily_post(
    ctx: ContextTypes.DEFAULT_TYPE
):

    car = random_car()


    text = (

        "🔥 <b>CAR OF THE DAY</b>\n\n"

        + car_text(car)

        + "\n\n👑 Car Legends Club"

    )


    await ctx.bot.send_message(

        CHANNEL,

        text,

        parse_mode="HTML"

    )



async def battle_post(
    ctx: ContextTypes.DEFAULT_TYPE
):

    car1 = random_car()

    car2 = random_car()


    text = (

        "⚔️ <b>LEGEND BATTLE</b>\n\n"

        f"🏎 {car1['name']}\n"
        f"⚡ {car1['power']}\n\n"

        "🔥 VS 🔥\n\n"

        f"🏎 {car2['name']}\n"
        f"⚡ {car2['power']}\n\n"

        "Голосуйте за свою легенду 👇"

    )


    await ctx.bot.send_poll(

        CHANNEL,

        "Какая машина лучше? 🏎",

        [

            car1["name"],

            car2["name"]

        ],

        is_anonymous=False

    )



# ==========================
# ЗАПУСК
# ==========================


def main():


    app = (

        Application

        .builder()

        .token(TOKEN)

        .build()

    )


    # команды

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


    # кнопки

    app.add_handler(

        CallbackQueryHandler(
            buttons
        )

    )


    # ежедневные посты

    app.job_queue.run_daily(

        daily_post,

        time=time(
            12,
            0
        )

    )


    app.job_queue.run_daily(

        battle_post,

        time=time(
            19,
            0
        )

    )


    print(
        "🏎 Car Legends Club started!"
    )


    app.run_polling()



if __name__ == "__main__":

    main()
