"""This is my create your own adenture and it is the game farkle."""

__author__ = "730308740"

still_playing = True
num_dice = 6 
points = 0 
dice_values: list[int] = [] 
NAME = ""
from random import randint
def roll(number_of_dice: int) -> dict[str,int]: 
    """This function rolls some number of dice."""
    i = 1
    global dice_values
    dice_values = []
    while  i <= number_of_dice: 
        dice_values.append(randint(1,6))
        i += 1 
    dice_values.sort()
    print(dice_values)
    

def didja_farkle(dice_values: list[int]) -> bool: 
    """This will tell a player if their roll scored no points and they lost."""
    if didja_roll_a1(dice_values) or didja_roll_a5(dice_values): 
        return False 
    return True

def didja_roll_a1(dice_values: list[int]) -> bool: 
    """This will show if a 1 is included in the rolled dice."""
    if 1 in dice_values: 
        return True
    return False

def didja_roll_a5(dice_values: list[int]) -> bool: 
    """This will show if a 5 was rolled. """
    if 5 in dice_values: 
        return True
    return False

        
def score_roll(dice_values: list[int]) -> int: 
    """This totals a players score for a round."""
    roll_score = 0 
    for die in dice_values: 
        if die == 1:
            roll_score += 100 
        elif die == 5: 
            roll_score += 50 
    return roll_score

def dice_left(dice_values) -> int: 
    global num_dice 
    for die in dice_values: 
        if die == 1 or die == 5:
            num_dice -= 1 
    if num_dice == 0:
        num_dice = 6 
    return num_dice

def a_single_roll(num_dice: int): 
    global dice_values
    roll(num_dice) 
    dice_left(dice_values)
    return score_roll(dice_values)
    

def round_but_better(): 
    still_playing = True
    round_score = 0
    roll_score = 0
    global num_dice
    global points
    while still_playing: 
        if round_score == 0: 
            player_rdy = input(f"{NAME} your total score is {points}. Ready to start a new round? Y/N ")
            if player_rdy == "N": 
                still_playing = False
            else: 
                roll_score = a_single_roll(num_dice)
                if roll_score == 0: 
                    print("You Farkled! Score no points this round.")
                    round_score = 0 
                    still_playing = False
                else: 
                    round_score += roll_score 
        else: 
            player_want_2play = input(f"You have scored {round_score} points this round. You have {num_dice} to roll. Do you want to roll? Y/N ")
            if player_want_2play == "N": 
                still_playing = False 
            else: 
                roll_score = a_single_roll(num_dice)
                if roll_score == 0: 
                    print("You Farkled! Score no points this round.")
                    round_score = 0 
                    still_playing = False
                else: 
                    round_score += roll_score
    roll_score = 0 
    num_dice = 6
    return round_score
    




def main(): 
    NAME = input("What is your name? ")
    print(f"Welcome to the Game of Farkle, {NAME}!")
    print("In this ~simplified~ version of the game you are rolling dice to try and get the highest score.")
    print("You roll six dice ans core points based on the visible faces of the die.")
    print("1's are worth 100 and 5's are worth 50.")
    print("Dice that score points are set aside and can't be rolled again in this round, but you can roll the remaining dice to score more points!")
    print("But beware, if a roll scores no points, you lose all the points you have accumulated that round!")
    print("BUTT, if all six die score points you are able to reroll all of them.")
    print ("The winner is the first player to reach 2,000.")

    global points 
    turns = 1
    while points < 2000: 
        points += round_but_better()
        turns =+1 
    print("f{NAME} won the game of Farkle with {points} points in {turns} turns!!! Remember to like, subscribe, and ring that little bell to get a notification whenever I have a Comp110 assignment.")


if __name__ == "__main__": 
    main() 

