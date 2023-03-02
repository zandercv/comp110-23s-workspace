"""New utility functions to use with lists."""

__author__ = "730308740"

def only_evens(input_list: list[int]) -> list[int]: 
    #She'll give ya only the evens in your list. 
    evens: list[int] = []
    #this makes a new list called evens
    for value in input_list: 
        #we're here for each value in the list
        if value % 2 == 0: 
            #we're here if the value was even 
            evens.append(value)
            #add it to the evens list, then go get a new item from the list (back to top of loop)
    return evens 


def concat(list1: list[int], list2: list[int]) -> list[int]: 
    # this bad boy puts list 2 at the back of list one
    for num in list2: 
        list1.append(num) 
        #add each item in list two to the end of list 1
    return list1 

def sub(numbers: list[int], start_idx: int, end_idx: int) -> list[int]:
    idx = start_idx 
    #needed an index because i couldn't figure out how to do it with a for loop 
    sub_list: list[int] = [] 
    #creates a sub list which will be added to and returned
    if idx < 0: 
        #if the start_idx was lower than 0, we just make it zero and start from there 
        idx = 0 
    

    if end_idx > len(numbers): 
        #if the end index given is too high, we just make it one more than the last intdex in the list. 
        end_idx = len(numbers)

    while idx < end_idx: 
        #for each index between the start and end index
        sub_list.append(numbers[idx])
        #tack 'em on to the new list
        idx += 1 
        #also iterate lest you want an infinite loop 
    return sub_list

