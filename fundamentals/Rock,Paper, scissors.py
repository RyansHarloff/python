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