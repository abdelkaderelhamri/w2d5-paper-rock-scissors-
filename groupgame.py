import random

computer_choices =["rock", "paper", "scissors"]

while True:
    player_choice = input("Enter your choice(rock, paper, scissors), or 'Q' to end the game: ")
    computer_choice = random.choice(computer_choices)
    print (computer_choice) 
    if player_choice == 'q':
        print("Thanks for playing")
        break

    if player_choice not in computer_choices:
        print("invalid choice. please type rock, paper, or scissor.")
        continue
    

    if player_choice == computer_choice:
        print("game tied")
    elif player_choice == "rock" and computer_choice == "paper":
        print("you lose")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("you win")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("you lose")
    elif player_choice == "paper" and computer_choice == "rock":
        print("you win")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("you lose")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("you win")
        
    
