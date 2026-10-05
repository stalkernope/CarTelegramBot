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


from car_database import (
    get_all_cars,
    get_car
)


from case_system import (
    cases_text,
    buy_and_open_case
)


from garage_system import (
    garage_text,
    get_garage_cars
)


from battle_system import (
    battle,
    battle_result_text,
    reward_win,
    reward_loss
)


from boss_race_system import (
    get_boss,
    fight_boss
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


        reply_markup=main_menu(),

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

            reply_markup=profile_menu(),

            parse_mode="HTML"

        )




    # ГАРАЖ

    elif action == "garage":


        await query.edit_message_text(

            garage_text(user_id),

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )




    # ГОНКИ

    elif action == "race":


        await query.edit_message_text(

            "🏁 <b>ГОНКИ</b>\n\n"

            "Выбирай соперника:",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # NPC БОЙ

    elif action == "npc":


        player = get_player(

            user_id

        )


        if not player.get("main_car"):


            await query.edit_message_text(

                "❌ Сначала выбери главную машину",

                reply_markup=main_menu()

            )

            return



        player_car = get_car(

            player["main_car"]

        )


        cars = get_all_cars()


        enemy = None



        for car in cars:

            if car["name"] != player_car["name"]:

                enemy = car

                break



        if not enemy:


            await query.edit_message_text(

                "❌ Нет соперников"

            )

            return




        result = battle(

            player_car,

            enemy

        )


        if result["winner"]["name"] == player_car["name"]:


            reward = reward_win(

                user_id

            )


            text = (

                battle_result_text(result)

                +

                "\n\n🏆 ПОБЕДА!"

                +

                f"\n💰 +{reward['coins']}"

            )


        else:


            reward_loss(

                user_id

            )


            text = (

                battle_result_text(result)

                +

                "\n\n❌ ПОРАЖЕНИЕ"

            )



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )




    # БОСС

    elif action == "boss":


        player = get_player(

            user_id

        )


        if not player.get("main_car"):


            await query.edit_message_text(

                "❌ Нет главной машины"

            )

            return



        car = get_car(

            player["main_car"]

        )


        boss = get_boss()



        result = fight_boss(

            user_id,

            car.get("power",0),

            boss["id"]

        )



        if result["win"]:


            text = (

                "👑 <b>БОСС ПОБЕЖДЕН!</b>\n\n"

                f"{result['boss']}\n\n"

                f"🎁 Награда:\n"

                f"{result['reward']}"

            )


        else:


            text = (

                "❌ <b>ПОРАЖЕНИЕ</b>\n\n"

                f"Босс: {result['boss']}"

            )



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )




    # КЕЙСЫ

    elif action == "cases":


        await query.edit_message_text(

            cases_text(),

            reply_markup=cases_menu(),

            parse_mode="HTML"

        )




    # ОТКРЫТИЕ КЕЙСА

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


        await query.edit_message_text(

            result["message"],

            reply_markup=main_menu(),

            parse_mode="HTML"

        )




    # КЛАН

    elif action == "clan":


        await query.edit_message_text(

            "⚔️ <b>КЛАНЫ</b>",

            reply_markup=clan_menu(),

            parse_mode="HTML"

        )




    # НАЗАД

    elif action == "back":


        await query.edit_message_text(

            "🏎 Главное меню",

            reply_markup=main_menu()

        )




    else:


        await query.edit_message_text(

            "🔥 Раздел в разработке",

            reply_markup=main_menu()

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