import random

user = input('enter choice(rock, paper, scissors):')
actions = ['rock',  'paper', 'scissors']
computer = random.choice(actions)

if user == computer:
    print(f"Both players selected {user_action}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock breaks scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_ == "scissors":
    if computer_ == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock breaks scissors! You lose.")

import random

user = input('enter choice(rock, paper, scissors):')
actions = ['rock',  'paper', 'scissors']
computer = random.choice(actions)
user_score = 0
comp_score = 0

if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock breaks scissors! You win!")
        user_score + 1
    else:
        print("Paper covers rock! You lose.")
        comp_score + 1
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
        user_score + 1
    else:
        print("Scissors cuts paper! You lose.")
        comp_score + 1
elif user_ == "scissors":
    if computer_ == "paper":
        print("Scissors cuts paper! You win!")
        user_score + 1
    else:
        print("Rock breaks scissors! You lose.")
        comp_score + 1


print("User Wins: ",  user_score)
print("Comp Wins: ", comp_score)

if user_score > comp_score:
    print("The user wins the game!")
elif comp_score > user_score:
    print("The computer wins the game!")