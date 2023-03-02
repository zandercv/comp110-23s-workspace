"""Establishes a few fuctions that are inherent in python to better understand lists."""


__author__ = "730308740"


def all(numbers: list[int], comparison: int) -> bool: 
    """If all the numbers in a list are the same as the comparison value it returns true."""
    length_list: int = len(numbers)
    if length_list == 0: 
        return False
    i = 0 
    while i < length_list: 
        if comparison != numbers[i]: 
            return False
        i += 1   
    return True 
  

def max(max_list: list[int]) -> int: 
    """Gives you the max of a list of numbers."""
    if len(max_list) == 0: 
        raise ValueError("max() arg is an empty list")   

    current_max: int = max_list[0]
    i = 1 
    while i < len(max_list): 
        if current_max < max_list[i]: 
            current_max = max_list[i] 
        i += 1 
    return current_max 


def is_equal(input1: list[int], input2: list[int]) -> bool: 
    """Are the two lists provided totally identical."""
    if len(input1) != len(input2): 
        return False 
     
    i = 0 
    while i < len(input1): 
        if input1[i] != input2[i]: 
            return False 
        i += 1
    return True