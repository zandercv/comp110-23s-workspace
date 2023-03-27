"""This is my create your own adenture and it is the game farkle."""

__author__ = "730308740"

# Imports 
from random import randint

# Globals
still_playing: bool = True
num_dice: int = 6 
points: int = 0 
player: str = ""
GRIMACE_EMOJI = "\U0001F62C"
dice_values: list[int] = [] 


def roll(number_of_dice: int) -> dict[str, int]: 
    """This function rolls some number of dice."""
    i: int = 1
    global dice_values
    dice_values = [] 
    # This is going to store values in the global variable dice_values, but we have to empty it first because each roll is unique.
    while i <= number_of_dice: 
        # For each die it will add a random integer from 1 to 6 to dice_values.
        dice_values.append(randint(1, 6))
        i += 1 
    dice_values.sort()
    print(dice_values)
    
        
def score_roll(dice_values: list[int]) -> int: 
    """This totals a players score for a round."""
    roll_score: int = 0 
    # Roll_score is a local variable that will be reported back. 
    for die in dice_values: 
        # It goes through and looks at each die in dice_values. 
        if die == 1:
            roll_score += 100 
            # If it is a 1 it adds 100 to roll_score score. 
        elif die == 5: 
            roll_score += 50 
            # if it is a 5 it adds 50 to roll_score. 
    return roll_score


def dice_left(dice_values) -> int: 
    """This reduces the number of dice left to roll by the number of dice that scored points in a roll."""
    global num_dice 
    for die in dice_values: 
        # For each die, if it is a 1 or a 5 reduce the number of die left to roll by one. 
        if die == 1 or die == 5:
            num_dice -= 1 
    if num_dice == 0:
        num_dice = 6 
    return num_dice


def a_single_roll(num_dice: int) -> int:
    """This will roll dice, count the number left, and score the roll."""
    global dice_values
    roll(num_dice)
    # Get die values for however many dice are beign rolled. 
    dice_left(dice_values)
    # Subtract all the scoring dice from the total of dice to roll. 
    return score_roll(dice_values)
    # Score the roll (1's are 100 5's are 50)
    

def round_but_better() -> int: 
    """This handles the meat of the game. The player continues rolling until they have a roll which scores them no points or they decide to end the round. If the end the round before having a non-scoring roll, their total for this round is added to their overall total."""
    still_playing = True
    round_score = 0
    roll_score = 0
    global num_dice
    global points
    while still_playing: 
        if round_score == 0: 
            # Enter this if statement if it is the first roll of a round
            player_rdy = input(f"\nYour total score is {points} points, {player}. Ready to start a new round? Y/N ")
            if player_rdy == "N": 
                still_playing = False
                # If the player doesn't want to play, end the round. 
            else: 
                roll_score = a_single_roll(num_dice)
                # Roll the dice, reduce the number of dice to be rolled, score the role. 
                if roll_score == 0: 
                    print(f"You Farkled {player}! Farkin Narts, on the first roll too. Score no points this round.")
                    round_score = 0 
                    still_playing = False
                    # If the player Farkles, i.e. rolls and scores no points the round is over. 
                else: 
                    round_score += roll_score 
                    # Otherwise increase their round score by the score of that roll. 
        else: 
            # Enter here if it is not the first roll of a round. 
            player_want_2play = input(f"You have scored {round_score} points this round, {player}. You have {num_dice} to roll. Do you want to roll? Y/N ")
            if player_want_2play == "N" or player_want_2play == "n": 
                still_playing = False 
                # Player can exit a round and score their points by saying no here. 
            else: 
                roll_score = a_single_roll(num_dice)
                # Or they can choose to roll. 
                if roll_score == 0: 
                    # If they farkle they are kicked out of the round and score no points. 
                    print(f"You Farkled! Score no points this round. {GRIMACE_EMOJI}{GRIMACE_EMOJI}{GRIMACE_EMOJI}")
                    round_score = 0 
                    still_playing = False
                else: 
                    round_score += roll_score
                    # Otherwise the round continues! 
    roll_score = 0 
    num_dice = 6
    # Reset these or everything breaks. 
    return round_score
    

def greet() -> None: 
    """Take the name of the player and introduce them to the game."""
    global player
    player = input("What is your name? ")
    print(f"\n \nWelcome to the Game of Farkle, {player}!")
    print("In this ~simplified~ version of the game you are rolling dice to try and get the highest score.")
    print("You roll six dice ans score points based on the visible faces of the die.")
    print("1's are worth 100 and 5's are worth 50.")
    print("Dice that score points are set aside and can't be rolled again in this round, but you can roll the remaining dice to score more points!")
    print("But beware, if a roll scores no points, you lose all the points you have accumulated that round!")
    print("BUTT, if all six die score points you are able to reroll all of them.")
    print("Win the game by reaching 2,000 points. Try to get there in fewer turns than your friends!")


def main(): 
    """This runs the whole game!"""
    global player
    global points 
    turns: int = 1
    greet()

    want_to_play: str = input("\nDo you want to play? Y/N ")
    if want_to_play == "N": 
        print("Lame.")
    else: 
        while points < 2000: 
            points += round_but_better()
            turns += 1 
            # Keep playing until the player scores 500 points. Counts each turn so players can do it in as few turns as possible. 
        print(f"\n{player} won the game of Farkle in {turns} turns with {points} points!!! Remember to like, subscribe, and ring that little bell to get a notification whenever I have a Comp110 assignment.")


if __name__ == "__main__": 
    main() 