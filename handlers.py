from telegram import Update


from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)



# =========================
# МЕНЮ
# =========================


from menu_system import (

    main_menu,

    garage_menu,

    garage_cars_menu,

    car_menu,

    tuning_menu,

    race_menu,

    cases_menu,

    shop_menu,

    shop_cars_menu,

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

    race_result_text,

    get_boss,

    fight_boss

)




# =========================
# КЕЙС
# =========================


from shop import (

    open_case,

    get_shop_cars,

    buy_car

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

    clan_text,

    top_clans

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

        """

🏎 <b>CAR LEGENDS</b>


Добро пожаловать!


🚗 Машины

🔧 Тюнинг

🐾 Питомцы

🏁 Гонки

🏆 Карьера


Выбирай раздел 👇

""",

        reply_markup=main_menu(),

        parse_mode="HTML"

    )
    
    # =========================
# BUTTONS
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

{player.get('level',1)}


💰 Монеты:

{player.get('coins',0)}


🏁 Победы:

{player.get('wins',0)}


🚗 Машины:

{len(player.get('garage',[]))}


🐾 Питомцы:

{len(player.get('pets',[]))}

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




    # =====================
    # МАШИНЫ
    # =====================


    if action == "garage_cars":


        cars = get_garage_cars(

            user_id

        )


        await query.edit_message_text(

            "🚗 <b>ТВОИ МАШИНЫ</b>",

            reply_markup=garage_cars_menu(cars),

            parse_mode="HTML"

        )


        return




    # =====================
    # КАРТОЧКА МАШИНЫ
    # =====================


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




    # =====================
    # ГЛАВНАЯ МАШИНА
    # =====================


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

            "👑 Главная машина установлена",

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

            reply_markup=tuning_menu(car),

            parse_mode="HTML"

        )


        return




    # =====================
    # УЛУЧШЕНИЕ
    # =====================


    if action.startswith("upgrade_"):


        data = action.replace(

            "upgrade_",

            ""

        )


        parts = data.split("_")



        if len(parts) >= 2:


            car_name = parts[0]

            part = parts[1]



            result = upgrade_car(

                user_id,

                car_name,

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

            "🎁 <b>ВЫБЕРИ КЕЙС</b>",

            reply_markup=cases_menu(),

            parse_mode="HTML"

        )


        return




    if action in [

        "normal_case",

        "premium_case",

        "legend_case"

    ]:


        car = open_case(

            user_id

        )


        await query.edit_message_text(

            "🎁 <b>КЕЙС ОТКРЫТ</b>\n\n"

            f"🚗 {car['name']}",

            reply_markup=main_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # МАГАЗИН
    # =====================


    if action == "shop":


        cars = get_shop_cars()



        await query.edit_message_text(

            "🛒 <b>АВТОСАЛОН</b>\n\nВыбери машину:",

            reply_markup=shop_cars_menu(cars),

            parse_mode="HTML"

        )


        return




    # =====================
    # ПОКУПКА
    # =====================


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

                "✅ <b>ПОКУПКА УСПЕШНА</b>\n\n"

                f"🚗 {car['name']}"

            )



        except Exception as error:


            text = (

                f"❌ {error}"

            )



        await query.edit_message_text(

            text,

            reply_markup=main_menu(),

            parse_mode="HTML"

        )


        return
        
            # =====================
    # ГОНКИ
    # =====================


    if action == "race":


        await query.edit_message_text(

            "🏁 <b>ВЫБЕРИ ГОНКУ</b>",

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

                "❌ Сначала выбери главную машину",

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
    # БОСС
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

                "❌ Сначала выбери главную машину",

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


⚔️ Гонки игроков

🏆 Рейтинг

🔥 Серии побед


Система будет подключена.

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


Скоро доступно.

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


🏎 CAR LEGENDS SEASON


🎁 Награды

🏆 Рейтинг

🚗 Эксклюзивные машины

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




    if action in [

        "level",

        "rewards"

    ]:


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

{player.get('wins',0)}


❌ Поражения:

{player.get('losses',0)}


💰 Монеты:

{player.get('coins',0)}


🚗 Машины:

{len(player.get('garage',[]))}


🐾 Питомцы:

{len(player.get('pets',[]))}

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


Открываются через карьеру.

""",

            reply_markup=career_menu(),

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

👥 Друзья

🎁 Рефералы

""",

            reply_markup=social_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # РЕЙТИНГ ИГРОКОВ
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
    # МОЙ КЛАН
    # =====================


    if action == "my_clan":


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


        from clan_war_system import clan_war_text



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


        clans = top_clans()



        text = (

            "⚔️ <b>ТОП КЛАНОВ</b>\n\n"

        )



        place = 1



        for clan in clans:


            text += (

                f"{place}. {clan['name']}\n"

                f"⭐ Уровень: {clan['level']}\n"

                f"⚡ Сила: {clan['power']}\n\n"

            )


            place += 1



        if not clans:

            text += "Кланов пока нет"



        await query.edit_message_text(

            text,

            reply_markup=clan_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ТУРНИРЫ
    # =====================


    if action == "tournaments":


        from social_system import tournaments_text



        await query.edit_message_text(

            tournaments_text(),

            reply_markup=social_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ПРОЧЕЕ
    # =====================


    if action in [

        "friends",

        "referrals",

        "exclusive",

        "market",

        "daily_car",

        "parts",

        "skins",

        "garage_upgrade"

    ]:


        await query.edit_message_text(

            """

🔥 <b>РАЗДЕЛ В РАЗРАБОТКЕ</b>


Система будет подключена.

""",

            reply_markup=main_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # НЕИЗВЕСТНО
    # =====================


    await query.edit_message_text(

        "❌ Раздел не найден",

        reply_markup=main_menu()

    )




# =========================
# ОШИБКИ
# =========================


async def error_handler(

    update,

    context

):

    print(

        "Ошибка:",

        context.error

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


    app.add_error_handler(

        error_handler

    )