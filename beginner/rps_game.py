
import random

## Rock-Paper-Scissor game between player and computer.
# Scissor beats Paper, s > p
# Paper beats Rock, p > r
# Rock beats Scissor, r > s

options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}

def play():
    player = input("What do you bet for? (R)ock, (P)aper or (S)cissor? ").lower()
    if player not in options.keys():
        return "Wrong option. Better luck next time!"
    computer = random.choice(list(options.keys()))
    if player == computer:
        return f"It's a TIE! Both have {options.get(player)}."
    if is_win(player, computer):
        return f"You WON. You have {options.get(player)}, Computer has {options.get(computer)}"
    if is_win(computer, player):
        return f"You LOST. You have {options.get(player)}, Computer has {options.get(computer)}"

def is_win(player, computer):
    return (player == 's' and computer == 'p') or\
           (player == 'p' and computer == 'r') or\
           (player == 'r' and computer == 's')

print(play())