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
                "👑 Выбрать главную машину",
                callback_data="garage_select"
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
# СПИСОК МАШИН
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

                    f"🔧 Улучшить {car['name']}",

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
# ПРОКАЧКА
# =========================


def upgrade_menu(car_id):


    keyboard = [

        [

            InlineKeyboardButton(

                "🔧 Улучшить",

                callback_data=f"upgrade_{car_id}"

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