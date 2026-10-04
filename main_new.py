import os
import logging
import random

from datetime import time

from telegram import Update

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


from keyboards import main_menu


from car_database import (
    get_random_car
)


from database import (
    get_player,
    add_car,
    add_coins
)


from profiles import (
    profile_text
)



logging.basicConfig(
    level=logging.INFO
)



TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = "@toway2m"



MATCH_TEXT = [

    "🔥 Ты создан для скорости и эмоций.",

    "🏁 Тебе нужна машина с характером.",

    "💎 Твой стиль — редкость и эксклюзив.",

    "🌙 Ночной город и мощный мотор — это твоё.",

    "👑 Ты выбираешь не транспорт, а легенду."

]



# =========================
# КАРТОЧКА МАШИНЫ
# =========================


def car_text(car):

    return (

        f"🏎 <b>{car['name']}</b>\n\n"

        f"🏭 Бренд: {car.get('brand','')}\n"

        f"🌍 Страна: {car.get('country','')}\n"

        f"📅 Год: {car.get('year','')}\n\n"

        f"⚡ Мощность: {car.get('power','')} л.с.\n"

        f"🚀 Скорость: {car.get('speed','')} км/ч\n"

        f"💰 Цена: {car.get('price','')} $\n"

        f"💎 Редкость: {car.get('rarity','')}\n"

        f"🏁 Категория: {car.get('category','')}\n\n"

        f"📖 {car.get('description','')}"

    )



# =========================
# START
# =========================


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    get_player(
        user.id
    )


    await update.message.reply_text(

        """
🏎 <b>CAR LEGENDS CLUB</b>


Добро пожаловать в мир легендарных автомобилей 🔥


🔥 Машины
⚔️ Битвы
🎁 Кейсы
🏆 Коллекция
💰 Экономика


Выбирай свой путь 👇
""",

        parse_mode="HTML",

        reply_markup=main_menu()

    )
    
    # =========================
# КОМАНДА CAR
# =========================


async def car_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    car = get_random_car()


    if not car:

        await update.message.reply_text(
            "❌ База машин пуста"
        )

        return



    add_car(

        user.id,

        car["name"]

    )


    await update.message.reply_text(

        "🔥 <b>ТЕБЕ ВЫПАЛА МАШИНА</b>\n\n"

        + car_text(car),

        parse_mode="HTML"

    )



# =========================
# MATCH
# =========================


async def match_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    car = get_random_car()


    add_car(

        user.id,

        car["name"]

    )


    await update.message.reply_text(

        "🎲 <b>ТВОЯ МАШИНА ПО ХАРАКТЕРУ</b>\n\n"

        + random.choice(MATCH_TEXT)

        + "\n\n"

        + car_text(car),

        parse_mode="HTML"

    )



# =========================
# PROFILE
# =========================


async def profile_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = get_player(

        update.effective_user.id

    )


    await update.message.reply_text(

        profile_text(user),

        parse_mode="HTML"

    )



# =========================
# БАЛАНС
# =========================


async def balance_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = get_player(

        update.effective_user.id

    )


    await update.message.reply_text(

        f"""

💰 <b>ТВОЙ БАЛАНС</b>


🪙 Монеты: {user['coins']}

⭐ Уровень: {user['level']}

🔥 XP: {user['xp']}

""",

        parse_mode="HTML"

    )



# =========================
# ГАРАЖ
# =========================


async def garage_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = get_player(

        update.effective_user.id

    )


    garage = user["garage"]



    text = (

        "🏆 <b>ТВОЙ ГАРАЖ</b>\n\n"

    )


    if garage:


        for car in garage:

            text += (

                "🏎 "

                + car

                + "\n"

            )


    else:

        text += "Гараж пока пуст 😢"



    await update.message.reply_text(

        text,

        parse_mode="HTML"

    )
    
    # =========================
# КНОПКИ
# =========================


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id



    # =====================
    # МАШИНА ДНЯ
    # =====================

    if query.data == "daily":

        car = get_random_car()


        add_car(

            user_id,

            car["name"]

        )


        await query.message.reply_text(

            "🔥 <b>МАШИНА ДНЯ</b>\n\n"

            + car_text(car),

            parse_mode="HTML"

        )

        return



    # =====================
    # MATCH
    # =====================

    if query.data == "match":

        car = get_random_car()


        add_car(

            user_id,

            car["name"]

        )


        await query.message.reply_text(

            "🎲 <b>ТВОЯ МАШИНА</b>\n\n"

            + random.choice(MATCH_TEXT)

            + "\n\n"

            + car_text(car),

            parse_mode="HTML"

        )

        return



    # =====================
    # ПРОФИЛЬ
    # =====================

    if query.data == "profile":

        user = get_player(
            user_id
        )


        await query.message.reply_text(

            profile_text(user),

            parse_mode="HTML"

        )

        return



    # =====================
    # ГАРАЖ
    # =====================

    if query.data == "garage":

        user = get_player(
            user_id
        )


        text = (

            "🏆 <b>ТВОЙ ГАРАЖ</b>\n\n"

        )


        if user["garage"]:

            for car in user["garage"]:

                text += (

                    "🏎 "

                    + car

                    + "\n"

                )

        else:

            text += "Гараж пуст"



        await query.message.reply_text(

            text,

            parse_mode="HTML"

        )

        return



    # =====================
    # КЕЙС
    # =====================

    if query.data == "case":

        try:

            from shop import open_case


            car = open_case(
                user_id
            )


            await query.message.reply_text(

                "🎁 <b>ТЫ ОТКРЫЛ LEGEND CASE!</b>\n\n"

                "🔥 Тебе выпала:\n\n"

                + car_text(car),

                parse_mode="HTML"

            )


        except Exception as e:

            logging.error(e)


            await query.message.reply_text(

                "❌ Ошибка открытия кейса"

            )


        return



    # =====================
    # МАГАЗИН
    # =====================

    if query.data == "shop":

        await query.message.reply_text(

            """

🛒 <b>МАГАЗИН CAR LEGENDS</b>


🎁 LEGEND CASE

Открывай кейсы и получай машины!


💰 Баланс смотри через:
 /balance


""",

            parse_mode="HTML"

        )

        return



    # =====================
    # НАЗАД В МЕНЮ
    # =====================

    if query.data == "menu":

        await query.message.reply_text(

            "Главное меню 👇",

            reply_markup=main_menu()

        )

        return
        
        # =========================
# АВТОПОСТ
# =========================


async def daily_post(
    context: ContextTypes.DEFAULT_TYPE
):

    car = get_random_car()


    await context.bot.send_message(

        chat_id=CHANNEL,

        text=(

            "🔥 <b>МАШИНА ДНЯ</b>\n\n"

            + car_text(car)

        ),

        parse_mode="HTML"

    )



# =========================
# ОШИБКИ
# =========================


async def error_handler(
    update,
    context
):

    logging.error(

        "Ошибка бота",

        exc_info=context.error

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


    app.add_handler(

        CommandHandler(
            "balance",
            balance_command
        )

    )


    app.add_handler(

        CommandHandler(
            "garage",
            garage_command
        )

    )



    # Кнопки

    app.add_handler(

        CallbackQueryHandler(
            button_handler
        )

    )



    # Ошибки

    app.add_error_handler(

        error_handler

    )



    # Автопост каждый день

    app.job_queue.run_daily(

        daily_post,

        time=time(
            12,
            0
        )

    )



    print(
        "🏎 CAR LEGENDS CLUB 6.0 запущен!"
    )


    app.run_polling()



if __name__ == "__main__":

    main()