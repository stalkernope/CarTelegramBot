from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from config import INSTAGRAM


def main_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🔥 Машина дня",
                callback_data="daily"
            ),

            InlineKeyboardButton(
                "⚔️ Битва легенд",
                callback_data="battle"
            )
        ],


        [
            InlineKeyboardButton(
                "🎲 Мой автомобиль",
                callback_data="match"
            ),

            InlineKeyboardButton(
                "🏆 Мой гараж",
                callback_data="garage"
            )
        ],


        [
            InlineKeyboardButton(
                "👤 Профиль",
                callback_data="profile"
            ),

            InlineKeyboardButton(
                "🌍 Каталог",
                callback_data="catalog"
            )
        ],


        [
            InlineKeyboardButton(
                "📸 Street Spot",
                callback_data="street"
            )
        ],


        [
            InlineKeyboardButton(
                "📷 Instagram",
                url=INSTAGRAM
            )
        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )



def back_button():

    return InlineKeyboardMarkup(

        [[

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="menu"
            )

        ]]

    )