# Predefined prompt templates for various AI-driven situations

def intro_prompt(player_name: str) -> str:
    return f"""
You are a Dungeon Master introducing the player to a procedurally generated dungeon.
Set the tone with a vivid and immersive opening scene.

Player Name: {player_name}

Intro:
"""

def encounter_prompt(context: str, encounter_type: str) -> str:
    return f"""
You are a Dungeon Master narrating a dungeon event.

Context:
{context}

Encounter Type: {encounter_type}

Describe the scene and the challenge that unfolds.
"""

def choice_outcome_prompt(context: str, choice: str) -> str:
    return f"""
You are a Dungeon Master resolving a player's choice in the dungeon.

Context:
{context}

Player's Choice:
{choice}

Narrate what happens as a result.
"""
