import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'

def is_win(player, opponent):
    return (player == "r" and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

# Call the play function to start the game
print(play())

