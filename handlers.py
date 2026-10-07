# =========================
# HANDLERS FINAL COMPLETE
# CAR LEGENDS
# =========================


from telegram import Update

from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)



# DATABASE

from database import (
    get_player,
    update_player
)



# MENUS

from menu_system import (
    main_menu,
    profile_menu,
    garage_menu,
    shop_menu,
    race_menu,
    clan_menu,
    social_menu,
    tuning_menu,
    cases_menu,
    career_menu
)



# CARS

from car_database import (
    get_all_cars,
    get_car
)



# SHOP

from shop_cars import (
    buy_car,
    get_shop_cars
)



# GARAGE

from garage_system import (
    get_garage,
    set_main_car
)



# TUNING

from tuning import (
    upgrade_car
)



# RACES

from boss_race_system import (
    race_npc,
    fight_boss
)



# BATTLES

from battles import (
    create_battle,
    get_battle_result_text
)



# CLANS

from clan_system import (
    create_clan,
    get_player_clan
)


from clan_war_system import (
    clan_war_text
)



# OTHER SYSTEMS

from case_system import (
    open_case
)


from pet_system import (
    get_pets
)


from ranking_system import (
    get_top_players
)


from achievement_system import (
    get_achievements
)


from career_system import (
    get_career
)


from blacklist import (
    blacklist_text
)


from daily_car import (
    get_daily_car
)


from social_system import (
    social_text
)






# =========================
# START COMMAND
# =========================


