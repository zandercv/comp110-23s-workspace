"""Testing the Farkle game."""

from exercises.cyoa import score_roll 

def test_roll_score(): 
    test_list = [1,2,3,4,5,6]
    assert score_roll(test_list) == 150

from exercises.cyoa import dice_left

def test_dice_left(): 
    test_list = [1,1,5,2,2,4]
    num_dice = 6
    assert dice_left(test_list, num_dice) == 3 

def test_dice_restored(): 
    test_list = [1,1,5,5,5,1]
    num_dice = 6
    assert dice_left(test_list, num_dice) == 6

    
