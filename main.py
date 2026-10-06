import os
import logging
import threading

from api import run_api
from server import keep_alive


keep_alive()


threading.Thread(
    target=run_api,
    daemon=True
).start()


from telegram.ext import Application
from handlers import setup_handlers




logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)



TOKEN = os.environ.get(

    "BOT_TOKEN"

)




def main():


    if not TOKEN:


        print(

            "❌ BOT_TOKEN отсутствует"

        )

        return



    keep_alive()



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


    main()