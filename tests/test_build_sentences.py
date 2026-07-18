import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)

def test_get_seven_letter_word(mocker):
    # Mock the input function
    mock_input = mocker.patch("builtins.input", return_value="testing")

    # Call the function under test
    result = get_seven_letter_word()

    # Assert the result
    assert result == "TESTING"

    # Verify input() was called correctly
    mock_input.assert_called_once_with("Please enter a word with at least 7 letters: ")

    # Mock a short word
    mocker.patch("builtins.input", return_value="test")

    # Verify the exception is raised
    with pytest.raises(ValueError):
        get_seven_letter_word()

def test_parse_json_from_file():
    pass

def test_choose_sentence_structure():
    pass

def test_get_pronoun():
    pass

def test_get_article():
    pass

def test_get_word():
    pass

def test_fix_agreement():
    pass

def test_build_sentence():
    pass