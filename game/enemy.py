import random

class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, amount):
        self.hp -= max(0, amount - self.defense)

    def is_alive(self):
        return self.hp > 0

    def attack_player(self, player):
        damage = random.randint(0, self.attack)
        player.take_damage(damage)
        return damage


def generate_random_enemy():
    enemies = [
        Enemy("Goblin", 30, 5, 2),
        Enemy("Skeleton", 40, 6, 3),
        Enemy("Orc", 50, 8, 4),
        Enemy("Dark Mage", 35, 10, 1)
    ]
    return random.choice(enemies)
