import os
import logging
import threading


from api import run_api


from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler
)


from handlers import (
    setup_handlers
)





# =========================
# LOGS
# =========================


logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)





TOKEN = os.environ.get(

    "BOT_TOKEN"

)






# =========================
# MINI APP SERVER
# =========================


threading.Thread(

    target=run_api,

    daemon=True

).start()






# =========================
# START BOT
# =========================


def main():


    if not TOKEN:


        print(

            "❌ BOT_TOKEN отсутствует"

        )

        return




    app = (

        Application

        .builder()

        .token(TOKEN)

        .build()

    )





    setup_handlers(

        app

    )






    print(

        "🏎 CAR LEGENDS запущен!"

    )






    app.run_polling()







if __name__ == "__main__":


    try:


        main()



    except Exception as e:


        logging.exception(

            e

        )