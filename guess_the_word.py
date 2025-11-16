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

def process_guess(game, letter):
    letter = letter.lower()

    # If the player already guessed this letter, do nothing
    if letter in game["wrong_letters"] or letter in game["display"]:
        return False

    # If the letter is in the word, show it
    if letter in game["word"]:
        for i, char in enumerate(game["word"]):
            if char == letter:
                game["display"][i] = letter
        return True
    else:
        # Wrong guess
        game["wrong_letters"].add(letter)
        game["attempts_left"] -= 1
        return False
