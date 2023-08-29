import random
import time
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

rock = {
  "name": "rock",
  "vs_paper": "You lose!",
  "vs_scissors": "You win!",
}

paper = {
  "name": "paper",
  "vs_scissors": "You lose!",
  "vs_rock": "You win!",
}

scissors = {
  "name": "scissors",
  "vs_rock": "You lose!",
  "vs_paper": "You win!",
}

starting_move = {
  "name": "",
}

moves = [rock, paper, scissors]
player_move = starting_move
play_again = "y"
lost = 0
won = 0
drawn = 0

while play_again == "y" or play_again == "Y":
    clear()
    print("Rock, Paper, Scissors")
    time.sleep(0.7)
    player_selection = input("Choose your move. (R)ock, (P)aper, (S)cissors: ")
    while player_move["name"] == "":
        if player_selection == "r" or player_selection == "R":
            player_move = rock
        elif player_selection == "p" or player_selection == "P":
            player_move = paper
        elif player_selection == "s" or player_selection == "S":
            player_move = scissors
        else:
            player_selection = input("Invalid selection. Choose your move. (R)ock, (P)aper, (S)cissors: ")
    clear()
    time.sleep(0.5)
    print("Rock!")
    time.sleep(0.5)
    print("         Paper!")
    time.sleep(0.5)
    print("                     Scissors!")
    time.sleep(1)
    clear()
    computer_move = random.choice(moves)
    print("You: {}".format(player_move["name"]))
    print("Computer: {}".format(computer_move["name"]))
    print()
    if player_move == computer_move:
        result_to_print = "That's a draw!"
    else:
        result = "vs_{}".format(computer_move["name"])
        result_to_print = player_move[result]
    time.sleep(1.3)
    
    print(result_to_print)
    if "lose" in result_to_print:
        lost += 1
    elif "win" in result_to_print:
        won += 1
    elif "draw" in result_to_print:
        drawn += 1
    time.sleep(0.8)
    print("You lost {} times, won {} times and drawn {} times.".format(lost, won, drawn))
    player_move = starting_move
    time.sleep(1)
    print()
    play_again = input("Game Over. Play again? (y/N) ")
    clear()