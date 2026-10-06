import json
import os


DB_FILE = "players.json"


def load_players():
    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_players(players):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(players, f, indent=4, ensure_ascii=False)


def get_player(player_id):
    players = load_players()

    if str(player_id) not in players:
        players[str(player_id)] = {
            "coins": 0,
            "xp": 0,
            "wins": 0,
            "cars": []
        }
        save_players(players)

    return players[str(player_id)]


def update_player(player_id, data):
    players = load_players()

    players[str(player_id)] = data

    save_players(players)


def add_coins(player_id, amount):
    player = get_player(player_id)

    player["coins"] += amount

    update_player(player_id, player)


def remove_coins(player_id, amount):
    player = get_player(player_id)

    if player["coins"] >= amount:
        player["coins"] -= amount

    update_player(player_id, player)


def add_xp(player_id, amount):
    player = get_player(player_id)

    player["xp"] += amount

    update_player(player_id, player)


def add_win(player_id):
    player = get_player(player_id)

    player["wins"] += 1

    update_player(player_id, player)


def add_car(player_id, car):
    player = get_player(player_id)

    if car not in player["cars"]:
        player["cars"].append(car)

    update_player(player_id, player)


def remove_car(player_id, car):
    player = get_player(player_id)

    if car in player["cars"]:
        player["cars"].remove(car)

    update_player(player_id, player)