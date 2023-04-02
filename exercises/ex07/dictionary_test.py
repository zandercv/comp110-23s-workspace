"""This will test the basic functions develop in exercise 7."""

__author__ = "730308740"

from exercises.ex07.dictionary import invert, favorite_color, count 
import pytest


def test_invert_with_strs() -> None: 
    """When given a dictionary with string keys and string values successfully inverts them."""
    test_dict: dict[str, str] = {"one": "a", "two": "b", "three": "c"} 
    assert invert(test_dict) == {'a': 'one', 'b': 'two', 'c': 'three'} 


def test_invert_whole_words() -> None: 
    """When given a dictionary with string keys and string values successfully inverts them."""
    test_dict: dict[str, str] = {"dog": "cat", "chicken": "egg", "vanila": "chocolate"} 
    assert invert(test_dict) == {'cat': 'dog', 'egg': 'chicken', 'chocolate': 'vanila'} 


def test_key_error() -> None: 
    """When given values that result in a key error, the key error is reported."""
    with pytest.raises(KeyError): 
        test_dict: dict[str, str] = {'Zander': 'Vierling', 'Max': 'Vierling'}
        invert(test_dict)


def test_empty() -> None: 
    """When given an empty dict returns an empty dict."""
    test_dict: dict[str, str] = {} 
    assert invert(test_dict) == {} 


def test_clear_winner() -> None: 
    """When given a dictionary in which one color has the most votes, tests that the function returns that color."""
    test_dict: dict(str, str) = {"Zander": "blue", "Katherine": "pink", "David": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_unclear_winner() -> None:
    """When given a dictionary in which two colors are equally favored, returns the first color entered."""
    test_dict: dict(str, str) = {"Zander": "blue", "Katherine": "pink", "David": "blue", "Violet": "pink"}
    assert favorite_color(test_dict) == "blue"


def test_empty_fav_color() -> None: 
    """When given an empty dictionary, returns a blank ."""
    test_dict: dict(str, str) = {}
    assert favorite_color(test_dict) == ""


def test_count_variety() -> None: 
    """When given a variety of strings counts them appropriately."""
    test_list: list[str] = ["grape", "grape", "grape", "banana", "grape", "orange", "banana"]
    assert count(test_list) == {"grape": 4, "banana": 2, "orange": 1}


def test_count_no_variety() -> None: 
    """When give a string of one thing counts it appropriately."""
    test_list: list[str] = ["grape", "grape", "grape"]
    assert count(test_list) == {"grape": 3}


def test_no_input() -> None: 
    """When given an empty string returns an empty dictionary."""
    test_list: list[str] = list()
    assert count(test_list) == {}