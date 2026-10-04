import logging
from datetime import time

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from config import TOKEN, CHANNEL

from keyboards import main_menu

from database import (
    create_files,
    get_user,
    add_xp,
    add_car
)

from cars import (
    random_car,
    format_car
)

from profiles import profile_text

from daily import daily_car_text

from battles import (
    create_battle,
    battle_text
)


logging.basicConfig(
    level=logging.INFO
)



# ==========================
# START
# ==========================

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    get_user(user.id)

    text = (
        "🏎 <b>CAR LEGENDS CLUB</b>\n\n"
        "Добро пожаловать в автомобильный клуб.\n\n"
        "🔥 Машины дня\n"
        "⚔️ Битвы легенд\n"
        "🎲 Подбор автомобиля\n"
        "🏆 Личный гараж\n"
        "👤 Профиль коллекционера\n\n"
        "Пристегнись. Путешествие начинается 🚀"
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=main_menu()
    )



# ==========================
# COMMAND CAR
# ==========================

async def car_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    car = random_car()

    add_car(
        user.id,
        car["name"]
    )

    add_xp(
        user.id,
        50
    )

    await update.message.reply_text(
        format_car(car),
        parse_mode="HTML"
    )



# ==========================
# PROFILE
# ==========================

async def profile_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):

    text = profile_text(
        update.effective_user.id
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )



# ==========================
# BATTLE
# ==========================

async def battle_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):

    cars = create_battle()

    await update.message.reply_text(
        battle_text(
            cars[0],
            cars[1]
        ),
        parse_mode="HTML"
    )



# ==========================
# BUTTONS
# ==========================

async def button_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    if query.data == "match":

        car = random_car()

        add_car(
            user_id,
            car["name"]
        )

        add_xp(
            user_id,
            50
        )


        await query.message.reply_text(
            "🎲 Твой автомобиль:\n\n"
            + format_car(car),
            parse_mode="HTML"
        )



    elif query.data == "profile":

        await query.message.reply_text(
            profile_text(user_id),
            parse_mode="HTML"
        )



    elif query.data == "garage":

        user = get_user(user_id)

        cars = user.get(
            "cars",
            []
        )

        if cars:

            text = (
                "🏆 <b>Твой гараж:</b>\n\n"
            )

            for car in cars:
                text += f"🏎 {car}\n"

        else:

            text = (
                "🏆 Гараж пуст.\n"
                "Получи первую машину 🎲"
            )


        await query.message.reply_text(
            text,
            parse_mode="HTML"
        )



    elif query.data == "daily":

        text, car = daily_car_text()

        await query.message.reply_text(
            text,
            parse_mode="HTML"
        )



    elif query.data == "battle":

        cars = create_battle()

        await query.message.reply_text(
            battle_text(
                cars[0],
                cars[1]
            ),
            parse_mode="HTML"
        )



    elif query.data == "catalog":

        car = random_car()

        await query.message.reply_text(
            format_car(car),
            parse_mode="HTML"
        )



    elif query.data == "street":

        await query.message.reply_text(
            "📸 STREET SPOT\n\n"
            "Скоро здесь будут лучшие машины с улиц 🔥",
            parse_mode="HTML"
        )



# ==========================
# CHANNEL POSTS
# ==========================

async def daily_post(ctx: ContextTypes.DEFAULT_TYPE):

    text, car = daily_car_text()

    await ctx.bot.send_message(
        CHANNEL,
        text,
        parse_mode="HTML"
    )



async def battle_post(ctx: ContextTypes.DEFAULT_TYPE):

    cars = create_battle()

    await ctx.bot.send_message(
        CHANNEL,
        battle_text(
            cars[0],
            cars[1]
        ),
        parse_mode="HTML"
    )



# ==========================
# MAIN
# ==========================

def main():

    create_files()


    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )


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


    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    # Ежедневные публикации

    app.job_queue.run_daily(
        daily_post,
        time=time(12, 0)
    )


    app.job_queue.run_daily(
        battle_post,
        time=time(19, 0)
    )


    print(
        "🏎 Car Legends Club 3.0 started!"
    )


    app.run_polling()



if __name__ == "__main__":
    main()