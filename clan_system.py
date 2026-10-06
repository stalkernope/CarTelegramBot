import json
import os



CLAN_FILE = "clans.json"




# =========================
# ЗАГРУЗКА
# =========================


def load_clans():

    if not os.path.exists(CLAN_FILE):

        return {}



    try:

        with open(
            CLAN_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_clans(data):

    with open(
        CLAN_FILE,
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
# СОЗДАТЬ КЛАН
# =========================


def create_clan(
    user_id,
    name
):

    clans = load_clans()



    clan_id = str(
        len(clans)+1
    )



    clans[clan_id] = {

        "name": name,

        "owner": user_id,

        "members": [

            user_id

        ],

        "level": 1,

        "xp": 0,

        "wins": 0,

        "rating": 0

    }



    save_clans(
        clans
    )


    return clans[clan_id]




# =========================
# ВСТУПИТЬ
# =========================


def join_clan(
    clan_id,
    user_id
):

    clans = load_clans()



    if clan_id not in clans:

        return False



    clan = clans[clan_id]



    if user_id in clan["members"]:

        return False



    clan["members"].append(

        user_id

    )



    save_clans(
        clans
    )



    return True




# =========================
# НАЙТИ КЛАН ИГРОКА
# =========================


def get_player_clan(
    user_id
):

    clans = load_clans()



    for clan_id, clan in clans.items():


        if user_id in clan["members"]:

            return clan_id, clan



    return None, None




# =========================
# ОПЫТ КЛАНА
# =========================


def add_clan_xp(
    clan_id,
    amount
):

    clans = load_clans()



    if clan_id not in clans:

        return



    clan = clans[clan_id]



    clan["xp"] += amount



    need = clan["level"] * 1000



    if clan["xp"] >= need:


        clan["xp"] -= need

        clan["level"] += 1



    save_clans(
        clans
    )




# =========================
# КЛАНОВЫЙ РЕЙТИНГ
# =========================


def clan_power(clan):


    power = (

        clan["level"] * 1000

        +

        len(clan["members"]) * 100

        +

        clan["wins"] * 50

    )


    return power




# =========================
# ТОП КЛАНОВ
# =========================


def top_clans(limit=10):

    clans = load_clans()



    result = []



    for clan_id, clan in clans.items():


        result.append(

            {

                "name":

                clan["name"],


                "level":

                clan["level"],


                "members":

                len(
                    clan["members"]
                ),


                "power":

                clan_power(
                    clan
                )

            }

        )



    result.sort(

        key=lambda x:

        x["power"],

        reverse=True

    )



    return result[:limit]




# =========================
# ТЕКСТ
# =========================


def clan_text(
    user_id
):

    clan_id, clan = get_player_clan(
        user_id
    )


    if not clan:

        return (

            "❌ Ты не состоишь в автоклубе"

        )



    return (

        "🏎 <b>AUTO CLUB</b>\n\n"

        f"🔥 Название: {clan['name']}\n"

        f"⭐ Уровень: {clan['level']}\n"

        f"⚡ Опыт: {clan['xp']}\n"

        f"👥 Участники: {len(clan['members'])}\n"

        f"🏆 Победы клуба: {clan['wins']}"

    )
    
    # =========================
# CLAN SYSTEM FIX
# =========================


from database import get_player






# =========================
# CLAN TEXT
# =========================


def clan_text(user_id):


    player = get_player(

        user_id

    )


    clan = player.get(

        "clan"

    )



    text = (

        "⚔️ <b>КЛАНЫ</b>\n\n"

    )



    if not clan:


        text += (

            "❌ Ты не состоишь в клане\n\n"

            "Создай клан или вступи в существующий."

        )


        return text





    text += (

        f"🏰 Клан: {clan}\n\n"

        "🔥 Участие в войнах\n"

        "🏆 Рейтинг кланов"

    )



    return text







# =========================
# TOP CLANS
# =========================


def top_clans():


    return [

        {

            "name": "🔥 Night Racers",

            "level": 10,

            "power": 9500

        },


        {

            "name": "⚡ Speed Demons",

            "level": 8,

            "power": 7200

        },


        {

            "name": "🏎 Street Kings",

            "level": 6,

            "power": 5000

        }

    ]