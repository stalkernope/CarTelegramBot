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


# =========================
# НАСТРОЙКИ
# =========================


TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = "@toway2m"

INSTAGRAM = os.environ.get(
    "INSTAGRAM_URL",
    "https://instagram.com/"
)


DATA_FILE = "users.json"



# =========================
# БАЗА МАШИН
# =========================


CARS = [

{
"name":"Bugatti Chiron Super Sport",
"power":"1600 л.с.",
"speed":"440 км/ч",
"price":"3 900 000$",
"type":"Гиперкар",
"rarity":"🔥 Mythic"
},

{
"name":"Koenigsegg Jesko Absolut",
"power":"1600 л.с.",
"speed":"500+ км/ч",
"price":"3 000 000$",
"type":"Гиперкар",
"rarity":"🔥 Mythic"
},

{
"name":"Pagani Huayra BC",
"power":"800 л.с.",
"speed":"370 км/ч",
"price":"3 500 000$",
"type":"Эксклюзив",
"rarity":"💎 Legendary"
},

{
"name":"Ferrari LaFerrari",
"power":"963 л.с.",
"speed":"350 км/ч",
"price":"1 500 000$",
"type":"Гибридный суперкар",
"rarity":"💎 Legendary"
},

{
"name":"Lamborghini Aventador SVJ",
"power":"770 л.с.",
"speed":"350 км/ч",
"price":"600 000$",
"type":"Суперкар",
"rarity":"🟣 Rare"
},

{
"name":"Porsche 911 GT3 RS",
"power":"525 л.с.",
"speed":"296 км/ч",
"price":"250 000$",
"type":"Спорткар",
"rarity":"🔵 Rare"
},

{
"name":"McLaren Senna",
"power":"800 л.с.",
"speed":"340 км/ч",
"price":"1 000 000$",
"type":"Трековый гиперкар",
"rarity":"💎 Legendary"
},

{
"name":"Mercedes AMG One",
"power":"1049 л.с.",
"speed":"352 км/ч",
"price":"2 700 000$",
"type":"Формула 1 для дороги",
"rarity":"🔥 Mythic"
}

]



# =========================
# ФРАЗЫ ДЛЯ MATCH
# =========================


MATCH_TEXT = [

"🔥 Ты любишь внимание. Твоя машина должна заставлять людей оборачиваться.",

"🏁 Ты создан для скорости и эмоций.",

"💎 Тебе подходят редкие машины с характером.",

"🌙 Твой стиль — ночной город, красивый звук и мощный мотор.",

"👑 Ты выбираешь не транспорт, а произведение искусства."

]



# =========================
# РАБОТА С БАЗОЙ
# =========================


def load_users():

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return {}



def save_users(users):

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            users,
            file,
            ensure_ascii=False,
            indent=4
        )



def create_user(user_id):

    users = load_users()

    uid = str(user_id)


    if uid not in users:

        users[uid] = {

            "xp":0,

            "coins":100,

            "garage":[],

            "level":1

        }

        save_users(users)


    return users[uid]



def add_car(user_id, car):

    users = load_users()

    uid = str(user_id)


    if uid not in users:

        create_user(user_id)


    if car not in users[uid]["garage"]:

        users[uid]["garage"].append(car)

        users[uid]["xp"] += 50


        if users[uid]["xp"] >= users[uid]["level"]*200:

            users[uid]["level"] += 1


        save_users(users)



def get_car():

    return random.choice(CARS)



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


def main_keyboard():

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
                "🎲 Какая машина мне подходит",
                callback_data="match"
            )
        ],

        [
            InlineKeyboardButton(
                "🏆 Мой гараж",
                callback_data="garage"
            ),

            InlineKeyboardButton(
                "👤 Профиль",
                callback_data="profile"
            )
        ],

        [
            InlineKeyboardButton(
                "📸 Мой Instagram",
                url=INSTAGRAM
            )
        ]

    ]


    return InlineKeyboardMarkup(
        buttons
    )



# =========================
# START
# =========================


