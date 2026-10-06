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


from systems.garage_system import (
    get_garage_cars,
    garage_text,
    car_text,
    set_main_car
)


from systems.pet_system import (
    pets_text
)


from systems.tuning_system import (
    tuning_text
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


🚗 Собирай легендарные машины

🔧 Улучшай характеристики

🐾 Собирай питомцев

🏁 Побеждай в гонках


Твой путь начинается!
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
    # ГЛАВНОЕ
    # =====================


    if action == "back":


        await query.edit_message_text(

            "🏎 Главное меню",

            reply_markup=main_menu()

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




    elif action == "garage_cars":


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

            "🚘 Твои машины:",

            reply_markup=

            garage_cars_menu(cars)

        )




    elif action.startswith("car_"):


        car_name = action.replace(

            "car_",

            ""

        )


        await query.edit_message_text(

            car_text(

                user_id,

                car_name

            ),

            reply_markup=

            car_menu(car_name),

            parse_mode="HTML"

        )




    elif action.startswith("main_"):


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

👑 <b>Главная машина изменена</b>


🚗 {car_name}

""",

            reply_markup=main_menu(),

            parse_mode="HTML"

        )
            # =====================
    # ТЮНИНГ
    # =====================


    elif action == "tuning":


        await query.edit_message_text(

            tuning_text(user_id),

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )




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
    # ДЕТАЛИ
    # =====================


    elif action == "parts":


        await query.edit_message_text(

            """
🧩 <b>ДЕТАЛИ</b>


⚙️ Двигатель

🛞 Шины

💨 Турбо

🔋 Электроника


Раздел развивается
""",

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )




    # =====================
    # СКИНЫ
    # =====================


    elif action == "skins":


        await query.edit_message_text(

            """
🎨 <b>СКИНЫ</b>


🚗 Стандартный

🔥 Гоночный

💎 Легендарный


Скоро можно будет менять внешний вид
""",

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )




    # =====================
    # РАСШИРЕНИЕ ГАРАЖА
    # =====================


    elif action == "garage_upgrade":


        await query.edit_message_text(

            """
🏠 <b>РАСШИРЕНИЕ ГАРАЖА</b>


Текущий уровень: 1


🚗 Вместимость:
5 машин


Скоро:
+ новые места
+ бонусы гаража
""",

            reply_markup=garage_menu(),

            parse_mode="HTML"

        )




    # =====================
    # УЛУЧШЕНИЕ МАШИНЫ
    # =====================


    elif action.startswith("upgrade_"):


        car_name = action.replace(

            "upgrade_",

            ""

        )


        await query.edit_message_text(

            f"""

🔧 <b>УЛУЧШЕНИЕ</b>


🚗 {car_name}


⚡ Следующий уровень:

+50 мощности

+20 скорости


(система прокачки будет подключена)
""",

            reply_markup=car_menu(car_name),

            parse_mode="HTML"

        )




    # =====================
    # ВНЕШНИЙ ВИД
    # =====================


    elif action.startswith("skin_"):


        car_name = action.replace(

            "skin_",

            ""

        )


        await query.edit_message_text(

            f"""

🎨 <b>ВНЕШНИЙ ВИД</b>


🚗 {car_name}


Доступные стили:

⚪ Стандарт

🔥 Спорт

💎 Премиум


Скоро появится магазин скинов.
""",

            reply_markup=car_menu(car_name),

            parse_mode="HTML"

        )
            # =====================
    # ГОНКИ
    # =====================


    elif action == "race":


        await query.edit_message_text(

            """
🏁 <b>ГОНКИ</b>


Выбери режим:
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # =====================
    # NPC
    # =====================


    elif action == "npc":


        await query.edit_message_text(

            """
🤖 <b>ГОНКА С NPC</b>


Соперник найден!


🚗 Твоя машина

⚡ Мощность: -

🚀 Скорость: -


Режим гонок будет подключён.
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # =====================
    # БОССЫ
    # =====================


    elif action == "boss":


        await query.edit_message_text(

            """
👑 <b>БОССЫ</b>


Доступные боссы:


🔥 Уличный король

💎 Легенда трассы

👑 Император скорости


Победи их и получи награды!
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # =====================
    # PVP
    # =====================


    elif action == "pvp":


        await query.edit_message_text(

            """
🌎 <b>PVP</b>


Сражения между игроками.


🏆 Рейтинг

🔥 Серии побед

💎 Награды


Скоро будет доступно.
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # =====================
    # ЧЕМПИОНАТЫ
    # =====================


    elif action == "championship":


        await query.edit_message_text(

            """
🏆 <b>ЧЕМПИОНАТЫ</b>


Сезонные соревнования:


🥇 1 место

🥈 2 место

🥉 3 место


Система в разработке.
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # =====================
    # СЕЗОНЫ
    # =====================


    elif action == "seasons":


        await query.edit_message_text(

            """
🔥 <b>СЕЗОН</b>


Текущий сезон:

🏎 Первый заезд


Награды:

🎁 Кейсы

💎 Валюта

🏆 Титулы
""",

            reply_markup=race_menu(),

            parse_mode="HTML"

        )




    # =====================
    # АВТОСАЛОН
    # =====================


    elif action == "shop":


        await query.edit_message_text(

            """
🛒 <b>АВТОСАЛОН</b>


🚗 Машины

💎 Эксклюзивы

🔄 Рынок игроков

🔥 Машина дня
""",

            reply_markup=shop_menu(),

            parse_mode="HTML"

        )




    # =====================
    # ПОКУПКА МАШИН
    # =====================


    elif action == "buy_car":


        await query.edit_message_text(

            """
🚗 <b>ПОКУПКА МАШИНЫ</b>


Доступные автомобили:


🚗 Honda Civic

🏎 BMW M3

🔥 Supra MK5

👑 Bugatti X
""",

            reply_markup=shop_menu(),

            parse_mode="HTML"

        )




    # =====================
    # КЕЙСЫ
    # =====================


    elif action == "cases":


        await query.edit_message_text(

            """
🎁 <b>КЕЙСЫ</b>


Открывай и получай:


🚗 Машины

🐾 Питомцев

🧩 Детали

💎 Валюту
""",

            reply_markup=cases_menu(),

            parse_mode="HTML"

        )




    elif action in [

        "normal_case",

        "premium_case",

        "legend_case"

    ]:


        await query.edit_message_text(

            """
📦 <b>КЕЙС ОТКРЫТ</b>


Система выпадения наград будет подключена.


🎁 Удачи!
""",

            reply_markup=main_menu(),

            parse_mode="HTML"

        )
            # =====================
    # ПРОФИЛЬ
    # =====================


    elif action == "profile":


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




    # =====================
    # КАРЬЕРА
    # =====================


    elif action == "career":


        await query.edit_message_text(

            """
🏆 <b>КАРЬЕРА</b>


⭐ Уровень игрока

🎁 Награды

🎫 Боевой пропуск

🏅 Достижения


Система прогресса будет подключена.
""",

            reply_markup=career_menu(),

            parse_mode="HTML"

        )




    # =====================
    # КЛАН
    # =====================


    elif action == "clan":


        await query.edit_message_text(

            """
⚔️ <b>КЛАН</b>


🏰 Создать клан

👥 Участники

⚔️ Война кланов

🏆 Рейтинг


Система кланов будет подключена.
""",

            reply_markup=clan_menu(),

            parse_mode="HTML"

        )




    # =====================
    # СОЦИАЛЬНОЕ
    # =====================


    elif action == "social":


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




    # =====================
    # ЗАГЛУШКИ
    # =====================


    elif action in [

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


Скоро здесь появится полноценная система.
""",

            reply_markup=main_menu(),

            parse_mode="HTML"

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