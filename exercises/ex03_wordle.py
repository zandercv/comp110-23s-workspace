"""This is the whole game and it really works!"""

__author__ = "730308740"

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> bool:
    """Lets you know if that character is in the word."""
    assert len(letter) == 1
    word_idx = 0 
    while word_idx < len(word): 
        # for each letter in the word
        if letter == word[word_idx]: 
            # kick out if the letter matches the current letter we're looking at in the word
            return True 
        word_idx = word_idx + 1
        # otherwise look at a new letter
    #  Kick out if none of the letters are in the word
    return False


def emojified(guess: str, secret: str) -> str: 
    """Turns a secret and a guess into a sequence of emojis.""" 
    assert len(secret) == len(guess)
    emojis: str = ""
    guess_idx: int = 0
    # this is where we'll put our emojis
    while guess_idx < len(guess):
        # for each letter in the guess
        letter: str = guess[guess_idx]
        if contains_char(secret, letter): 
            # for letters that are in the word
            if letter == secret[guess_idx]: 
                # if it is the right spot make a green box
                emojis = emojis + GREEN_BOX
            else: 
                # if it is the wrong spot make a yellow box
                emojis = emojis + YELLOW_BOX
        else: 
            # if not in the word make a white box
            emojis = emojis + WHITE_BOX
        guess_idx = guess_idx + 1 
    return emojis


def input_guess(word_length: int) -> str:
    """This function takes in a guess and makes sure it is the correct length."""
    potential_guess: str = input(f"Enter a {word_length} character word: ")
    # take a guess
    while len(potential_guess) != word_length: 
        # correct to right length
        potential_guess = input(f"That wasn't {word_length} chars! Try again: ")
    return potential_guess 
    # give back the guess


def main() -> None: 
    """The entry point of the program and the main game loop."""
    turn_count: int = 1 
    secret: str = "codes"
    guess: str = "" 

    while turn_count <= 6: 
        print(f"=== Turn {turn_count}/6 ===")
        guess = input_guess(len(secret))
        # define guess using the input guess fuction which takes words that are the same length as the secret
        print(emojified(guess, secret))
        # print emojis corresponding to the letters
        if guess == secret: 
            print(f"You won in {turn_count}/6 turns!")
            turn_count = 7
        else: 
            turn_count = turn_count + 1 
            # iterate guess 
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()