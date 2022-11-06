import random

user_score = 0
computer_score = 0
picks = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock, Paper, or Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in picks:
        print("Pick an option. ")
        continue

    random_number = random.randint(0, 2)
    computer_input = picks[random_number]
    print("The computer chose", computer_input)

    if user_input == "rock" and computer_input == "scissors":
        user_score += 1
        print("You won! Rock beats scissors.")

    elif user_input == "paper" and computer_input == "rock":
        user_score += 1
        print("You won! Paper beats rock.")

    elif user_input == "scissors" and computer_input == "paper":
        user_score += 1
        print("You won! Scissors beats Paper.")

    elif user_input == computer_input:
        print("It's a draw, try again!")

    else:
        computer_score += 1
        print("Computer won")

print("You have", user_score, "wins.")
print("The computer has", computer_score, "wins.")
    







