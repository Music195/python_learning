import random

print ("Welcome to Rock, Paper, Scissors!")
print ("You will play against the computer.")
print ("The rules are simple:")
print ("Rock crushes scissors, scissors cut paper, and paper covers rock.")
print ("Let's begin!")


def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices




def check_winner(player, computer):
        print(f"You chose {player}, Computer chose {computer}.")
        print ("Now let's see who wins!")
        if player == computer:
            return "It's a tie!"
        elif player == "rock":
            if computer == "scissors":
                return "Rock crushes scissors!\nYou win!"
            else:
                return "Paper covers rock!\nYou lose!"
        elif player == "paper":
            if computer == "rock":
                return "Paper covers rock!\nYou win!"
            else: 
                return "Scissors cut paper!\nYou lose!"
        elif player == "scissors":
            if computer == "paper":
                return "Scissors cut paper!\nYou win!"
            else:
                return "Rock crushes scissors!\nYou lose!"



choices = get_choices()
result = check_winner(choices["player"], choices["computer"])
print(f"Since you chose {choices['player']}, Computer chose {choices['computer']} and ......")# calling the values of choices of player and computer
print(result)
