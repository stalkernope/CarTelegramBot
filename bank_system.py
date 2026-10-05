import json
import os
import time



BANK_FILE = "bank.json"




# =========================
# НАСТРОЙКИ
# =========================


DEPOSIT_RATE = 0.05


LOAN_LIMIT = 500000




# =========================
# ЗАГРУЗКА
# =========================


def load_bank():

    if not os.path.exists(BANK_FILE):

        return {}


    try:

        with open(
            BANK_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_bank(data):

    with open(
        BANK_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )




# =========================
# ПРОФИЛЬ БАНКА
# =========================


def get_bank(user_id):

    data = load_bank()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "balance": 0,

            "deposit": 0,

            "loan": 0,

            "history": []

        }


        save_bank(data)



    return data[uid]




# =========================
# ПОПОЛНЕНИЕ
# =========================


def deposit_money(

    user_id,

    amount

):

    data = load_bank()


    bank = get_bank(

        user_id

    )


    bank["balance"] += amount



    bank["history"].append(

        {

            "type":

            "deposit",

            "amount":

            amount,

            "time":

            time.time()

        }

    )



    data[str(user_id)] = bank


    save_bank(data)



    return bank




# =========================
# СНЯТИЕ
# =========================


def withdraw_money(

    user_id,

    amount

):

    data = load_bank()


    bank = get_bank(

        user_id

    )



    if bank["balance"] < amount:

        return False



    bank["balance"] -= amount



    bank["history"].append(

        {

            "type":

            "withdraw",

            "amount":

            amount,

            "time":

            time.time()

        }

    )



    data[str(user_id)] = bank


    save_bank(data)



    return True




# =========================
# ДЕПОЗИТ
# =========================


def create_deposit(

    user_id,

    amount

):

    data = load_bank()


    bank = get_bank(

        user_id

    )



    if bank["balance"] < amount:

        return False



    bank["balance"] -= amount


    bank["deposit"] += amount



    data[str(user_id)] = bank


    save_bank(data)



    return True




# =========================
# НАЧИСЛЕНИЕ ПРОЦЕНТОВ
# =========================


def add_interest(user_id):

    data = load_bank()


    bank = get_bank(

        user_id

    )



    bonus = int(

        bank["deposit"]

        *

        DEPOSIT_RATE

    )



    bank["deposit"] += bonus



    data[str(user_id)] = bank


    save_bank(data)



    return bonus




# =========================
# КРЕДИТ
# =========================


def take_loan(

    user_id,

    amount

):

    data = load_bank()


    bank = get_bank(

        user_id

    )



    if amount > LOAN_LIMIT:

        return False



    bank["balance"] += amount


    bank["loan"] += amount



    data[str(user_id)] = bank


    save_bank(data)



    return True




# =========================
# ПОГАШЕНИЕ
# =========================


def repay_loan(

    user_id,

    amount

):

    data = load_bank()


    bank = get_bank(

        user_id

    )



    if bank["balance"] < amount:

        return False



    if bank["loan"] <= 0:

        return False



    bank["balance"] -= amount


    bank["loan"] -= amount



    data[str(user_id)] = bank


    save_bank(data)



    return True




# =========================
# ФИНАНСОВЫЙ РЕЙТИНГ
# =========================


def finance_rating(user_id):

    bank = get_bank(

        user_id

    )


    score = 0



    score += bank["deposit"] // 1000

    score -= bank["loan"] // 1000



    if score < 0:

        score = 0



    return score




# =========================
# ТЕКСТ
# =========================


def bank_text(user_id):

    bank = get_bank(

        user_id

    )


    return (

        "🏦 <b>БАНК</b>\n\n"

        f"💰 Баланс: {bank['balance']}\n"

        f"📈 Депозит: {bank['deposit']}\n"

        f"💳 Кредит: {bank['loan']}\n"

        f"⭐ Финансовый рейтинг: "

        f"{finance_rating(user_id)}"

    )