async def start(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    user = update.effective_user


    player = get_player(

        user.id

    )



    text = f"""

🏎 <b>CAR LEGENDS</b>


👤 Игрок:

{user.first_name}


⭐ Уровень:

{player['level']}


💰 Монеты:

{player['coins']}


🚗 Машина:

{player.get('main_car') or 'Нет'}

"""


    await update.message.reply_text(

        text,

        parse_mode="HTML",

        reply_markup=main_menu()

    )









# =========================
# CALLBACK MAIN
# =========================


async def button_handler(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    query = update.callback_query


    await query.answer()



    data = query.data


    user_id = query.from_user.id





# =========================
# PROFILE
# =========================


    if data == "profile":


        player = get_player(

            user_id

        )



        await query.edit_message_text(

f"""

👤 PROFILE


⭐ Level:

{player['level']}


🔥 XP:

{player['xp']}


💰 Coins:

{player['coins']}


💎 Gems:

{player['gems']}


🏆 Wins:

{player['wins']}


❌ Losses:

{player['losses']}

""",

            reply_markup=profile_menu()

        )






# =========================
# STATS
# =========================


    elif data == "stats":


        player = get_player(

            user_id

        )


        await query.edit_message_text(

f"""

📊 СТАТИСТИКА


🏁 Победы:

{player['wins']}


💀 Поражения:

{player['losses']}


⭐ Уровень:

{player['level']}


🚗 Машин:

{len(player['garage'])}

""",

            reply_markup=profile_menu()

        )






# =========================
# ACHIEVEMENTS
# =========================


    elif data == "achievements":


        text = get_achievements(

            user_id

        )


        await query.edit_message_text(

            text,

            reply_markup=profile_menu()

        )





# =========================
# CAREER
# =========================


    elif data == "career":


        text = get_career(

            user_id

        )


        await query.edit_message_text(

            text,

            reply_markup=career_menu()

        )
        
        
        # =========================
# GARAGE
# =========================


    elif data == "garage":


        player = get_player(

            user_id

        )


        cars = player.get(

            "garage",

            []

        )


        if not cars:


            await query.edit_message_text(

                "🚗 Гараж пуст",

                reply_markup=garage_menu()

            )

            return





        text = """

🚗 <b>ТВОЙ ГАРАЖ</b>


"""



        for car in cars:


            text += (

                f"🏎 {car}\n"

            )



        await query.edit_message_text(

            text,

            parse_mode="HTML",

            reply_markup=garage_menu()

        )







# =========================
# GARAGE CARS
# =========================


    elif data == "garage_cars":


        player = get_player(

            user_id

        )



        text = """

🚗 <b>МАШИНЫ</b>


"""



        for car in player["garage"]:


            text += (

                f"\n🏎 {car}"

            )



        await query.edit_message_text(

            text,

            parse_mode="HTML",

            reply_markup=garage_menu()

        )







# =========================
# SET MAIN CAR
# =========================


    elif data.startswith(

        "main_"

    ):


        car = data.replace(

            "main_",

            ""

        )


        result = set_main_car(

            user_id,

            car

        )



        await query.edit_message_text(

            f"""

👑 Главная машина:


{car}


Установлена.

""",

            reply_markup=garage_menu()

        )








# =========================
# SHOP
# =========================


    elif data == "shop":


        await query.edit_message_text(

            """

🛒 <b>МАГАЗИН</b>


Выбери раздел:

""",

            parse_mode="HTML",

            reply_markup=shop_menu()

        )








# =========================
# SHOP CARS
# =========================


    elif data == "shop_cars":


        cars = get_shop_cars()



        text = """

🚗 <b>АВТОСАЛОН</b>


"""



        for car in cars[:30]:


            text += (

                f"""

🏎 {car['name']}

💰 Цена:
{car['price']}


"""

            )



        await query.edit_message_text(

            text,

            parse_mode="HTML"

        )







# =========================
# BUY CAR
# =========================


    elif data.startswith(

        "buy_"

    ):


        car = data.replace(

            "buy_",

            ""

        )



        result = buy_car(

            user_id,

            car

        )



        await query.edit_message_text(

            str(result)

        )








# =========================
# TUNING
# =========================


    elif data == "tuning":


        player = get_player(

            user_id

        )


        car = player.get(

            "main_car"

        )



        if not car:


            await query.edit_message_text(

                "❌ Сначала выбери машину"

            )

            return





        await query.edit_message_text(

            f"""

🔧 ТЮНИНГ


🚗 {car}


Выбери улучшение:

""",

            reply_markup=tuning_menu(

                car

            )

        )







# =========================
# UPGRADE
# =========================


    elif data.startswith(

        "upgrade_"

    ):


        parts = data.split("_")



        if len(parts) >= 3:


            car = parts[1]

            upgrade = parts[2]



            result = upgrade_car(

                user_id,

                car,

                upgrade

            )



            await query.edit_message_text(

                str(result)

            )








# =========================
# CASES
# =========================


    elif data == "cases":


        await query.edit_message_text(

            """

🎁 КЕЙСЫ


Выбери кейс:

""",

            reply_markup=cases_menu()

        )







# =========================
# OPEN CASE
# =========================


    elif data.endswith(

        "_case"

    ):


        case = data.replace(

            "_case",

            ""

        )



        result = open_case(

            user_id,

            case

        )



        await query.edit_message_text(

            str(result)

        )
        
        
        # =========================
# RACE MENU
# =========================


    elif data == "race":


        await query.edit_message_text(

            """

🏁 ГОНКИ


Выбери режим:

""",

            reply_markup=race_menu()

        )








# =========================
# NPC RACE
# =========================


    elif data == "npc":


        player = get_player(

            user_id

        )


        car = player.get(

            "main_car"

        )


        if not car:


            await query.edit_message_text(

                "❌ Нет активной машины"

            )

            return





        result = race_npc(

            user_id,

            car

        )



        await query.edit_message_text(

            str(result)

        )








# =========================
# BOSS RACE
# =========================


    elif data == "boss":


        player = get_player(

            user_id

        )


        car = player.get(

            "main_car"

        )


        result = fight_boss(

            user_id,

            car,

            "boss"

        )



        await query.edit_message_text(

            str(result)

        )







# =========================
# PVP
# =========================


    elif data == "pvp":


        await query.edit_message_text(

            """

⚔️ PVP


Ожидание соперника...

"""

        )








# =========================
# BLACKLIST
# =========================


    elif data == "blacklist":


        text = blacklist_text(

            user_id

        )



        await query.edit_message_text(

            text

        )








# =========================
# DAILY CAR
# =========================


    elif data == "daily_car":


        car = get_daily_car(

            user_id

        )



        await query.edit_message_text(

            f"""

🎁 Ежедневная машина:


🏎 {car}

"""

        )








# =========================
# PETS
# =========================


    elif data == "pets":


        pets = get_pets(

            user_id

        )


        await query.edit_message_text(

            str(pets)

        )








# =========================
# RANKING
# =========================


    elif data == "players_rating":


        rating = get_top_players()



        text = """

🏆 ТОП ИГРОКОВ


"""



        for player in rating:


            text += (

                f"""

👤 {player['name']}

⭐ {player['level']}

🏁 {player['wins']} побед


"""

            )



        await query.edit_message_text(

            text

        )








# =========================
# SOCIAL
# =========================


    elif data == "social":


        text = social_text(

            user_id

        )



        await query.edit_message_text(

            text,

            reply_markup=social_menu()

        )








# =========================
# BATTLE
# =========================


    elif data == "battle":


        await query.edit_message_text(

            """

⚔️ БОИ


Выбор противника...

"""

        )
        
        
        # =========================
# CLAN MENU
# =========================


    elif data == "clan":


        await query.edit_message_text(

            """

⚔️ КЛАНЫ


Выбери действие:

""",

            reply_markup=clan_menu()

        )








# =========================
# MY CLAN
# =========================


    elif data == "my_clan":


        clan = get_player_clan(

            user_id

        )



        if not clan:


            await query.edit_message_text(

                """

❌ Ты не состоишь в клане


Создай свой клан или вступи в существующий.

"""

            )

            return





        await query.edit_message_text(

            f"""

⚔️ ТВОЙ КЛАН


🏰 Название:

{clan.get('name')}


👥 Участники:

{len(clan.get('members', []))}


🔥 Сила:

{clan.get('power',0)}

"""

        )








# =========================
# CLAN WAR
# =========================


    elif data == "clan_war":


        text = clan_war_text(

            user_id

        )



        await query.edit_message_text(

            text

        )








# =========================
# CLAN RATING
# =========================


    elif data == "clan_rating":


        await query.edit_message_text(

            """

🏆 ТОП КЛАНОВ


Рейтинг загружается...

"""

        )








# =========================
# CAREER
# =========================


    elif data == "career":


        text = get_career(

            user_id

        )



        await query.edit_message_text(

            text,

            reply_markup=career_menu()

        )








# =========================
# BATTLE PASS
# =========================


    elif data == "battle_pass":


        await query.edit_message_text(

            """

🎫 BATTLE PASS


Уровень сезона:

1


Награды доступны.

"""

        )








# =========================
# TOURNAMENTS
# =========================


    elif data == "tournaments":


        await query.edit_message_text(

            """

🏆 ТУРНИРЫ


Скоро доступно.

"""

        )








# =========================
# BACK
# =========================


    elif data == "back":


        await query.edit_message_text(

            """

🏎 CAR LEGENDS


Главное меню:

""",

            reply_markup=main_menu()

        )








# =========================
# UNKNOWN
# =========================


    else:


        await query.edit_message_text(

            """

❌ Неизвестная команда

"""

        )









# =========================
# REGISTER HANDLERS
# =========================


def register_handlers(

    application

):


    application.add_handler(

        CommandHandler(

            "start",

            start

        )

    )



    application.add_handler(

        CallbackQueryHandler(

            button_handler

        )

    )