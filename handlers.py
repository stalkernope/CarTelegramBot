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
    car_card_menu,
    race_menu,
    profile_menu,
    clan_menu,
    cases_menu,
    shop_menu,
    career_menu,
    social_menu
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
    set_main_car,
    car_card_text
)


from car_shop_system import (
    shop_text,
    buy_shop_car
)


from upgrade_system import (
    upgrade_car
)


from pet_system import (
    pets_text
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

        f"🏎 <b>CAR LEGENDS</b>\n\n"

        f"Добро пожаловать, {user.first_name}!\n\n"

        "🚗 Собирай машины\n"

        "🔧 Улучшай характеристики\n"

        "🐾 Собирай питомцев\n"

        "🏁 Побеждай в гонках",

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

            "🚗 <b>ТВОИ МАШИНЫ</b>\n\n"

            "Выбери автомобиль:",

            reply_markup=garage_cars_menu(cars),

            parse_mode="HTML"

        )
            # =====================
    # КАРТОЧКА МАШИНЫ
    # =====================


    elif action.startswith("car_"):


        car_id = action.replace(

            "car_",

            ""

        )


        cars = get_garage_cars(

            user_id

        )


        for car in cars:


            if str(car.get("id")) == car_id:


                await query.edit_message_text(

                    car_card_text(

                        user_id,

                        car

                    ),

                    reply_markup=

                    car_card_menu(car_id),

                    parse_mode="HTML"

                )

                return




    # =====================
    # ПИТОМЦЫ
    # =====================


    elif action == "pets":


        await query.edit_message_text(

            pets_text(user_id),

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )




    # =====================
    # ГЛАВНАЯ МАШИНА
    # =====================


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


            if str(car.get("id")) == car_id:


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
    # УЛУЧШЕНИЕ
    # =====================


    elif action.startswith("upgrade_"):


        car_id = action.replace(

            "upgrade_",

            ""

        )


        cars = get_garage_cars(

            user_id

        )


        car_name = None



        for car in cars:


            if str(car.get("id")) == car_id:


                car_name = car["name"]

                break



        if not car_name:


            await query.edit_message_text(

                "❌ Машина не найдена",

                reply_markup=main_menu()

            )

            return



        player = get_player(

            user_id

        )



        result = upgrade_car(

            user_id,

            player,

            car_name

        )



        if result["success"]:


            update_player(

                user_id,

                player

            )


            text = (

                "🔧 <b>УЛУЧШЕНИЕ</b>\n\n"

                f"🚗 {car_name}\n\n"

                f"⭐ Уровень: {result['level']}/10\n"

                f"⚡ +{result['power']} мощности\n"

                f"🚀 +{result['speed']} скорости"

            )


        else:


            text = result["message"]



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )




    # =====================
    # КАРЬЕРА
    # =====================


    elif action == "career":


        await query.edit_message_text(

            "🏆 <b>КАРЬЕРА</b>\n\n"

            "⭐ Уровень\n"

            "🎁 Награды\n"

            "🎫 Боевой пропуск",

            reply_markup=career_menu(),

            parse_mode="HTML"

        )




    # =====================
    # СОЦИАЛЬНОЕ
    # =====================


    elif action == "social":


        await query.edit_message_text(

            "🌐 <b>СОЦИАЛЬНОЕ</b>\n\n"

            "👥 Друзья\n"

            "🎁 Рефералы\n"

            "🏆 Рейтинг",

            reply_markup=social_menu(),

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

                "🛒 <b>ПОКУПКА УСПЕШНА</b>\n\n"

                f"🚗 {car_name}\n"

                "✅ Машина добавлена"

            )


        else:


            text = (

                "❌ Покупка невозможна"

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

                "❌ Нет главной машины",

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


        car = get_car(

            player.get("main_car")

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

                "👑 <b>БОСС ПОБЕЖДЕН</b>\n\n"

                f"⚔️ {result['boss']}\n\n"

                f"🎁 {result['reward']}"

            )


        else:


            text = (

                "❌ <b>ПОРАЖЕНИЕ</b>\n\n"

                f"👑 {result['boss']}"

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

            "🏰 Мой клан\n"

            "⚔️ Война кланов\n"

            "🏆 Рейтинг",

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