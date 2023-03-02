"""New utility functions to use with lists."""

__author__ = "730308740"

def only_evens(input_list: list[int]) -> list[int]: 
    evens: list[int] = []
    for value in input_list: 
        if value % 2 == 0: 
            evens.append(value) 
    return evens 

