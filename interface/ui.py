def display_message(message):
    print("\n" + "=" * 40)
    print(message)
    print("=" * 40 + "\n")


def display_stats(player):
    print("Player Stats:")
    print(f"Name: {player.name}")
    print(f"HP: {player.hp}")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print(f"Inventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")
    print(f"Position: {player.position}")
    print("-" * 40)
