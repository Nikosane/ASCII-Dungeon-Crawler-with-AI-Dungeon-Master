import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek"

def generate_story(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "[No response from AI]")
    except requests.exceptions.RequestException as e:
        return f"[AI Error: {e}]"

def narrate_event(context: str, player_action: str) -> str:
    prompt = f"""
You are a Dungeon Master narrating a dark fantasy RPG. Based on the context and the player's action, describe what happens next.

Context:
{context}

Player Action:
{player_action}

Narration:
"""
    return generate_story(prompt.strip())
