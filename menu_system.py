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
                "🚗 Гараж",
                callback_data="garage"
            ),

            InlineKeyboardButton(
                "🏁 Гонки",
                callback_data="race"
            )

        ],


        [

            InlineKeyboardButton(
                "👤 Профиль",
                callback_data="profile"
            ),

            InlineKeyboardButton(
                "🎁 Кейсы",
                callback_data="cases"
            )

        ],


        [

            InlineKeyboardButton(
                "🛒 Автосалон",
                callback_data="shop"
            )

        ],


        [

            InlineKeyboardButton(
                "⚔️ Клан",
                callback_data="clan"
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
                "🚗 Машины",
                callback_data="cars"
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
                "👑 Босс",
                callback_data="boss"
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
                "⚔️ Война",
                callback_data="clan_war"
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
                "📦 Открыть обычный",
                callback_data="open_normal_case"
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
# МАГАЗИН
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
                "⬅️ Назад",
                callback_data="back"
            )

        ]

    ]


    return InlineKeyboardMarkup(

        keyboard

    )