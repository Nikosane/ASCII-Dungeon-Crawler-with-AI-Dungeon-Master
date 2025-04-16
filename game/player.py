class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.inventory = []
        self.position = (0, 0)
        self.story_flags = {}

    def move(self, direction):
        x, y = self.position
        if direction == 'up':
            self.position = (x, y - 1)
        elif direction == 'down':
            self.position = (x, y + 1)
        elif direction == 'left':
            self.position = (x - 1, y)
        elif direction == 'right':
            self.position = (x + 1, y)

    def take_damage(self, amount):
        self.hp -= max(0, amount - self.defense)

    def is_alive(self):
        return self.hp > 0

    def add_item(self, item):
        self.inventory.append(item)

    def set_flag(self, key, value=True):
        self.story_flags[key] = value

    def get_flag(self, key):
        return self.story_flags.get(key, False)
