"""Write list of choices"""
import random
Counter=0
choices=["rock","paper","scissors"]

"""code for how play works"""
while Counter<6:
    Counter+=1
    player_choice = input("Enter your Choice(rock,paper,scissors)")  
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print("you are equals")
    elif player_choice== "rock" and computer_choice=="scissors":
        print ("You win")
    elif player_choice == "paper" and computer_choice=="rock":
        print("You win")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You Win")

    else :
        print("you Loss")
        