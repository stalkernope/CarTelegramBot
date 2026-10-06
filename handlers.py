from telegram import Update

from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)


from menus.menu_system import (

    main_menu,

    garage_menu,

    garage_cars_menu,

    car_menu,

    race_menu,

    profile_menu,

    cases_menu,

    shop_menu,

    clan_menu,

    career_menu,

    social_menu

)



from database import (

    get_player,

    update_player

)



from garage_system import (

    get_garage_cars,

    garage_text,

    car_text,

    set_main_car

)



from tuning import (

    tuning_text,

    upgrade_car

)



from pet_system import (

    pets_text

)



from race_system import (

    race_npc,

    fight_boss,

    race_result_text,

    get_boss

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


Добро пожаловать, {user.first_name}!


🚗 Собирай машины

🔧 Улучшай их

🐾 Собирай питомцев

🏁 Побеждай в гонках


Стань легендой трассы!

""",

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


        if not cars:


            await query.edit_message_text(

                "🚗 Гараж пуст",

                reply_markup=garage_menu()

            )

            return



        await query.edit_message_text(

            "🚘 <b>ТВОИ МАШИНЫ</b>",

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

            f"""

👑 <b>Главная машина</b>


🚗 {car_name}

""",

            reply_markup=main_menu(),

            parse_mode="HTML"

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
    # УЛУЧШЕНИЕ ДЕТАЛИ
    # =====================


    if action.startswith("upgrade_"):


        data = action.replace(

            "upgrade_",

            ""

        )


        parts = data.split(

            "_"

        )



        if len(parts) < 2:


            await query.edit_message_text(

                "❌ Ошибка улучшения",

                reply_markup=garage_menu()

            )

            return



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
    # ДЕТАЛИ
    # =====================


    if action == "parts":


        await query.edit_message_text(

            """
🧩 <b>ДЕТАЛИ</b>


⚙️ Двигатели

🔥 Турбо

🛞 Шины

🔧 Подвеска


Система инвентаря деталей будет подключена.
""",

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # СКИНЫ
    # =====================


    if action == "skins":


        await query.edit_message_text(

            """
🎨 <b>СКИНЫ</b>


🚗 Стандарт

🔥 Гоночный

💎 Премиум

👑 Легендарный


Система внешнего вида готовится.
""",

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # РАСШИРЕНИЕ ГАРАЖА
    # =====================


    if action == "garage_upgrade":


        await query.edit_message_text(

            """
🏠 <b>РАСШИРЕНИЕ ГАРАЖА</b>


Текущий уровень: 1


🚗 Вместимость:
5 машин


Скоро:

+ дополнительные места

+ бонусы гаража

""",

            reply_markup=garage_menu(),

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
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # NPC
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


⚔️ Сражения игроков

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

🔥 Сезонный рейтинг


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
🔥 <b>СЕЗОНЫ</b>


Текущий сезон:

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
    # МАГАЗИН
    # =====================


    if action == "shop":


        await query.edit_message_text(

            """
🛒 <b>АВТОСАЛОН</b>


🚗 Машины

💎 Эксклюзивы

🔄 Рынок

🔥 Машина дня
""",

            reply_markup=shop_menu(),

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


Выбери кейс.
""",

            reply_markup=cases_menu(),

            parse_mode="HTML"

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


💎 Кристаллы:
{player['gems']}


🏁 Победы:
{player['wins']}


❌ Поражения:
{player['losses']}


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
    # КАРЬЕРА
    # =====================


    if action == "career":


        await query.edit_message_text(

            """
🏆 <b>КАРЬЕРА</b>


⭐ Уровень

🎁 Награды

🎫 Боевой пропуск

🏅 Достижения


Система прогресса будет подключена.
""",

            reply_markup=career_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # КЛАН
    # =====================


    if action == "clan":


        await query.edit_message_text(

            """
⚔️ <b>КЛАН</b>


🏰 Мой клан

⚔️ Война кланов

🏆 Рейтинг


Клановая система готовится.
""",

            reply_markup=clan_menu(),

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


👥 Друзья

🎁 Рефералы

🏆 Рейтинг игроков


Скоро будет доступно.
""",

            reply_markup=social_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # ОСТАЛЬНЫЕ РАЗДЕЛЫ
    # =====================


    if action in [

        "stats",

        "achievements",

        "titles",

        "level",

        "rewards",

        "battle_pass",

        "friends",

        "referrals",

        "players_rating",

        "my_clan",

        "clan_war",

        "clan_rating",

        "exclusive",

        "market",

        "daily_car"

    ]:


        await query.edit_message_text(

            """
🔥 <b>РАЗДЕЛ В РАЗРАБОТКЕ</b>


Этот модуль будет подключён позже.
""",

            reply_markup=main_menu(),

            parse_mode="HTML"

        )


        return




    # =====================
    # НЕИЗВЕСТНАЯ КНОПКА
    # =====================


    await query.edit_message_text(

        "🔥 Раздел недоступен",

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