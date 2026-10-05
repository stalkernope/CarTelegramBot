from database import (
    get_player,
    update_player
)



# =========================
# ЛИГИ
# =========================


LEAGUES = [

    {
        "name": "🥉 Bronze",
        "rep": 0
    },

    {
        "name": "🥈 Silver",
        "rep": 1000
    },

    {
        "name": "🥇 Gold",
        "rep": 3000
    },

    {
        "name": "💎 Diamond",
        "rep": 7000
    },

    {
        "name": "🔥 Legend",
        "rep": 15000
    },

    {
        "name": "👑 Immortal",
        "rep": 30000
    }

]




# =========================
# ТИТУЛЫ
# =========================


TITLES = [

    {
        "name": "Новичок",
        "wins": 0
    },

    {
        "name": "Гонщик",
        "wins": 10
    },

    {
        "name": "Профессионал",
        "wins": 50
    },

    {
        "name": "Легенда трассы",
        "wins": 100
    },

    {
        "name": "Король машин",
        "wins": 250
    },

    {
        "name": "Автомобильный бог",
        "wins": 500
    }

]




# =========================
# ОБНОВЛЕНИЕ ЛИГИ
# =========================


def update_league(user_id):

    player = get_player(
        user_id
    )


    current = "🥉 Bronze"



    for league in LEAGUES:

        if player["rep"] >= league["rep"]:

            current = league["name"]



    player["league"] = current



    update_player(

        user_id,

        player

    )



    return current




# =========================
# ОБНОВЛЕНИЕ ТИТУЛА
# =========================


def update_title(user_id):

    player = get_player(
        user_id
    )


    title = "Новичок"



    for item in TITLES:

        if player["wins"] >= item["wins"]:

            title = item["name"]



    player["title"] = title



    update_player(

        user_id,

        player

    )



    return title




# =========================
# ОБЩИЙ АПГРЕЙД
# =========================


def refresh_player(user_id):

    league = update_league(
        user_id
    )


    title = update_title(
        user_id
    )


    return {

        "league": league,

        "title": title

    }




# =========================
# РЕЙТИНГ ИГРОКА
# =========================


def player_rating(player):


    rating = (

        player["wins"] * 50

        +

        player["level"] * 100

        +

        player["rep"]

    )



    return rating




# =========================
# КАРТОЧКА ИГРОКА
# =========================


def player_card(user_id):

    player = get_player(
        user_id
    )


    refresh_player(
        user_id
    )


    return (

        "👤 <b>CAR LEGENDS PROFILE</b>\n\n"

        f"👑 Титул: {player['title']}\n"

        f"🏆 Лига: {player['league']}\n\n"

        f"⭐ Уровень: {player['level']}\n"

        f"🔥 XP: {player['xp']}\n"

        f"⭐ Репутация: {player['rep']}\n\n"

        f"⚔️ Победы: {player['wins']}\n"

        f"❌ Поражения: {player['losses']}\n"

        f"🔥 Серия: {player['win_streak']}\n\n"

        f"🚗 Машин: {len(player['garage'])}\n"

        f"📊 Рейтинг: {player_rating(player)}"

    )