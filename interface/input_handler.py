def get_player_input():
    command = input("Enter your action: ").strip().lower()
    return command


def parse_command(command):
    if command in ["up", "down", "left", "right", "save", "quit", "f", "fl"]:
        return command
    else:
        return None
