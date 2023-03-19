"""This is my create your own adenture and it is the game farkle."""

__author__ = "730308740"

#Globals
still_playing = True
num_dice = 6 
points = 0 
player = ""
GRIMACE_EMOJI = "\U0001F62C"

#Imports 
from random import randint

dice_values: list[int] = [] 
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

def a_single_roll(num_dice: int) -> int:
    global dice_values
    roll(num_dice) 
    dice_left(dice_values)
    return score_roll(dice_values)
    

def round_but_better() -> int: 
    still_playing = True
    round_score = 0
    roll_score = 0
    global num_dice
    global points
    while still_playing: 
        if round_score == 0: 
            player_rdy = input(f"\nYour total score is {points} points, {player}. Ready to start a new round? Y/N ")
            if player_rdy == "N": 
                still_playing = False
            else: 
                roll_score = a_single_roll(num_dice)
                if roll_score == 0: 
                    print(f"You Farkled {player}! Farkin Narts, on the first roll too. Score no points this round.")
                    round_score = 0 
                    still_playing = False
                else: 
                    round_score += roll_score 
        else: 
            player_want_2play = input(f"You have scored {round_score} points this round, {player}. You have {num_dice} to roll. Do you want to roll? Y/N ")
            if player_want_2play == "N" or player_want_2play == "n": 
                still_playing = False 
            else: 
                roll_score = a_single_roll(num_dice)
                if roll_score == 0: 
                    print(f"You Farkled! Score no points this round. {GRIMACE_EMOJI}{GRIMACE_EMOJI}{GRIMACE_EMOJI}")
                    round_score = 0 
                    still_playing = False
                else: 
                    round_score += roll_score
    roll_score = 0 
    num_dice = 6
    return round_score
    
def greet() -> None: 
    global player
    player = input("What is your name? ")
    print(f"\n \nWelcome to the Game of Farkle, {player}!")
    print("In this ~simplified~ version of the game you are rolling dice to try and get the highest score.")
    print("You roll six dice ans score points based on the visible faces of the die.")
    print("1's are worth 100 and 5's are worth 50.")
    print("Dice that score points are set aside and can't be rolled again in this round, but you can roll the remaining dice to score more points!")
    print("But beware, if a roll scores no points, you lose all the points you have accumulated that round!")
    print("BUTT, if all six die score points you are able to reroll all of them.")
    print ("Win the game by reaching 2,000 points. Try to get there in fewer turns than your friends!")

def main(): 
    global player
    global points 
    turns = 1
    greet()

    want_to_play: str = input("\nDo you want to play? Y/N ")
    if want_to_play == "N": 
        print("Lame.")
    else: 
        while points < 500: 
            points += round_but_better()
            turns += 1 
        print(f"\n{player} won the game of Farkle in {turns} turns with {points} points!!! Remember to like, subscribe, and ring that little bell to get a notification whenever I have a Comp110 assignment.")


if __name__ == "__main__": 
    main() 