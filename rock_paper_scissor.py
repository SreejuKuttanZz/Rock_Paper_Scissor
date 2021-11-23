import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_insert = input("Type Rock/Paper/Scissors or Quit : ").lower()

    if user_insert == "q":
        break
    if user_insert not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_insert == "rock" and computer_pick == "scissors":
        print("You got it...!")
        user_wins += 1
    elif user_insert == "paper" and computer_pick == "rock":
        print("You got it...!")
        user_wins += 1
    elif user_insert == "scissors" and computer_pick == "paper":
        print("You got it...!")
        user_wins += 1
    else:
        print("You got Wrong...!")
        computer_wins += 1
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Good Bye..!")
