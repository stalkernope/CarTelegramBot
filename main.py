import os
import logging
import random

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



from keyboards import main_menu


from database import (
    get_player,
    add_car
)


from car_database import (
    get_random_car
)


from profiles import (
    profile_text
)


from shop import (
    open_case
)


from battles import (
    start_battle,
    fight,
    battle_text
)


from images import (
    get_car_image
)



logging.basicConfig(
    level=logging.INFO
)



TOKEN = os.environ["BOT_TOKEN"]



CHANNEL = "@toway2m"





# =========================
# ТЕКСТ МАШИНЫ
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

        f"💎 Редкость: {car.get('rarity','')}\n\n"

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

        "🏎 <b>CAR LEGENDS CLUB</b>\n\n"

        "Добро пожаловать в мир легендарных автомобилей 🔥\n\n"

        "🚗 Коллекция машин\n"

        "⚔️ Битвы легенд\n"

        "🎁 Кейсы\n"

        "🏆 Гараж\n\n"

        "Выбирай раздел 👇",

        parse_mode="HTML",

        reply_markup=main_menu()

    )
    
    # =========================
# КОМАНДА МАШИНА
# =========================


async def car_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    car = get_random_car()


    if not car:

        await update.message.reply_text(
            "❌ База машин пустая"
        )

        return



    add_car(

        user.id,

        car["name"]

    )


    photo = get_car_image(
        car
    )


    if photo:

        await update.message.reply_photo(

            photo=photo,

            caption=car_text(car),

            parse_mode="HTML"

        )

    else:

        await update.message.reply_text(

            car_text(car),

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

        "🎲 <b>ТВОЯ МАШИНА</b>\n\n"

        "🔥 Тебе подходит эта легенда:\n\n"

        + car_text(car),

        parse_mode="HTML"

    )





# =========================
# ПРОФИЛЬ
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
# ГАРАЖ
# =========================


async def garage_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = get_player(

        update.effective_user.id

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

        text += "Гараж пока пуст"



    await update.message.reply_text(

        text,

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
💰 <b>БАЛАНС</b>

🪙 Монеты: {user['coins']}

⭐ Уровень: {user['level']}

🔥 XP: {user['xp']}
""",

        parse_mode="HTML"

    )
    
    # =========================
# КНОПКИ МЕНЮ
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


        photo = get_car_image(
            car
        )


        if photo:


            await query.message.reply_photo(

                photo=photo,

                caption=(

                    "🔥 <b>МАШИНА ДНЯ</b>\n\n"

                    + car_text(car)

                ),

                parse_mode="HTML"

            )


        else:


            await query.message.reply_text(

                "🔥 <b>МАШИНА ДНЯ</b>\n\n"

                + car_text(car),

                parse_mode="HTML"

            )


        return




    # =====================
    # МОЯ МАШИНА
    # =====================


    if query.data == "match":


        car = get_random_car()


        add_car(

            user_id,

            car["name"]

        )


        await query.message.reply_text(

            "🎲 <b>ТЕБЕ ПОДХОДИТ</b>\n\n"

            + car_text(car),

            parse_mode="HTML"

        )


        return





    # =====================
    # КЕЙС
    # =====================


    if query.data == "case":


        try:


            car = open_case(

                user_id

            )


            await query.message.reply_text(

                "🎁 <b>ОТКРЫТ КЕЙС</b>\n\n"

                + car_text(car),

                parse_mode="HTML"

            )


        except Exception as e:


            await query.message.reply_text(

                f"❌ {e}"

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

            "🏆 <b>ГАРАЖ</b>\n\n"

        )


        if user["garage"]:


            for car in user["garage"]:

                text += (

                    "🏎 "

                    + car

                    + "\n"

                )


        else:

            text += "Пусто"



        await query.message.reply_text(

            text,

            parse_mode="HTML"

        )


        return
        
            # =====================
    # БИТВА МАШИН
    # =====================


    if query.data == "battle":


        car1, car2 = start_battle()


        keyboard = [

            [

                InlineKeyboardButton(

                    car1["name"],

                    callback_data=f"battle_win:{car1['name']}"

                )

            ],

            [

                InlineKeyboardButton(

                    car2["name"],

                    callback_data=f"battle_win:{car2['name']}"

                )

            ]

        ]


        await query.message.reply_text(

            battle_text(

                car1,

                car2

            ),

            parse_mode="HTML",

            reply_markup=InlineKeyboardMarkup(

                keyboard

            )

        )


        return





    # =====================
    # ГОЛОС ЗА БИТВУ
    # =====================


    if query.data.startswith("battle_win:"):


        winner = query.data.replace(

            "battle_win:",

            ""

        )


        await query.message.reply_text(

            "🏆 Победитель выбран:\n\n"

            + winner

            + "\n\n🔥 Спасибо за голос!"

        )


        return





# =========================
# ОШИБКИ
# =========================


async def error_handler(
    update,
    context
):

    logging.error(

        "Ошибка:",

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

            "garage",

            garage_command

        )

    )


    app.add_handler(

        CommandHandler(

            "balance",

            balance_command

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



    print(

        "🏎 CAR LEGENDS CLUB запущен!"

    )


    app.run_polling()





if __name__ == "__main__":

    main()