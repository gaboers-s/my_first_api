import json
from pathlib import Path
import random

data_file = Path(__file__).resolve().parent.parent/"data"/"quotes.json"

def get_all_quotes():
    with open(data_file, "r", encoding="utf-8") as file:
        quotes = json.load(file)

    return quotes

def get_random_quotes():
    all_quotes = get_all_quotes()

    if not all_quotes:
        return None

    return random.choice(all_quotes)