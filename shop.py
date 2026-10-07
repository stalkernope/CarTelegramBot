# =========================
# SHOP SYSTEM FINAL
# =========================


from case_system import (
    open_case,
    get_cases,
    case_result_text
)





# =========================
# SHOP TEXT
# =========================


def shop_text():


    text = (

        "🛒 <b>МАГАЗИН</b>\n\n"

    )



    for key, case in get_cases().items():


        text += (

            f"🎁 {case['name']}\n"

            f"💰 Цена: {case['price']} "

            f"{case['currency']}\n\n"

        )



    return text







# =========================
# OPEN SHOP CASE
# =========================


def buy_case(

    user_id,

    case_type

):


    car = open_case(

        user_id,

        case_type

    )



    return {


        "success":

        True,


        "car":

        car,


        "text":

        case_result_text(

            car

        )

    }







# =========================
# CASE BUTTONS
# =========================


def available_cases():


    return list(

        get_cases().keys()

    )






# =========================
# SIMPLE CHECK
# =========================


def check_case(

    case_type

):


    cases = get_cases()



    return case_type in cases