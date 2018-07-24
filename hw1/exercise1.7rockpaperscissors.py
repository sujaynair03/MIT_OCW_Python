from random import randint
opt = ["Rock", "Paper", "Scissors"]
opponent = opt[randint(0,2)]
player = raw_input("Rock, Paper, or Scissors?: ")
if player == opponent:
    print("Tie!")
elif player == "Rock":
    if opponent == "Paper":
        print("You lose!")
    else:
        print("You win!")
elif player == "Paper":
    if opponent == "Scissors":
        print("You lose!")
    else:
        print("You win!")
elif player == "Scissors":
    if opponent == "Rock":
        print("You lose!")
    else:
        print("You win!")