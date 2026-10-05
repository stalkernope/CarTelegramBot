import os
import logging


from server import keep_alive


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
# KEEP ALIVE RENDER
# =========================


keep_alive()



# =========================
# ТЕКСТ МАШИНЫ
# =========================


def car_text(car):

    if not car:

        return "❌ Машина не найдена"



    return (

        f"🏎 <b>{car.get('name','')}</b>\n\n"

        f"🏭 Бренд: {car.get('brand','')}\n"

        f"🌍 Страна: {car.get('country','')}\n"

        f"📅 Год: {car.get('year','')}\n\n"

        f"⚡ Мощность: {car.get('power',0)} л.с.\n"

        f"🚀 Скорость: {car.get('speed',0)} км/ч\n"

        f"💰 Цена: {car.get('price',0)}$\n"

        f"💎 Редкость: {car.get('rarity','')}\n\n"

        f"📝 {car.get('description','')}"

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

        "🔥 Добро пожаловать!\n\n"

        "🚗 Собирай легендарные машины\n"

        "⚔️ Участвуй в битвах\n"

        "🎁 Открывай кейсы\n"

        "🛒 Покупай автомобили\n\n"

        "Выбирай действие 👇",

        parse_mode="HTML",

        reply_markup=main_menu()

    )



# =========================
# /car
# =========================


async def car_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    user_id = update.effective_user.id


    car = get_random_car()



    if not car:


        await update.message.reply_text(

            "❌ Нет машин в базе"

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
# КНОПКИ
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
            f"BUTTON {query.data} USER {user_id}"
        )



        # =====================
        # НАЗАД
        # =====================


        if query.data == "menu":


            await query.message.reply_text(

                "🏎 Главное меню",

                reply_markup=main_menu()

            )


            return




        # =====================
        # МАШИНА ДНЯ
        # =====================


        if query.data == "daily":


            car = get_daily_car()



            if not car:


                await query.message.reply_text(

                    "❌ Машина дня недоступна"

                )

                return



            await query.message.reply_text(

                "🔥 <b>МАШИНА ДНЯ</b>\n\n"

                + car_text(car),

                parse_mode="HTML"

            )


            return




        # =====================
        # СЛУЧАЙНАЯ МАШИНА
        # =====================


        if query.data == "match":


            car = get_random_car()



            if not car:


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


            try:


                car = open_case(

                    user_id

                )


                await query.message.reply_text(

                    "🎁 <b>КЕЙС ОТКРЫТ</b>\n\n"

                    + car_text(car),

                    parse_mode="HTML"

                )



            except Exception as e:


                await query.message.reply_text(

                    "❌ "

                    + str(e)

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



            keyboard.append(

                [

                    InlineKeyboardButton(

                        "⬅️ Назад",

                        callback_data="menu"

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



            try:


                car = buy_car(

                    user_id,

                    car_name

                )



                await query.message.reply_text(

                    "✅ <b>МАШИНА КУПЛЕНА</b>\n\n"

                    + car_text(car),

                    parse_mode="HTML"

                )



            except Exception as e:


                await query.message.reply_text(

                    "❌ "

                    + str(e)

                )



            return




        # =====================
        # БИТВА
        # =====================


        if query.data == "battle":


            car1, car2 = start_battle()



            if not car1 or not car2:


                await query.message.reply_text(

                    "❌ Недостаточно машин"

                )

                return



            context.user_data["battle"] = [

                car1,

                car2

            ]



            keyboard = [


                [

                    InlineKeyboardButton(

                        car1["name"],

                        callback_data="fight_1"

                    )

                ],


                [

                    InlineKeyboardButton(

                        car2["name"],

                        callback_data="fight_2"

                    )

                ],


                [

                    InlineKeyboardButton(

                        "⬅️ Назад",

                        callback_data="menu"

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


            return




        # =====================
        # ВЫБОР БИТВЫ
        # =====================


        if query.data in [

            "fight_1",

            "fight_2"

        ]:


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



            chosen = (


                car1

                if query.data == "fight_1"

                else car2

            )



            if chosen["name"] == winner["name"]:


                player_win(

                    user_id

                )


                result = (

                    "🏆 Ты выбрал победителя!"

                )


            else:


                player_loss(

                    user_id

                )


                result = (

                    "❌ Неверный выбор!"

                )



            await query.message.reply_text(

                result

                +

                "\n\n🏎 Победитель:\n"

                +

                winner["name"]

            )


            return




    except Exception as e:


        logging.exception(

            "Ошибка кнопки"

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

    logging.exception(

        "Ошибка приложения",

        exc_info=context.error

    )





# =========================
# ЗАПУСК
# =========================


def main():


    if not TOKEN:


        print(

            "❌ BOT_TOKEN отсутствует"

        )

        return



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

        CallbackQueryHandler(

            button_handler

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


    try:

        main()


    except Exception:


        logging.exception(

            "КРИТИЧЕСКАЯ ОШИБКА"

        )