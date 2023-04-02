"""This wil have some basic functions of dictionaries."""


__author__ = "730308740"


def invert(my_dict: dict[str, str]) -> dict[str, str]: 
    """Makes Keys Values and Values Keys."""
    tcid: dict[str, str] = dict() 
    # It's called tcid because its a backwards dict. 
    for key_a in my_dict: 
        # This double for loop will raise a key error if two of the values are the same. 
        # Key_a will hold a key to be compared to the other keys. 
        for key_b in my_dict: 
            # This cycles through the other keys. 
            if key_a != key_b and my_dict[key_a] == my_dict[key_b]: 
                # If the key isn't the same (just talking about the exact same value), than 
                raise KeyError("Cannot Create a Dictionary with overlapping Keys.")

    for key in my_dict: 
        # This takes each value in my_dict and declares it a Key in tcid. Then it assigns the value that was previously the Key
        tcid[my_dict[key]] = key 
    return tcid


def favorite_color(my_dict: dict[str, str]) -> str: 
    """Reports the color most frequently names as favorite color."""
    color_scores: dict[str, int] = dict() 
    unique_colors: list[str] = list()
    winning_color: str = ""
    winning_color_score: int = 0
    for person in my_dict: 
        # Ok so this whole thing is me unnescesarily looping because I didn't know about the "in" key word
        # It compares colors in the dict to colors in a new list and adds them if they aren't already there. 
        need_to_add: bool = True 
        for color in unique_colors: 
            if my_dict[person] == color: 
                need_to_add = False
        if need_to_add: 
            unique_colors.append(my_dict[person])
    for color in unique_colors: 
        # this uses the list of unique colors to build a dictionary with keys as colors and values as the number of reports they received. 
        color_scores[color] = 1
        for person in my_dict: 
            if color == my_dict[person]: 
                color_scores[color] += 1 
    for color in color_scores: 
        # This establishes a color with the most reports based on the color_scores dictionary. 
        if color_scores[color] > winning_color_score: 
            winning_color = color 
            winning_color_score = color_scores[color]
    return winning_color


def count(my_list: list[str]) -> dict[str, int]: 
    """Reports the number of times an item in a list appears."""
    counted: dict[str, int] = dict()
    # Creates a dictionary to hold unique values and the amount of times they are reported.
    for value in my_list: 
        if value in counted: 
            # For values that are already imported, increase their count. 
            counted[value] += 1 
        else: 
            counted[value] = 1 
            # For new values, start a count by putting them in the dictionary
    return counted


if __name__ == "__main__": 
    test_list: list[str] = ["grape", "grape", "grape"]
    print(count(test_list))