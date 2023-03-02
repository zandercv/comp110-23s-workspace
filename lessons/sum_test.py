"""This tests sum, which sums a list."""

from lessons.sum import sum_idx 

def test_empty() -> None: 
    assert sum([]) == 0.0

def test_one_element() -> None: 
    test_list: list[float] = [1.0] 
    assert sum(test_list) == 1.0 

def test_many() -> None: 
    test_list: list[float] = [1.0, 2.0, 4.0] 
    assert sum(test_list) == 7.0 

def test_many_with_negatives() -> None: 
    test_list: list[float] = [-1.0, 2.0, -1.0]
    assert sum(test_list) == 0.0 