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

                "🏆 Рейтинг",

                callback_data="rating"

            )

        ],


        [

            InlineKeyboardButton(

                "🛒 Магазин",

                callback_data="shop"

            ),

            InlineKeyboardButton(

                "🌍 Карта",

                callback_data="world"

            )

        ],


        [

            InlineKeyboardButton(

                "⚔️ Клан",

                callback_data="clan"

            ),

            InlineKeyboardButton(

                "🎁 Награды",

                callback_data="reward"

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

                "⚙️ Тюнинг",

                callback_data="tuning"

            )

        ],


        [

            InlineKeyboardButton(

                "🎨 Кастом",

                callback_data="custom"

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

                "🤖 NPC гонка",

                callback_data="npc_race"

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

                "🏆 Чемпионат",

                callback_data="champ"

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

                "🏅 Титулы",

                callback_data="titles"

            )

        ],


        [

            InlineKeyboardButton(

                "🎟 Battle Pass",

                callback_data="pass"

            )

        ],


        [

            InlineKeyboardButton(

                "🎁 Ежедневный бонус",

                callback_data="daily"

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

                "⚔️ Война",

                callback_data="clan_war"

            )

        ],


        [

            InlineKeyboardButton(

                "👥 Участники",

                callback_data="members"

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