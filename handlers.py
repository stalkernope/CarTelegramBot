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
    clan_menu
)


from game_core import profile_text



# =========================
# START
# =========================


async def start(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    user = update.effective_user



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




    # ПРОФИЛЬ

    if action == "profile":


        await query.edit_message_text(

            profile_text(user_id),

            reply_markup=

            profile_menu(),

            parse_mode="HTML"

        )




    # ГАРАЖ

    elif action == "garage":


        await query.edit_message_text(

            "🚗 <b>ГАРАЖ</b>\n\n"

            "Выбери действие:",

            reply_markup=

            garage_menu(),

            parse_mode="HTML"

        )




    # ГОНКИ

    elif action == "race":


        await query.edit_message_text(

            "🏁 <b>ГОНКИ</b>\n\n"

            "Выбери режим:",

            reply_markup=

            race_menu(),

            parse_mode="HTML"

        )




    # КЛАН

    elif action == "clan":


        await query.edit_message_text(

            "⚔️ <b>КЛАН</b>",

            reply_markup=

            clan_menu(),

            parse_mode="HTML"

        )




    # НАЗАД

    elif action == "back":


        await query.edit_message_text(

            "🏎 Главное меню",

            reply_markup=

            main_menu()

        )




    # В РАЗРАБОТКЕ

    else:


        await query.edit_message_text(

            "🔥 Раздел подключается..."

        )




# =========================
# РЕГИСТРАЦИЯ
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