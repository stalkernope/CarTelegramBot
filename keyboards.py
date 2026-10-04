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
                "🔥 Машина дня",
                callback_data="daily"
            ),

            InlineKeyboardButton(
                "⚔️ Битва машин",
                callback_data="battle"
            )

        ],


        [

            InlineKeyboardButton(
                "🎲 Моя машина",
                callback_data="match"
            ),

            InlineKeyboardButton(
                "🎁 Открыть кейс",
                callback_data="case"
            )

        ],


        [

            InlineKeyboardButton(
                "🏆 Мой гараж",
                callback_data="garage"
            ),

            InlineKeyboardButton(
                "🛒 Магазин",
                callback_data="shop"
            )

        ],


        [

            InlineKeyboardButton(
                "👤 Профиль",
                callback_data="profile"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )





# =========================
# НАЗАД
# =========================


def back_button():


    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "⬅️ Назад",

                    callback_data="menu"

                )

            ]

        ]

    )