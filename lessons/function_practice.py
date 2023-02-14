"""This is for practicing functions. """


def mimic(my_words: str) -> str: 
    """Given the string my_words, outputs the same string"""
    return my_words

def mimic_letter(my_words: str, letter_idx: int) -> str: 
    """Give back the letter at that index"""
    if letter_idx >= len(my_words): 
        return ("Too high of an index")
    return my_words[letter_idx]

print(mimic_letter("hi",2))