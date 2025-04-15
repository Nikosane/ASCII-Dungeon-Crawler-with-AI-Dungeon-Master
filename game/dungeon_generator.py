import random

DUNGEON_WIDTH = 10
DUNGEON_HEIGHT = 10

TILE_EMPTY = '.'
TILE_WALL = '#'
TILE_PLAYER = '@'
TILE_EXIT = 'X'

def generate_dungeon(width=DUNGEON_WIDTH, height=DUNGEON_HEIGHT):
    dungeon = [[TILE_EMPTY for _ in range(width)] for _ in range(height)]

    # Place walls randomly
    for y in range(height):
        for x in range(width):
            if random.random() < 0.2:
                dungeon[y][x] = TILE_WALL

    # Ensure starting and exit points
    start_x, start_y = 0, 0
    exit_x, exit_y = width - 1, height - 1
    dungeon[start_y][start_x] = TILE_PLAYER
    dungeon[exit_y][exit_x] = TILE_EXIT

    return dungeon

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))
