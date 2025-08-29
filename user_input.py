import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")

playerchoice = input("Enter... \n 1 for Rock, \n 2 for Paper, \n 3 for Scissors:\n ")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2 or 3")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + RPS(player).name + ".")
print("Python chose " + RPS(computer).name + ".")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("It's a draw!")
else:
    print("You lose! Python wins!")