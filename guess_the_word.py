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

def play_game():
    word = choose_word()
    game = initialize_game(word)

    print("Welcome to Guess the Word! Let's get started.")
    print("I'm thinking of a word with", len(word), "letters.")
    print("You have", game["attempts_left"], "wrong attempts allowed.\n")

    while game["attempts_left"] > 0 and "_" in game["display"]:
        print("Current word:", " ".join(game["display"]))
        print("Wrong letters so far:", ", ".join(sorted(game["wrong_letters"])) or "None")
        guess = input("Guess a letter: ")

        if not guess.isalpha() or len(guess) != 1:
            print("Please guess a single letter.\n")
            continue

        correct = process_guess(game, guess)

        if correct:
            print("Nice! That letter is in the word. Are you psychic?\n")
        else:
            print("Nope! That letter is NOT in the word. Try again.\n")

    if "_" not in game["display"]:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)
