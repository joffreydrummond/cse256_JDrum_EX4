from guess_the_word import choose_word, WORDS, process_guess, initialize_game

def test_word_selection():
    # make sure the chosen word is actually from the list
    word = choose_word()
    assert word in WORDS