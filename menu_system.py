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
                "🔧 ТЮНИНГ",
                callback_data="tuning"
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
                callback_data="garage_select"
            )

        ],


        [

            InlineKeyboardButton(
                "🔧 Улучшения",
                callback_data="tuning"
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
# ВЫБОР МАШИНЫ
# =========================


def garage_cars_menu(cars):


    keyboard = []


    for car in cars:


        keyboard.append(

            [

                InlineKeyboardButton(

                    f"👑 {car['name']}",

                    callback_data=

                    f"set_main_{car.get('id')}"

                )

            ]

        )


        keyboard.append(

            [

                InlineKeyboardButton(

                    f"🔧 Улучшить",

                    callback_data=

                    f"upgrade_{car.get('id')}"

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
                "👑 БОСС",
                callback_data="boss"
            )

        ],


        [

            InlineKeyboardButton(
                "🌎 Онлайн",
                callback_data="online"
            )

        ],


        [

            InlineKeyboardButton(
                "🏆 Чемпионат",
                callback_data="championship"
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
# КЕЙСЫ
# =========================


def cases_menu():


    keyboard = [

        [

            InlineKeyboardButton(

                "📦 Обычный кейс",

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
# АВТОСАЛОН
# =========================


def shop_menu():


    keyboard = [

        [

            InlineKeyboardButton(

                "🚗 Honda Civic",

                callback_data="buy_honda"

            )

        ],


        [

            InlineKeyboardButton(

                "🏎 BMW M3",

                callback_data="buy_bmw"

            )

        ],


        [

            InlineKeyboardButton(

                "🔥 Supra MK5",

                callback_data="buy_supra"

            )

        ],


        [

            InlineKeyboardButton(

                "👑 Bugatti X",

                callback_data="buy_bugatti"

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

                callback_data="clan_members"

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