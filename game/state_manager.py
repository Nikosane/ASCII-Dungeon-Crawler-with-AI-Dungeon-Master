import json
import os

SAVE_FILE = "data/savegame.json"

def save_game(player, dungeon):
    data = {
        "player": {
            "name": player.name,
            "hp": player.hp,
            "attack": player.attack,
            "defense": player.defense,
            "inventory": player.inventory,
            "position": player.position,
            "story_flags": player.story_flags
        },
        "dungeon": dungeon
    }

    os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_game(PlayerClass):
    if not os.path.exists(SAVE_FILE):
        return None, None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    player_data = data["player"]
    player = PlayerClass(player_data["name"])
    player.hp = player_data["hp"]
    player.attack = player_data["attack"]
    player.defense = player_data["defense"]
    player.inventory = player_data["inventory"]
    player.position = tuple(player_data["position"])
    player.story_flags = player_data["story_flags"]

    dungeon = data["dungeon"]
    return player, dungeon
