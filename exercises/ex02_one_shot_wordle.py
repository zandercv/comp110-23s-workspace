"""Gives you one chance to guess a word of any character length!"""

__author__ = "730308740"

# establishes a secret
secret: str = "python"

# asks for a guess
num_secret_letters: str = str(len(secret))
guess: str = input(f"What is your { num_secret_letters }-letter guess? ")

# asks for a new input if guess is incorrect length 
while len(guess) != len(secret): 
    guess = input(f"That was not { num_secret_letters } letters! Try again: ")


# Defining Emoji's 

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Establishes variables used within loops
guess_idx: int = 0 
secret_idx: int = 0
in_word: str = "No"
squares: str = ""

while guess_idx < len(guess): 

    # This stuff looks at one of the letters in the guess 
    while secret_idx < len(secret) and in_word == "No": 

        # This stuff checks the letter in the guess against each letter in the secret. It will stop early if it has already found this letter in the secret
        if guess[guess_idx] == secret[secret_idx]:
            in_word = "Yes"
        secret_idx = secret_idx + 1
    secret_idx = 0

    if in_word == "Yes":
        # If the guess letter is in the secret we will make either a yellow or green box
        if secret[guess_idx] == guess[guess_idx]: 
            # If the letter is in the right place, green box
            squares = f"{squares}{GREEN_BOX}"
        else: 
            # If the letter is not in the right place, yellow box 
            squares = f"{squares}{YELLOW_BOX}"
    else: 
        # If the guess letter is not in the secret we will make a white box 
        squares = f"{squares}{WHITE_BOX}"
    guess_idx = guess_idx + 1 
    in_word = "No"

print(squares)

if secret == guess: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
