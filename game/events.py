import random

def random_event(player):
    events = [
        find_trap,
        find_treasure,
        mysterious_vision
    ]
    return random.choice(events)(player)

def find_trap(player):
    damage = random.randint(5, 15)
    player.take_damage(damage)
    return f"A hidden trap triggers! You lose {damage} HP."

def find_treasure(player):
    treasure = random.choice(["Potion", "Gold Coin", "Ancient Scroll"])
    player.add_item(treasure)
    return f"You discover a hidden chest containing a {treasure}."

def mysterious_vision(player):
    player.set_flag("vision_seen")
    return "You are engulfed by a blinding light. A voice whispers a forgotten name..."
