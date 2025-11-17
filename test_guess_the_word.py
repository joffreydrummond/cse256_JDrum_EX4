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

def test_process_guess_incorrect():
    game = initialize_game("coffee")
    result = process_guess(game, "z")  # obviously not in the word coffee

    assert result is False
    assert game["display"] == ["_"] * 6  # nothing revealed
    assert "z" in game["wrong_letters"]
    assert game["attempts_left"] == 5

def test_process_guess_multiple_letters():
    game = initialize_game("weekend")
    result = process_guess(game, "e")

    # 'e' appears 3 times in "weekend"
    assert result is True
    assert game["display"] == ["_", "e", "e", "_", "e", "_", "_"]
    assert game["attempts_left"] == 6  # no penalty on correct guesses
