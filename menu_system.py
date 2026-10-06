from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)




# =========================
# ГЛАВНОЕ МЕНЮ
# =========================


def main_menu():


    keyboard = [

        [

            InlineKeyboardButton(
                "🚗 ГАРАЖ",
                callback_data="garage"
            ),

            InlineKeyboardButton(
                "🏁 ГОНКИ",
                callback_data="race"
            )

        ],


        [

            InlineKeyboardButton(
                "🛒 АВТОСАЛОН",
                callback_data="shop"
            ),

            InlineKeyboardButton(
                "🎁 КЕЙСЫ",
                callback_data="cases"
            )

        ],


        [

            InlineKeyboardButton(
                "👤 ПРОФИЛЬ",
                callback_data="profile"
            ),

            InlineKeyboardButton(
                "🏆 КАРЬЕРА",
                callback_data="career"
            )

        ],


        [

            InlineKeyboardButton(
                "⚔️ КЛАН",
                callback_data="clan"
            ),

            InlineKeyboardButton(
                "🌐 СОЦИАЛЬНОЕ",
                callback_data="social"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )




# =========================
# ГАРАЖ
# =========================


def garage_menu():


    keyboard = [

        [

            InlineKeyboardButton(
                "🚘 Мои машины",
                callback_data="garage_cars"
            )

        ],

        [

            InlineKeyboardButton(
                "🔧 Тюнинг",
                callback_data="tuning"
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
                "🧩 Детали",
                callback_data="parts"
            )

        ],

        [

            InlineKeyboardButton(
                "🎨 Скины",
                callback_data="skins"
            )

        ],

        [

            InlineKeyboardButton(
                "🏠 Расширить гараж",
                callback_data="garage_upgrade"
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
# МАШИНЫ
# =========================


def garage_cars_menu(cars):


    keyboard = []



    for car in cars:


        keyboard.append(

            [

                InlineKeyboardButton(

                    car["name"],

                    callback_data=

                    f"car_{car['name']}"

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
# КАРТОЧКА МАШИНЫ
# =========================


def car_menu(car_name):


    keyboard = [

        [

            InlineKeyboardButton(

                "👑 Сделать главной",

                callback_data=

                f"main_{car_name}"

            )

        ],


        [

            InlineKeyboardButton(

                "🔧 Улучшить",

                callback_data=

                f"upgrade_{car_name}"

            )

        ],


        [

            InlineKeyboardButton(

                "🎨 Внешний вид",

                callback_data=

                f"skin_{car_name}"

            )

        ],


        [

            InlineKeyboardButton(

                "⬅️ Назад",

                callback_data="garage_cars"

            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )




# =========================
# ГОНКИ
# =========================


def race_menu():


    keyboard = [

        [

            InlineKeyboardButton(
                "🤖 NPC",
                callback_data="npc"
            )

        ],

        [

            InlineKeyboardButton(
                "👑 Боссы",
                callback_data="boss"
            )

        ],

        [

            InlineKeyboardButton(
                "🌎 PvP",
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
# ПРОФИЛЬ
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
# КАРЬЕРА
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
                "🎫 Боевой пропуск",
                callback_data="battle_pass"
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
# КЕЙСЫ
# =========================


def cases_menu():


    keyboard = [

        [

            InlineKeyboardButton(
                "📦 Обычный",
                callback_data="normal_case"
            )

        ],

        [

            InlineKeyboardButton(
                "💎 Премиум",
                callback_data="premium_case"
            )

        ],

        [

            InlineKeyboardButton(
                "🔥 Легендарный",
                callback_data="legend_case"
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
# АВТОСАЛОН
# =========================


def shop_menu():


    keyboard = [

        [

            InlineKeyboardButton(
                "🚗 Купить машину",
                callback_data="buy_car"
            )

        ],

        [

            InlineKeyboardButton(
                "💎 Эксклюзивы",
                callback_data="exclusive"
            )

        ],

        [

            InlineKeyboardButton(
                "🔄 Рынок",
                callback_data="market"
            )

        ],

        [

            InlineKeyboardButton(
                "🔥 Машина дня",
                callback_data="daily_car"
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
# КЛАН
# =========================


def clan_menu():


    keyboard = [

        [

            InlineKeyboardButton(
                "🏰 Мой клан",
                callback_data="my_clan"
            )

        ],

        [

            InlineKeyboardButton(
                "⚔️ Война кланов",
                callback_data="clan_war"
            )

        ],

        [

            InlineKeyboardButton(
                "🏆 Рейтинг",
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
# СОЦИАЛЬНОЕ
# =========================


def social_menu():


    keyboard = [

        [

            InlineKeyboardButton(
                "👥 Друзья",
                callback_data="friends"
            )

        ],

        [

            InlineKeyboardButton(
                "🎁 Рефералы",
                callback_data="referrals"
            )

        ],

        [

            InlineKeyboardButton(
                "🏆 Рейтинг игроков",
                callback_data="players_rating"
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