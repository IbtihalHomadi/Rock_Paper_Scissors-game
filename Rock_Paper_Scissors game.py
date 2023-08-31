
"""Write list of choices"""
"""Kinda stupid way to that Game:) """
import random
Counter=0
choices=["rock","paper","scissors"]

"""code for how play works"""
while Counter<6:
    Counter+=1
    player_choice = input("Enter your Choice(rock,paper,scissors)")  
    computer_choice = random.choice(choices)
    if player_choice==computer_choice:
            print("Equals Try again")
    elif player_choice =="rock":
            if computer_choice=="scissors":
                print("you win")
            elif computer_choice== "paper":
                print("ypu Loss")

    elif player_choice == "paper":
            if computer_choice == "rock":
                  print("you win")
            elif computer_choice == "scissors":
                  print("you loss")

    elif player_choice == "scissors":
            if computer_choice == "paper":
                  print ("you win")
            elif computer_choice == "rock":
                  print("you loss")
    else:
          print("Word is not allowed!")


      