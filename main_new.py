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
    get_random_car,
    get_car
)

from database import (
    get_user,
    add_car_to_garage
)

from profiles import profile_text

from images import (
    get_car_image,
    photo_caption
)


from economy import (
    add_coins,
    get_balance
)


logging.basicConfig(
    level=logging.INFO
)


TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = "@toway2m"



# ==========================
# START
# ==========================


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    get_user(
        user.id
    )


    await update.message.reply_text(

        """
🏎 <b>CAR LEGENDS CLUB</b>

Добро пожаловать в клуб легендарных автомобилей 🔥

Тебя ждут:

🏁 Тысячи автомобилей
⚔️ Битвы легенд
🎲 Подбор машины
🏆 Коллекция
💰 Экономика

Выбирай раздел 👇
""",

        parse_mode="HTML",

        reply_markup=main_menu()

    )
    
    # ==========================
# МАШИНА ДНЯ
# ==========================


async def car_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    car = get_random_car()


    add_car_to_garage(
        user.id,
        car["name"]
    )


    image = get_car_image(
        car
    )


    await update.message.reply_photo(

        photo=image,

        caption=photo_caption(car),

        parse_mode="HTML"

    )



# ==========================
# MATCH
# ==========================


MATCH_PHRASES = [

    "🔥 Ты создан для скорости и эмоций",

    "👑 Тебе нужна машина, которая выделяет тебя из толпы",

    "💎 Твой стиль — редкость и эксклюзив",

    "🏁 Ты выбираешь характер, а не просто автомобиль",

    "🌙 Твой гараж должен быть наполнен легендами"

]



async def match_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    car = get_random_car()


    add_car_to_garage(
        user.id,
        car["name"]
    )


    image = get_car_image(
        car
    )


    text = (

        "🎲 <b>ТВОЯ МАШИНА ПО ХАРАКТЕРУ</b>\n\n"

        + random.choice(MATCH_PHRASES)

        + "\n\n"

        + photo_caption(car)

    )


    await update.message.reply_photo(

        photo=image,

        caption=text,

        parse_mode="HTML"

    )



# ==========================
# ПРОФИЛЬ
# ==========================


async def profile_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = get_user(
        update.effective_user.id
    )


    await update.message.reply_text(

        profile_text(user),

        parse_mode="HTML"

    )



# ==========================
# БАЛАНС
# ==========================


async def balance_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    coins = get_balance(
        update.effective_user.id
    )


    await update.message.reply_text(

        f"""
💰 <b>ТВОЙ БАЛАНС</b>

Монеты: {coins} 🪙
""",

        parse_mode="HTML"

    )
    
    # ==========================
# ОБРАБОТКА КНОПОК
# ==========================


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id



    # ======================
    # МАШИНА ДНЯ
    # ======================

    if query.data == "daily":

        car = get_random_car()


        add_car_to_garage(
            user_id,
            car["name"]
        )


        await query.message.reply_photo(

            photo=get_car_image(car),

            caption=(
                "🔥 <b>МАШИНА ДНЯ</b>\n\n"
                + photo_caption(car)
            ),

            parse_mode="HTML"

        )

        return



    # ======================
    # MATCH
    # ======================

    if query.data == "match":

        car = get_random_car()


        add_car_to_garage(
            user_id,
            car["name"]
        )


        await query.message.reply_photo(

            photo=get_car_image(car),

            caption=(

                "🎲 <b>ТЕБЕ ПОДХОДИТ:</b>\n\n"

                + random.choice(MATCH_PHRASES)

                + "\n\n"

                + photo_caption(car)

            ),

            parse_mode="HTML"

        )

        return



    # ======================
    # ПРОФИЛЬ
    # ======================

    if query.data == "profile":

        user = get_user(
            user_id
        )


        await query.message.reply_text(

            profile_text(user),

            parse_mode="HTML"

        )

        return



    # ======================
    # ГАРАЖ
    # ======================

    if query.data == "garage":

        user = get_user(
            user_id
        )


        garage = user.get(
            "garage",
            []
        )


        if garage:


            text = (
                "🏆 <b>ТВОЙ ГАРАЖ</b>\n\n"
            )


            for car in garage:

                text += (
                    "🏎 "
                    + car
                    + "\n"
                )


        else:

            text = (
                "🏆 <b>ТВОЙ ГАРАЖ</b>\n\n"
                "Пока пусто 😢\n"
                "Получи первую машину!"
            )


        await query.message.reply_text(

            text,

            parse_mode="HTML"

        )

        return



    # ======================
    # БИТВА
    # ======================

    if query.data == "battle":

        from battles import create_battle_text


        battle = create_battle_text()


        await query.message.reply_text(

            battle,

            parse_mode="HTML"

        )

        return
        
        # ==========================
# АВТОПОСТЫ
# ==========================


async def daily_post(
    context: ContextTypes.DEFAULT_TYPE
):

    car = get_random_car()


    await context.bot.send_photo(

        chat_id=CHANNEL,

        photo=get_car_image(car),

        caption=(

            "🔥 <b>ЭКСКЛЮЗИВ ДНЯ</b>\n\n"

            + photo_caption(car)

        ),

        parse_mode="HTML"

    )



# ==========================
# ОШИБКИ
# ==========================


async def error_handler(
    update,
    context
):

    logging.error(

        "Ошибка: ",

        exc_info=context.error

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


    app.add_handler(

        CommandHandler(
            "balance",
            balance_command
        )

    )



    # кнопки

    app.add_handler(

        CallbackQueryHandler(
            button_handler
        )

    )



    # ошибки

    app.add_error_handler(

        error_handler

    )



    # каждый день машина

    app.job_queue.run_daily(

        daily_post,

        time=time(
            12,
            0
        )

    )


    print(
        "🏎 CAR LEGENDS CLUB запущен!"
    )


    app.run_polling()



if __name__ == "__main__":

    main()
    