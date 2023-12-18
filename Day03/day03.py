print("Welcome to Treasure Island! Your job is to find the treasure to win!")
choice_1 = input("You come to a crossroads, do you go 'Left' or 'Right'?")
if choice_1 == "Left":
    choice_2 = input("You stumble towards a lake with an island in the middle. Do you 'Swim' or 'Wait' for a boat?")
    if choice_2 == "Wait":
        choice_3 = input("The island has a building with three doors, 'Red', 'Green', and 'Blue' - which do you choose?")
        if choice_3 == "Green":
            print("Congratulations, you've found the treasure and won!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")