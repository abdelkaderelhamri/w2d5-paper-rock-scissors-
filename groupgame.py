import random

computer_choices =["Rock", "Paper", "Scissors"]

while True:
    computer_choice = random.choice(computer_choices)
    player_choice = input("Enter your choice (Rock, Paper, Scissors), or 'Q' to end the game: ")

    if player_choice.lower() != 'q':
        print (f"\nThe computer chose {computer_choice.lower()} and your choice was {player_choice}.")
    if player_choice.lower() == 'q':
        print("Thanks for playing!")
        break
    elif player_choice.lower() == computer_choice.lower():
        print("Game Tied...boring\n")
    elif player_choice.lower() == "rock" and computer_choice.lower() == "paper":
        print("You Lose :-( \n")
    elif player_choice.lower() == "rock" and computer_choice.lower() == "scissors":
        print("You Win!\n")
    elif player_choice.lower() == "paper" and computer_choice.lower() == "scissors":
        print("You Lose :-(\n")
    elif player_choice.lower() == "paper" and computer_choice.lower() == "rock":
        print("You Win!\n")
    elif player_choice.lower() == "scissors" and computer_choice.lower() == "rock":
        print("You Lose :-(\n")
    elif player_choice.lower() == "scissors" and computer_choice.lower() == "paper":
        print("You Win!\n")
    else: 
        print("Invalid choice. Please type Rock, Paper, or Scissors.\nSince you ruined it, the computer will choose again too.\n")
        continue



        
    
