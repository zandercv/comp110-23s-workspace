"""Ex01 -- Chardle - A step Toward Wordle!"""

__author__ = "730308740"

word: str = input("Enter a 5-character word: ")
if len(word) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single Character: ")
if len(letter) != 1: 
    print("Error: Character must be a single character.")
    exit()
appearances: int = 0
print("Searching for " + letter + " in " + word)

if letter == word[0]: 
    print(letter + " found at index 0 ")
    appearances = appearances + 1 
if letter == word[1]: 
    print(letter + " found at index 1 ")
    appearances = appearances + 1 
if letter == word[2]: 
    print(letter + " found at index 2 ")
    appearances = appearances + 1 
if letter == word[3]: 
    print(letter + " found at index 3 ")
    appearances = appearances + 1 
if letter == word[4]: 
    print(letter + " found at index 4 ")
    appearances = appearances + 1 

if appearances == 0: 
    print("No instances of " + letter + " found in " + word) 
else: 
    if appearances == 1: 
        print(str(appearances) + " instance of " + letter + " found in " + word)
    else: 
        print(str(appearances) + " instances of " + letter + " found in " + word)
    