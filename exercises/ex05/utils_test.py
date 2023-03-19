"""Tests for the utils file."""

__author__ = "730308740"


from exercises.ex05.utils import only_evens, sub, concat


def test_empty() -> None: 
    """Tests to see if only evens returns an empty list when given an empty list."""
    test_list1: list[int] = []
    assert only_evens(test_list1) == [] 


def test_some_evens() -> None: 
    """Tests to see if only evens returns the evens when given all sorts of stuff.""" 
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_no_evens() -> None: 
    """Tests to see if only evens returns nothing when presented with only odds.""" 
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == [] 


def test_empty_cat() -> None: 
    """Tests to see if concat returns an empty list when given an empty list as an argument."""
    test_list1: list[int] = [] 
    assert concat(test_list1, test_list1) == []


def test_same_length() -> None: 
    """Tests to see if concat can concatenate in the right order."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]


def test_diff_length() -> None: 
    """Tests to see if concat still works even when one list is longer than the other."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6, 7]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6, 7]


def test_neg() -> None: 
    """Tests to see if sub can create a sublist which starts at index 0 when the starting index is less than zero."""
    test_list: list[int] = [1, 7, 3, 88, 5]
    assert sub(test_list, -35, 4) == [1, 7, 3, 88]


def test_over() -> None: 
    """Tests to see if sub can create a sublist that ends at the last index when given a very high index.""" 
    test_list: list[int] = [1, 7, 3, 88, 5, 12]
    assert sub(test_list, 4, 1000) == [5, 12]


def test_wrong_order() -> None: 
    """Tests to see if sub returns a blank list when the indexes are given in the wrong order.""" 
    test_list: list[int] = [1, 7, 3, 88, 5, 12]
    assert sub(test_list, 1000, 4) == []


def test_simple() -> None: 
    """Tests to see if sub actually produces the correct sublist when given reasonable indices."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, 1, 4) == [2, 3, 4]