async def start(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    create_user(
        user.id
    )


    text = """

🏎 <b>CAR LEGENDS CLUB</b>

Добро пожаловать в мир легендарных автомобилей 🌎

Здесь тебя ждут:

🔥 Эксклюзивные машины
⚔️ Автомобильные битвы
🎲 Подбор машины по характеру
🏆 Личный гараж коллекционера
💎 Редкие гиперкары

Выбирай свой путь 👇

"""


    await update.message.reply_text(

        text,

        parse_mode="HTML",

        reply_markup=main_keyboard()

    )



# =========================
# /CAR
# =========================


async def car_command(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    create_user(
        user.id
    )


    car = get_car()


    add_car(
        user.id,
        car["name"]
    )


    await update.message.reply_text(

        "🔥 <b>Эксклюзивная машина:</b>\n\n"
        + car_card(car),

        parse_mode="HTML"

    )



# =========================
# /MATCH
# =========================


async def match_command(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    create_user(
        user.id
    )


    car = get_car()


    add_car(
        user.id,
        car["name"]
    )


    text = (

        "🎲 <b>Твоя машина по характеру:</b>\n\n"

        + random.choice(MATCH_TEXT)

        + "\n\n"

        + car_card(car)

    )


    await update.message.reply_text(

        text,

        parse_mode="HTML"

    )



# =========================
# /PROFILE
# =========================


async def profile_command(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    user = create_user(
        user_id
    )


    text = (

        "👤 <b>ТВОЙ ПРОФИЛЬ</b>\n\n"

        f"⭐ Уровень: {user['level']}\n"

        f"🔥 XP: {user['xp']}\n"

        f"💰 Монеты: {user['coins']}\n\n"

        "🏎 Твой гараж:\n"

    )


    if user["garage"]:

        for car in user["garage"]:

            text += (
                f"• {car}\n"
            )


    else:

        text += "Пока пусто"



    await update.message.reply_text(

        text,

        parse_mode="HTML"

    )



# =========================
# BUTTONS
# =========================


async def button_handler(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query


    await query.answer()


    user_id = query.from_user.id


    create_user(
        user_id
    )



    # Машина дня

    if query.data == "daily":


        car = get_car()


        await query.message.reply_text(

            "🔥 <b>CAR OF THE DAY</b>\n\n"
            + car_card(car),

            parse_mode="HTML"

        )



    # Match

    elif query.data == "match":


        car = get_car()


        add_car(
            user_id,
            car["name"]
        )


        await query.message.reply_text(

            "🎲 Тебе подходит:\n\n"
            + random.choice(MATCH_TEXT)
            + "\n\n"
            + car_card(car),

            parse_mode="HTML"

        )



    # Garage

    elif query.data == "garage":


        user = create_user(
            user_id
        )


        text = "🏆 <b>ТВОЙ ГАРАЖ</b>\n\n"


        if user["garage"]:

            for car in user["garage"]:

                text += f"🏎 {car}\n"


        else:

            text += "Гараж пуст"



        await query.message.reply_text(

            text,

            parse_mode="HTML"

        )



    # Profile

    elif query.data == "profile":


        user = create_user(
            user_id
        )


        await query.message.reply_text(

            "👤 <b>Профиль</b>\n\n"

            f"⭐ Уровень: {user['level']}\n"

            f"🔥 XP: {user['xp']}\n"

            f"💰 Монеты: {user['coins']}",

            parse_mode="HTML"

        )
        
        # =========================
# БИТВА МАШИН
# =========================


async def battle_command(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    car1 = get_car()

    car2 = get_car()


    while car1["name"] == car2["name"]:

        car2 = get_car()



    await update.message.reply_poll(

        question="⚔️ Какая машина сильнее?",

        options=[

            car1["name"],

            car2["name"]

        ],

        is_anonymous=False

    )



# =========================
# БИТВА ДЛЯ КНОПКИ
# =========================


async def send_battle(
    message
):

    car1 = get_car()

    car2 = get_car()


    while car1["name"] == car2["name"]:

        car2 = get_car()



    await message.reply_poll(

        "⚔️ LEGEND BATTLE\n\n"
        "Выбирай победителя 🔥",

        [

            car1["name"],

            car2["name"]

        ],

        is_anonymous=False

    )



# =========================
# АВТОПОСТ МАШИНЫ ДНЯ
# =========================


async def daily_post(
    ctx: ContextTypes.DEFAULT_TYPE
):

    car = get_car()


    text = (

        "🔥 <b>ЭКСКЛЮЗИВ ДНЯ</b>\n\n"

        + car_card(car)

        + "\n\n"

        "👑 Car Legends Club\n"

        "Каждый день — новые легенды"

    )


    await ctx.bot.send_message(

        chat_id=CHANNEL,

        text=text,

        parse_mode="HTML"

    )



# =========================
# АВТОПОСТ БИТВЫ
# =========================


async def daily_battle(
    ctx: ContextTypes.DEFAULT_TYPE
):

    car1 = get_car()

    car2 = get_car()


    while car1["name"] == car2["name"]:

        car2 = get_car()



    await ctx.bot.send_poll(

        CHANNEL,

        "⚔️ БИТВА ЛЕГЕНД\n\nКакая машина лучше?",

        [

            car1["name"],

            car2["name"]

        ],

        is_anonymous=False

    )



# =========================
# ОБРАБОТКА КНОПКИ BATTLE
# =========================


async def battle_button(
    update: Update,
    ctx: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query


    if query.data == "battle":

        await query.answer()

        await send_battle(
            query.message
        )
        
        # =========================
# ЗАПУСК БОТА
# =========================


async def error_handler(
    update,
    ctx
):

    logging.error(
        f"Ошибка: {ctx.error}"
    )



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


    app.add_handler(

        CommandHandler(
            "battle",
            battle_command
        )

    )


    # Кнопки

    app.add_handler(

        CallbackQueryHandler(
            button_handler
        )

    )


    app.add_handler(

        CallbackQueryHandler(
            battle_button
        )

    )


    # Ошибки

    app.add_error_handler(
        error_handler
    )



    # Автоматические публикации

    app.job_queue.run_daily(

        daily_post,

        time=time(
            12,
            0
        )

    )


    app.job_queue.run_daily(

        daily_battle,

        time=time(
            19,
            0
        )

    )


    print(
        "🏎 Car Legends Club 4.0 запущен!"
    )


    app.run_polling()



if __name__ == "__main__":

    main()