# =========================
# MENU SYSTEM FINAL
# CAR LEGENDS
# =========================


from telegram import InlineKeyboardButton, InlineKeyboardMarkup





# =========================
# MAIN MENU
# =========================


def main_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "🏎 Гонки",
                callback_data="race"
            ),

            InlineKeyboardButton(
                "🚗 Гараж",
                callback_data="garage"
            )

        ],


        [

            InlineKeyboardButton(
                "🔧 Тюнинг",
                callback_data="tuning"
            ),

            InlineKeyboardButton(
                "🛒 Магазин",
                callback_data="shop"
            )

        ],


        [

            InlineKeyboardButton(
                "🏆 Blacklist",
                callback_data="blacklist"
            ),

            InlineKeyboardButton(
                "👤 Профиль",
                callback_data="profile"
            )

        ],


        [

            InlineKeyboardButton(
                "⚔️ Кланы",
                callback_data="clan"
            ),

            InlineKeyboardButton(
                "🌎 Социальное",
                callback_data="social"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )







# =========================
# PROFILE MENU
# =========================


def profile_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "📊 Статистика",
                callback_data="stats"
            )

        ],


        [

            InlineKeyboardButton(
                "🏆 Достижения",
                callback_data="achievements"
            )

        ],


        [

            InlineKeyboardButton(
                "🎖 Титулы",
                callback_data="titles"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# GARAGE MENU
# =========================


def garage_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "🚗 Мои машины",
                callback_data="garage_cars"
            )

        ],


        [

            InlineKeyboardButton(
                "🐾 Питомцы",
                callback_data="pets"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# GARAGE CARS
# =========================


def garage_cars_menu(cars):


    keyboard = []



    for car in cars:


        keyboard.append(

            [

                InlineKeyboardButton(

                    "🚗 " + car,

                    callback_data="car_" + car

                )

            ]

        )



    keyboard.append(

        [

            InlineKeyboardButton(

                "⬅️ Назад",

                callback_data="garage"

            )

        ]

    )



    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# CAR MENU
# =========================


def car_menu(car):


    keyboard = [


        [

            InlineKeyboardButton(
                "👑 Сделать главной",
                callback_data="main_" + car
            )

        ],


        [

            InlineKeyboardButton(
                "🔧 Тюнинг",
                callback_data="upgrade_" + car
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="garage"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# TUNING
# =========================


def tuning_menu(car):


    keyboard = [


        [

            InlineKeyboardButton(
                "⚡ Двигатель",
                callback_data=f"upgrade_{car}_engine"
            )

        ],


        [

            InlineKeyboardButton(
                "🚀 Турбо",
                callback_data=f"upgrade_{car}_turbo"
            )

        ],


        [

            InlineKeyboardButton(
                "🎯 Управление",
                callback_data=f"upgrade_{car}_handling"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="garage"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# RACE MENU
# =========================


def race_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "🏁 NPC гонка",
                callback_data="npc"
            )

        ],


        [

            InlineKeyboardButton(
                "👑 Boss",
                callback_data="boss"
            )

        ],


        [

            InlineKeyboardButton(
                "⚔️ PVP",
                callback_data="pvp"
            )

        ],


        [

            InlineKeyboardButton(
                "🏆 Чемпионаты",
                callback_data="championship"
            )

        ],


        [

            InlineKeyboardButton(
                "🔥 Сезоны",
                callback_data="seasons"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# CASE MENU
# =========================


def cases_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "🎁 Обычный кейс",
                callback_data="normal_case"
            )

        ],


        [

            InlineKeyboardButton(
                "💎 Premium кейс",
                callback_data="premium_case"
            )

        ],


        [

            InlineKeyboardButton(
                "👑 Legendary кейс",
                callback_data="legend_case"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="shop"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# SHOP MENU
# =========================


def shop_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "🚗 Машины",
                callback_data="shop_cars"
            )

        ],


        [

            InlineKeyboardButton(
                "🎁 Кейсы",
                callback_data="cases"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# CAREER
# =========================


def career_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "⭐ Уровень",
                callback_data="level"
            )

        ],


        [

            InlineKeyboardButton(
                "🎁 Награды",
                callback_data="rewards"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# CLAN
# =========================


def clan_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "⚔️ Мой клан",
                callback_data="my_clan"
            )

        ],


        [

            InlineKeyboardButton(
                "🔥 Война кланов",
                callback_data="clan_war"
            )

        ],


        [

            InlineKeyboardButton(
                "🏆 Топ кланов",
                callback_data="clan_rating"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )








# =========================
# SOCIAL
# =========================


def social_menu():


    keyboard = [


        [

            InlineKeyboardButton(
                "🏆 Рейтинг игроков",
                callback_data="players_rating"
            )

        ],


        [

            InlineKeyboardButton(
                "🎫 Battle Pass",
                callback_data="battle_pass"
            )

        ],


        [

            InlineKeyboardButton(
                "🏆 Турниры",
                callback_data="tournaments"
            )

        ],


        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )