from telegram import Update

from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)


# =========================
# МЕНЮ
# =========================


from menus.menu_system import (

    main_menu,

    garage_menu,

    garage_cars_menu,

    car_menu,

    race_menu,

    shop_menu,

    cases_menu,

    profile_menu,

    career_menu,

    clan_menu,

    social_menu

)



# =========================
# БАЗА
# =========================


from database import (

    get_player

)



# =========================
# ГАРАЖ
# =========================


from garage_system import (

    get_garage_cars,

    garage_text,

    car_text,

    set_main_car

)



# =========================
# ТЮНИНГ
# =========================


from tuning import (

    tuning_text,

    upgrade_car

)



# =========================
# ПИТОМЦЫ
# =========================


from pet_system import (

    pets_text

)



# =========================
# ГОНКИ
# =========================


from race_system import (

    race_npc,

    fight_boss,

    race_result_text,

    get_boss

)



# =========================
# КЕЙСЫ
# =========================


from case_system import (

    open_case

)



# =========================
# МАГАЗИН
# =========================


from shop import (

    buy_car,

    get_shop_cars

)



# =========================
# КАРЬЕРА
# =========================


from career_system import (

    career_text

)



# =========================
# КЛАНЫ
# =========================


from clan_system import (

    clan_text

)



# =========================
# СОЦИАЛЬНОЕ
# =========================


from social_system import (

    top_text,

    battle_pass_text

)



# =========================
# ДОСТИЖЕНИЯ
# =========================


from achievement_system import (

    achievement_text

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

        f"""

🏎 <b>CAR LEGENDS</b>


Привет, {user.first_name}!


🚗 Собирай машины

🔧 Улучшай их

🐾 Собирай питомцев

🏁 Побеждай в гонках


Добро пожаловать в мир скорости!

""",

        reply_markup=main_menu(),

        parse_mode="HTML"

    )





