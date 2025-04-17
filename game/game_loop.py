from game.player import Player
from game.enemy import generate_random_enemy
from game.events import random_event
from game.dungeon_generator import generate_dungeon, print_dungeon
from game.state_manager import save_game, load_game
from ai.dungeon_master import narrate_event
from interface.ascii_renderer import render_scene


def start_game():
    print("Welcome to the ASCII Dungeon Crawler!")
    choice = input("Load game? (y/n): ").lower()

    if choice == 'y':
        player, dungeon = load_game(Player)
        if not player:
            print("No save file found. Starting new game.")
            player_name = input("Enter your name: ")
            player = Player(player_name)
            dungeon = generate_dungeon()
    else:
        player_name = input("Enter your name: ")
        player = Player(player_name)
        dungeon = generate_dungeon()

    print(narrate_event("You awaken at the entrance of a forgotten dungeon.", "Prepare yourself."))

    while player.is_alive():
        print_dungeon(dungeon)
        render_scene(player)
        move = input("Move (up/down/left/right) or (save/quit): ").lower()

        if move in ['up', 'down', 'left', 'right']:
            player.move(move)
            event_result = random_event(player)
            print(event_result)

            if not player.is_alive():
                print("You have perished in the dungeon...")
                break

            # Enemy encounter
            if random.random() < 0.3:
                enemy = generate_random_enemy()
                print(f"You encounter a {enemy.name}!")
                while enemy.is_alive() and player.is_alive():
                    action = input("Fight (f) or Flee (fl): ").lower()
                    if action == 'f':
                        enemy.take_damage(player.attack)
                        if enemy.is_alive():
                            damage = enemy.attack_player(player)
                            print(f"The {enemy.name} hits you for {damage} damage!")
                        else:
                            print(f"You have defeated the {enemy.name}!")
                    elif action == 'fl':
                        print("You fled successfully!")
                        break
                    else:
                        print("Invalid input.")

        elif move == 'save':
            save_game(player, dungeon)
            print("Game saved!")
        elif move == 'quit':
            confirm = input("Are you sure you want to quit? (y/n): ").lower()
            if confirm == 'y':
                save_game(player, dungeon)
                print("Game saved. Goodbye!")
                break
        else:
            print("Invalid input.")
