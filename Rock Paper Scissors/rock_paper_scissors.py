import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0 is rock, 1 is paper, 2 is scissors
    # Computers choice
    computers_answer = options[random_number]
    print("Computer Picked", computers_answer + ".")

    if user_input == "rock" and computers_answer == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computers_answer == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computers_answer == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won,", user_wins, "times")
print("The Computer won,", computer_wins, "times")
print("Goodbye!")