# =========================
# CALLBACK
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
    # НАЗАД
    # =====================


    if action == "back":


        await query.edit_message_text(

            "🏎 Главное меню",

            reply_markup=main_menu()

        )


        return




    # =====================
    # ПРОФИЛЬ
    # =====================


    if action == "profile":


        player = get_player(

            user_id

        )


        await query.edit_message_text(

            f"""

👤 <b>ПРОФИЛЬ</b>


⭐ Уровень:

{player['level']}


💰 Монеты:

{player['coins']}


🏁 Победы:

{player['wins']}


🚗 Машин:

{len(player['garage'])}

🐾 Питомцев:

{len(player['pets'])}

""",

            reply_markup=profile_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ГАРАЖ
    # =====================


    if action == "garage":


        await query.edit_message_text(

            garage_text(user_id),

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )


        return




    if action == "garage_cars":


        cars = get_garage_cars(

            user_id

        )


        await query.edit_message_text(

            "🚗 Твои машины",

            reply_markup=garage_cars_menu(cars)

        )


        return




    if action.startswith("car_"):


        car_name = action.replace(

            "car_",

            ""

        )


        await query.edit_message_text(

            car_text(

                user_id,

                car_name

            ),

            reply_markup=car_menu(car_name),

            parse_mode="HTML"

        )


        return




    if action.startswith("main_"):


        car_name = action.replace(

            "main_",

            ""

        )


        set_main_car(

            user_id,

            car_name

        )


        await query.edit_message_text(

            "👑 Главная машина изменена",

            reply_markup=main_menu()

        )


        return
        
            # =====================
    # ТЮНИНГ
    # =====================


    if action == "tuning":


        player = get_player(

            user_id

        )


        car = player.get(

            "main_car"

        )



        if not car:


            await query.edit_message_text(

                "❌ Сначала выбери главную машину",

                reply_markup=garage_menu()

            )

            return



        await query.edit_message_text(

            tuning_text(

                user_id,

                car

            ),

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # УЛУЧШЕНИЕ
    # =====================


    if action.startswith("upgrade_"):


        info = action.replace(

            "upgrade_",

            ""

        )


        data = info.split("_")



        if len(data) >= 2:


            car = data[0]

            part = data[1]



            result = upgrade_car(

                user_id,

                car,

                part

            )



            await query.edit_message_text(

                result["message"],

                reply_markup=garage_menu(),

                parse_mode="HTML"

            )



        return




    # =====================
    # ПИТОМЦЫ
    # =====================


    if action == "pets":


        await query.edit_message_text(

            pets_text(user_id),

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # КЕЙСЫ
    # =====================


    if action == "cases":


        await query.edit_message_text(

            """
🎁 <b>КЕЙСЫ</b>


📦 Обычный

💎 Премиум

🔥 Легендарный


Выбери свой шанс!
""",

            reply_markup=cases_menu(),

            parse_mode="HTML"

        )


        return




    if action.startswith("case_"):


        case_id = action.replace(

            "case_",

            ""

        )



        result = open_case(

            user_id,

            case_id

        )



        await query.edit_message_text(

            result["message"],

            reply_markup=main_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # МАГАЗИН
    # =====================


    if action == "shop":


        cars = get_shop_cars()



        text = (

            "🛒 <b>АВТОСАЛОН</b>\n\n"

        )



        for car in cars:


            text += (

                f"{car['name']}\n"

                f"💰 {car['price']}\n\n"

            )



        await query.edit_message_text(

            text,

            reply_markup=shop_menu(),

            parse_mode="HTML"

        )


        return




    if action.startswith("buy_"):


        car_name = action.replace(

            "buy_",

            ""

        )


        try:


            car = buy_car(

                user_id,

                car_name

            )


            text = (

                "🚗 <b>ПОКУПКА УСПЕШНА</b>\n\n"

                f"{car['name']}"

            )



        except Exception as e:


            text = (

                f"❌ {e}"

            )



        await query.edit_message_text(

            text,

            reply_markup=shop_menu(),

            parse_mode="HTML"

        )


        return
        
            # =====================
    # ГОНКИ
    # =====================


    if action == "race":


        await query.edit_message_text(

            """
🏁 <b>ГОНКИ</b>


Выбери режим:

🤖 NPC

👑 Боссы

🌎 PvP

🏆 Чемпионаты
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # NPC ГОНКА
    # =====================


    if action == "npc":


        player = get_player(

            user_id

        )


        car = player.get(

            "main_car"

        )



        if not car:


            await query.edit_message_text(

                "❌ Нет главной машины",

                reply_markup=main_menu()

            )

            return



        result = race_npc(

            user_id,

            car

        )



        await query.edit_message_text(

            race_result_text(result),

            reply_markup=race_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # БОССЫ
    # =====================


    if action == "boss":


        player = get_player(

            user_id

        )


        car = player.get(

            "main_car"

        )



        if not car:


            await query.edit_message_text(

                "❌ Нет главной машины",

                reply_markup=main_menu()

            )

            return



        boss = get_boss()



        result = fight_boss(

            user_id,

            car,

            boss["id"]

        )



        await query.edit_message_text(

            race_result_text(result),

            reply_markup=race_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # PVP
    # =====================


    if action == "pvp":


        await query.edit_message_text(

            """
🌎 <b>PVP</b>


⚔️ Гонки между игроками

🏆 Рейтинг

🔥 Серии побед


Система готовится.
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ЧЕМПИОНАТЫ
    # =====================


    if action == "championship":


        await query.edit_message_text(

            """
🏆 <b>ЧЕМПИОНАТЫ</b>


🥇 Турниры

🎁 Награды

🔥 Сезонные гонки


Скоро будет доступно.
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # СЕЗОНЫ
    # =====================


    if action == "seasons":


        await query.edit_message_text(

            """
🔥 <b>СЕЗОН</b>


🏎 Первый заезд


Награды:

💎 Валюта

🎁 Кейсы

🏆 Титулы
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )


        return
        
            # =====================
    # КАРЬЕРА
    # =====================


    if action == "career":


        await query.edit_message_text(

            career_text(user_id),

            reply_markup=career_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ДОСТИЖЕНИЯ
    # =====================


    if action == "achievements":


        await query.edit_message_text(

            achievement_text(user_id),

            reply_markup=profile_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # СОЦИАЛЬНОЕ
    # =====================


    if action == "social":


        await query.edit_message_text(

            """
🌐 <b>СОЦИАЛЬНОЕ</b>


🏆 Рейтинг игроков

🎫 Battle Pass

🏁 Турниры

👥 Друзья


Выбери раздел.
""",

            reply_markup=social_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # РЕЙТИНГ
    # =====================


    if action == "players_rating":


        await query.edit_message_text(

            top_text(),

            reply_markup=social_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # BATTLE PASS
    # =====================


    if action == "battle_pass":


        await query.edit_message_text(

            battle_pass_text(),

            reply_markup=social_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # СТАТИСТИКА
    # =====================


    if action == "stats":


        player = get_player(

            user_id

        )


        await query.edit_message_text(

            f"""

📊 <b>СТАТИСТИКА</b>


🏁 Победы:

{player['wins']}


❌ Поражения:

{player['losses']}


🚗 Машины:

{len(player['garage'])}


🐾 Питомцы:

{len(player['pets'])}

""",

            reply_markup=profile_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ТИТУЛЫ
    # =====================


    if action == "titles":


        await query.edit_message_text(

            """

🎖 <b>ТИТУЛЫ</b>


👑 Car Legend

🔥 Speed Master

🏁 Street Racer


Титулы открываются через карьеру.
""",

            reply_markup=career_menu(),

            parse_mode="HTML"

        )


        return
        
            # =====================
    # КЛАНЫ
    # =====================


    if action == "clan":


        await query.edit_message_text(

            clan_text(user_id),

            reply_markup=clan_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ВОЙНА КЛАНОВ
    # =====================


    if action == "clan_war":


        from clan_war_system import (

            clan_war_text

        )


        await query.edit_message_text(

            clan_war_text(user_id),

            reply_markup=clan_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # РЕЙТИНГ КЛАНОВ
    # =====================


    if action == "clan_rating":


        from clan_system import (

            top_clans

        )



        clans = top_clans()



        text = (

            "⚔️ <b>ТОП КЛАНОВ</b>\n\n"

        )



        place = 1



        for clan in clans:


            text += (

                f"{place}. "

                f"{clan['name']}\n"

                f"⭐ Уровень: "

                f"{clan['level']}\n"

                f"⚡ Сила: "

                f"{clan['power']}\n\n"

            )


            place += 1



        await query.edit_message_text(

            text,

            reply_markup=clan_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ДРУГИЕ РАЗДЕЛЫ
    # =====================


    if action in [

        "friends",

        "referrals",

        "market",

        "daily_car",

        "exclusive",

        "tournaments"

    ]:


        await query.edit_message_text(

            """
🔥 <b>РАЗДЕЛ В РАЗРАБОТКЕ</b>


Система будет подключена позже.
""",

            reply_markup=main_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # НЕИЗВЕСТНАЯ КНОПКА
    # =====================


    await query.edit_message_text(

        "❌ Раздел не найден",

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