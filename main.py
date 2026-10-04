import os
import logging


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
    add_car,
    add_win,
    add_loss
)


from car_database import (
    get_random_car,
    get_car
)


from daily_car import (
    get_daily_car
)


from shop import (
    open_case
)


from shop_cars import (
    get_shop_cars,
    buy_car
)


from battles import (
    start_battle,
    battle_text,
    fight,
    player_win,
    player_loss
)


from profiles import (
    profile_text
)



# =========================
# ЛОГИ
# =========================


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)



TOKEN = os.environ.get(
    "BOT_TOKEN"
)



# =========================
# ТЕКСТ МАШИНЫ
# =========================


def car_text(car):

    if not car:

        return "❌ Машина не найдена"


    return (

        f"🏎 <b>{car.get('name')}</b>\n\n"

        f"🏭 Бренд: {car.get('brand','')}\n"

        f"🌍 Страна: {car.get('country','')}\n"

        f"📅 Год: {car.get('year','')}\n\n"

        f"⚡ Мощность: {car.get('power',0)} л.с.\n"

        f"🚀 Скорость: {car.get('speed',0)} км/ч\n"

        f"💰 Цена: {car.get('price',0)}$\n"

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

    user_id = update.effective_user.id


    get_player(
        user_id
    )


    await update.message.reply_text(

        "🏎 <b>CAR LEGENDS CLUB</b>\n\n"

        "🔥 Добро пожаловать в мир легендарных машин!\n\n"

        "🚗 Собирай коллекцию\n"

        "⚔️ Участвуй в битвах\n"

        "🎁 Открывай кейсы\n"

        "🛒 Покупай редкие автомобили\n\n"

        "Выбирай раздел 👇",

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

    user_id = update.effective_user.id


    car = get_random_car()


    if not car:

        await update.message.reply_text(
            "❌ База машин пуста"
        )

        return


    add_car(
        user_id,
        car["name"]
    )


    await update.message.reply_text(

        car_text(car),

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

        text += "Гараж пуст"



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

💰 <b>CAR LEGENDS</b>

🪙 Монеты: {user['coins']}
⭐ Уровень: {user['level']}
🔥 XP: {user['xp']}

🏎 Машин: {len(user['garage'])}

⚔️ Победы: {user['wins']}
❌ Поражения: {user['losses']}

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


    try:

        await query.answer()


        user_id = query.from_user.id


        logging.info(
            f"Кнопка: {query.data} | USER: {user_id}"
        )



        # =====================
        # МАШИНА ДНЯ
        # =====================

        if query.data == "daily":


            car = get_daily_car()


            if not car:

                await query.message.reply_text(
                    "❌ Машина дня не найдена"
                )

                return



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


            if not car:

                await query.message.reply_text(
                    "❌ Нет машин"
                )

                return



            add_car(

                user_id,

                car["name"]

            )


            await query.message.reply_text(

                "🎲 <b>ТВОЯ МАШИНА</b>\n\n"

                + car_text(car),

                parse_mode="HTML"

            )


            return




        # =====================
        # КЕЙС
        # =====================

        if query.data == "case":


            car = open_case(
                user_id
            )


            await query.message.reply_text(

                "🎁 <b>КЕЙС ОТКРЫТ!</b>\n\n"

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
        # МАГАЗИН
        # =====================

        if query.data == "shop":


            cars = get_shop_cars()


            if not cars:


                await query.message.reply_text(

                    "❌ Магазин пуст"

                )

                return



            keyboard = []


            text = (

                "🛒 <b>CAR LEGENDS SHOP</b>\n\n"

            )



            for car in cars:


                text += (

                    f"🏎 <b>{car['name']}</b>\n"

                    f"💎 {car['rarity']}\n"

                    f"💰 {car['price']}$\n\n"

                )


                keyboard.append(

                    [

                        InlineKeyboardButton(

                            "Купить",

                            callback_data=

                            "buy:" + car["name"]

                        )

                    ]

                )



            await query.message.reply_text(

                text,

                parse_mode="HTML",

                reply_markup=

                InlineKeyboardMarkup(

                    keyboard

                )

            )


            return




        # =====================
        # ПОКУПКА
        # =====================

        if query.data.startswith("buy:"):


            car_name = query.data.replace(

                "buy:",

                ""

            )


            car = buy_car(

                user_id,

                car_name

            )


            await query.message.reply_text(

                "✅ <b>МАШИНА КУПЛЕНА</b>\n\n"

                + car_text(car),

                parse_mode="HTML"

            )


            return




        # =====================
        # БИТВА
        # =====================

        if query.data == "battle":


            car1, car2 = start_battle()


            if not car1 or not car2:


                await query.message.reply_text(

                    "❌ Недостаточно машин для битвы"

                )

                return



            keyboard = [

                [

                    InlineKeyboardButton(

                        car1["name"],

                        callback_data=

                        "battle:" + car1["name"]

                    )

                ],

                [

                    InlineKeyboardButton(

                        car2["name"],

                        callback_data=

                        "battle:" + car2["name"]

                    )

                ]

            ]



            await query.message.reply_text(

                battle_text(

                    car1,

                    car2

                ),

                parse_mode="HTML",

                reply_markup=

                InlineKeyboardMarkup(

                    keyboard

                )

            )


            context.user_data["battle"] = [

                car1,

                car2

            ]


            return




        # =====================
        # ВЫБОР БИТВЫ
        # =====================

        if query.data.startswith("battle:"):


            choice = query.data.replace(

                "battle:",

                ""

            )


            battle = context.user_data.get(
                "battle"
            )


            if not battle:

                await query.message.reply_text(

                    "❌ Битва устарела"

                )

                return



            car1, car2 = battle



            winner, loser = fight(

                car1,

                car2

            )



            if choice == winner["name"]:


                player_win(
                    user_id
                )


                result = "🏆 Ты угадал победителя!"

            else:


                player_loss(
                    user_id
                )


                result = "❌ Ты проиграл!"



            await query.message.reply_text(

                result

                +

                "\n\n🏎 Победитель:\n"

                +

                winner["name"]

            )


            return



    except Exception as e:


        logging.error(

            "Ошибка кнопки",

            exc_info=True

        )


        await query.message.reply_text(

            "❌ Ошибка:\n"

            + str(e)

        )
        # =========================
# ОШИБКИ
# =========================


async def error_handler(
    update,
    context
):

    logging.error(

        "Глобальная ошибка бота",

        exc_info=context.error

    )



# =========================
# ЗАПУСК
# =========================


def main():


    if not TOKEN:

        print(
            "❌ BOT_TOKEN не найден"
        )

        return



    app = (

        Application

        .builder()

        .token(TOKEN)

        .build()

    )



    # =====================
    # КОМАНДЫ
    # =====================


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



    # =====================
    # КНОПКИ
    # =====================


    app.add_handler(

        CallbackQueryHandler(

            button_handler

        )

    )



    # =====================
    # ОШИБКИ
    # =====================


    app.add_error_handler(

        error_handler

    )



    print(

        "🏎 CAR LEGENDS CLUB запущен!"

    )



    app.run_polling()



# =========================
# START
# =========================


if __name__ == "__main__":

    main()