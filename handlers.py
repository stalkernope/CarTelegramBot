from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)


from menu_system import (
    main_menu,
    garage_menu,
    race_menu,
    profile_menu,
    clan_menu,
    cases_menu
)


from game_core import profile_text


from database import (
    get_player,
    update_player
)


from car_database import get_all_cars


from case_system import (
    cases_text,
    buy_and_open_case
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

        f"🏎 Добро пожаловать, {user.first_name}!\n\n"

        "🔥 CAR LEGENDS\n"

        "Твой путь начинается!",


        reply_markup=

        main_menu(),

        parse_mode="HTML"

    )




# =========================
# КНОПКИ
# =========================


async def buttons(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    query = update.callback_query


    await query.answer()


    user_id = query.from_user.id


    action = query.data




    if action == "profile":


        await query.edit_message_text(

            profile_text(user_id),

            reply_markup=

            profile_menu(),

            parse_mode="HTML"

        )




    elif action == "garage":


        await query.edit_message_text(

            "🚗 <b>ГАРАЖ</b>\n\n"

            "Твой автопарк готов",

            reply_markup=

            garage_menu(),

            parse_mode="HTML"

        )




    elif action == "race":


        await query.edit_message_text(

            "🏁 <b>ГОНКИ</b>\n\n"

            "Выбери режим",

            reply_markup=

            race_menu(),

            parse_mode="HTML"

        )




    elif action == "clan":


        await query.edit_message_text(

            "⚔️ <b>КЛАНЫ</b>",

            reply_markup=

            clan_menu(),

            parse_mode="HTML"

        )




    elif action == "cases":


        await query.edit_message_text(

            cases_text(),

            reply_markup=

            cases_menu(),

            parse_mode="HTML"

        )




    elif action == "open_normal_case":


        player = get_player(

            user_id

        )


        result = buy_and_open_case(

            user_id,

            player,

            "normal",

            get_all_cars()

        )


        if result["success"]:


            update_player(

                user_id,

                player

            )


            text = result["message"]


        else:


            text = result["message"]



        await query.edit_message_text(

            text,

            reply_markup=

            main_menu(),

            parse_mode="HTML"

        )




    elif action == "back":


        await query.edit_message_text(

            "🏎 Главное меню",

            reply_markup=

            main_menu()

        )




    else:


        await query.edit_message_text(

            "🔥 Раздел скоро будет доступен",

            reply_markup=

            main_menu()

        )




# =========================
# ПОДКЛЮЧЕНИЕ
# =========================


def setup_handlers(app):


    app.add_handler(

        CommandHandler(

            "start",

            start

        )

    )


    app.add_handler(

        CallbackQueryHandler(

            buttons

        )

    )