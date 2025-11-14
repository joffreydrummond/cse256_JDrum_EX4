import random

# Simple set of words for the game
WORDS = ["coffee", "backpack", "notebook", "python", "sunshine", "weekend"]

def choose_word():
    return random.choice(WORDS)

def initialize_game(word):
    # Track the letters guessed so far and incorrect guesses
    return {
        "word": word,
        "display": ["_"] * len(word),
        "attempts_left": 6,
        "wrong_letters": set()
    }
