from guess_the_word import choose_word, WORDS, process_guess, initialize_game

def test_word_selection():
    # make sure the word picked is actually from the list
    word = choose_word()
    assert word in WORDS

    def test_process_guess_correct():
        game = initialize_game("coffee")
        result = process_guess(game, "o")

        assert result is True
        assert game["display"] == ["_", "o", "_", "_", "_", "_"]
        assert game["attempts_left"] == 6
