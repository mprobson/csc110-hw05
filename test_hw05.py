from unittest.mock import patch
import pytest
import hw05_main  # Import the module here
import sys

# Global
text = "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain."
word_list = text.split()

# Part 1
# ===========
def test_1_1_get_user_word_more_than_one(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["two words", "fear", "should_not_read_this_input"]) as mock_input:
        result = hw05_main.get_user_word()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "Error: You provided more than one word"
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1
    hint2 = f"\n\n *** Did your loop break after a successful word was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 2, hint2
    hint3 = f"\n\n *** Did your code return the correct word?"
    assert result == "fear", hint3

def test_1_2_get_user_word_more_than_one_does_not_continue(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["two words", "fear", "should_not_read_this_input"]) as mock_input:
        result = hw05_main.get_user_word()
    hint2 = f"\n\n *** Did your loop break after a successful word was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 2, hint2


def test_1_3_get_user_word_word_too_short(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["do", "fear", "should_not_read_this_input"]) as mock_input:
        result = hw05_main.get_user_word()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "Error: The word is too short"
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1



def test_1_4_get_user_word_word_too_short_does_not_continue(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["do", "fear", "should_not_read_this_input"]) as mock_input:
        result = hw05_main.get_user_word()
    hint2 = f"\n\n *** Did your loop break after a successful word was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 2, hint2


def test_1_5_get_user_word_does_not_return_correct_word(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["do", "fear", "should_not_read_this_input"]) as mock_input:
        result = hw05_main.get_user_word()
    hint3 = f"\n\n *** Did your code return the correct word?"
    assert result == "fear", hint3


# Part 2
# ===========
def test_2_1_count_in_text_for_the_word_not(capsys, monkeypatch):
    result = hw05_main.count_in_text("not", word_list)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "The word 'not' is found 2 times in the text"
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1


def test_2_2_count_in_text_for_the_word_fear(capsys, monkeypatch):
    result = hw05_main.count_in_text("fear", word_list)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "The word 'fear' is found 3 times in the text"
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1


def test_2_3_count_in_text_for_the_word_cat(capsys, monkeypatch):
    result = hw05_main.count_in_text("cat", word_list)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "The word 'cat' is found 0 times in the text"
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1
