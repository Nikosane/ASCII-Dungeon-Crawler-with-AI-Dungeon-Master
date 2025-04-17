def render_scene(player):
    print("=" * 40)
    print(f"Player: {player.name}")
    print(f"HP: {player.hp}")
    print(f"Inventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")
    print("=" * 40)
