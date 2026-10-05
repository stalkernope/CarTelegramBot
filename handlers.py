from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)


from menu_system import (
    main_menu,
    garage_menu,
    garage_cars_menu,
    race_menu,
    profile_menu,
    clan_menu,
    cases_menu,
    shop_menu
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
    get_garage_cars,
    set_main_car
)


from car_shop_system import (
    shop_text,
    buy_shop_car
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
# НАГРАДЫ
# =========================


def rewards_text(reward):

    text = ""


    if reward.get("missions"):


        text += "\n\n🎯 <b>МИССИИ:</b>\n"


        for mission in reward["missions"]:

            text += (

                f"✅ {mission['name']}\n"

            )



    if reward.get("achievements"):


        text += "\n\n🏆 <b>ДОСТИЖЕНИЯ:</b>\n"


        for achievement in reward["achievements"]:

            text += (

                f"🏅 {achievement['name']}\n"

            )


    return text




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




    # =====================
    # ПРОФИЛЬ
    # =====================


    if action == "profile":


        await query.edit_message_text(

            profile_text(user_id),

            reply_markup=profile_menu(),

            parse_mode="HTML"

        )




    # =====================
    # ГАРАЖ
    # =====================


    elif action == "garage":


        await query.edit_message_text(

            garage_text(user_id),

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )




    elif action == "garage_select":


        cars = get_garage_cars(

            user_id

        )


        if not cars:


            await query.edit_message_text(

                "❌ Гараж пуст",

                reply_markup=main_menu()

            )

            return



        await query.edit_message_text(

            "👑 Выбери главную машину:",

            reply_markup=garage_cars_menu(cars),

            parse_mode="HTML"

        )




    elif action.startswith("set_main_"):


        car_id = action.replace(

            "set_main_",

            ""

        )


        cars = get_garage_cars(

            user_id

        )


        selected = None



        for car in cars:


            if car.get("id") == car_id:

                selected = car["name"]

                break



        if selected:


            set_main_car(

                user_id,

                selected

            )


            text = (

                "👑 <b>ГЛАВНАЯ МАШИНА</b>\n\n"

                f"🚗 {selected}"

            )


        else:


            text = "❌ Машина не найдена"



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )
        
        
            # =====================
    # ГОНКИ
    # =====================


    elif action == "race":


        await query.edit_message_text(

            "🏁 <b>ГОНКИ</b>\n\n"

            "Выбери режим:",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # =====================
    # АВТОСАЛОН
    # =====================


    elif action == "shop":


        await query.edit_message_text(

            shop_text(),

            reply_markup=shop_menu(),

            parse_mode="HTML"

        )




    # =====================
    # ПОКУПКА МАШИН
    # =====================


    elif action.startswith("buy_"):


        cars = {

            "buy_honda":
            "🚗 Honda Civic",


            "buy_bmw":
            "🏎 BMW M3",


            "buy_supra":
            "🔥 Supra MK5",


            "buy_bugatti":
            "👑 Bugatti X"

        }



        car_name = cars.get(

            action

        )



        if not car_name:


            await query.edit_message_text(

                "❌ Машина не найдена",

                reply_markup=main_menu()

            )

            return



        player = get_player(

            user_id

        )



        result = buy_shop_car(

            user_id,

            player,

            car_name

        )



        if result:


            update_player(

                user_id,

                player

            )


            text = (

                "🛒 <b>ПОКУПКА УСПЕШНА!</b>\n\n"

                f"🚗 {car_name}\n\n"

                f"💰 Осталось: "

                f"{player.get('money',0)}\n\n"

                "✅ Добавлено в гараж"

            )


        else:


            text = (

                "❌ <b>Покупка невозможна</b>\n\n"

                "Причины:\n"

                "• не хватает денег\n"

                "• машина уже есть"

            )



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )




    # =====================
    # NPC
    # =====================


    elif action == "npc":


        player = get_player(

            user_id

        )


        if not player.get("main_car"):


            await query.edit_message_text(

                "❌ У тебя нет главной машины",

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

                "❌ Нет соперников",

                reply_markup=main_menu()

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

                "\n\n🏆 <b>ПОБЕДА!</b>\n"

                +

                f"💰 +{reward['coins']}"

            )


            text += rewards_text(

                reward

            )


        else:


            reward_loss(

                user_id

            )


            text = (

                battle_result_text(result)

                +

                "\n\n❌ <b>ПОРАЖЕНИЕ</b>"

            )



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )
        
        
            # =====================
    # БОСС
    # =====================


    elif action == "boss":


        player = get_player(

            user_id

        )


        if not player.get("main_car"):


            await query.edit_message_text(

                "❌ Сначала выбери главную машину",

                reply_markup=main_menu()

            )

            return



        car = get_car(

            player["main_car"]

        )


        boss = get_boss()



        result = fight_boss(

            user_id,

            car.get(

                "power",

                0

            ),

            boss["id"]

        )



        if result["win"]:


            text = (

                "👑 <b>БОСС ПОБЕЖДЕН!</b>\n\n"

                f"⚔️ {result['boss']}\n\n"

                f"🎁 Награда:\n"

                f"{result['reward']}"

            )


        else:


            text = (

                "❌ <b>ПОРАЖЕНИЕ</b>\n\n"

                f"👑 Босс:\n"

                f"{result['boss']}"

            )



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )




    # =====================
    # КЕЙСЫ
    # =====================


    elif action == "cases":


        await query.edit_message_text(

            cases_text(),

            reply_markup=cases_menu(),

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



        await query.edit_message_text(

            result["message"],

            reply_markup=main_menu(),

            parse_mode="HTML"

        )




    # =====================
    # КЛАН
    # =====================


    elif action == "clan":


        await query.edit_message_text(

            "⚔️ <b>КЛАНЫ</b>\n\n"

            "Раздел в разработке",

            reply_markup=clan_menu(),

            parse_mode="HTML"

        )




    # =====================
    # НАЗАД
    # =====================


    elif action == "back":


        await query.edit_message_text(

            "🏎 Главное меню",

            reply_markup=main_menu()

        )




    else:


        await query.edit_message_text(

            "🔥 Раздел пока недоступен",

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