# create a rock, paper, scissor game
import random
# from colorama import init, Fore, Style

# init(autoreset=True)
# 3 options to choose from
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors")
while True:
    # add a score
    print(f"Your score: {player_score} | Computer: {computer_score} \n")
    # need to be able to take a users input so they can select
    player = input("Choose either rock, paper, or scissors (or quit): ").lower()

    if player == "quit":
        print("Thanks for playing!")
        print("Final Score")
        print(f"Your score: {player_score} | Computer: {computer_score} \n")
        break

    if player not in choices:
        print("That is not an option. Please choose either rock, paper, or scissors \n")
        continue
    # need to give random choice to computer
    computer = random.choice(choices)
    print("Your opponent chooses: ", computer)
    # create what to do depending on different outcomes

    if player == computer:
        print("Oh - its a tie! \n")
    elif player == "rock" and computer == "scissors":
        print(Fore.GREEN + "You win rockstar! \n")
        player_score +=1
    elif player == "scissors" and computer == "paper":
        print(Fore.GREEN + "You are really cutting down your opponents! You Win!!! \n")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win!!! \n")
        player_score +=1
    else:
        print("haha - you lose! Better luck next time! \n")
        computer_score +=1