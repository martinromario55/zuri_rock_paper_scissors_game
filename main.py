# Rock - Paper - Scissors Logic: Rock beats Scissors, Scissors beat Paper, Paper beats Rock
# r > s, s > p, p > r

import random

while True:    

    def play():
        user = input("What's your choice? 'R' for rock, 'P', for paper, 'S' for scissors\n>>>> ").upper()
        computer = random.choice(['Rock', 'Paper', 'Scissors'])

        if user == 'R':
            user = 'Rock'
        elif user == 'P':
            user = 'Paper'
        elif user == 'S':
            user = 'Scissors'
        else: user = None

        if user == computer:
            return f"****** It's a tie! ********\nPlayer ({user}) : CPU ({computer})\n"

        if is_win(user, computer):
            return f'******** You won! ********\nPlayer ({user}) : CPU ({computer})\n'

        return f'********* You lost! ********\nPlayer ({user}) : CPU ({computer})\n'

    def is_win(player, opponent):
        # return true if player wins
        # r > s, s > p, p > r
        if (player == 'Rock' and opponent == 'Scissors') or (player == 'Scissors' and opponent == 'Paper') or (player == 'Paper' and opponent == 'Rock'):
            return True

    

    print(play())