def car_card_menu(car_id):

    keyboard = [

        [

            InlineKeyboardButton(
                "🔧 Улучшить",
                callback_data=f"upgrade_{car_id}"
            )

        ],

        [

            InlineKeyboardButton(
                "👑 Сделать главной",
                callback_data=f"set_main_{car_id}"
            )

        ],

        [

            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="garage_select"
            )

        ]

    ]


    return InlineKeyboardMarkup(
        keyboard
    )