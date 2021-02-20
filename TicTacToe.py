# Tic Tac Toe project, showcasing function programming and logic to play the game

# The Board, a print function that clears previous board by using a bunch of new lines

import random

def display_board(board):
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('- - -')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('- - -')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Player Marker, uses a while loop to make sure I get the correct responses

def player_input():

    player1 = 'nah'
    player2 = ''
    symbol = ['X', 'O']

    while player1 not in symbol:
        player1 = input('Player 1, wanna be "X" or "O"? ')

        if player1 not in symbol:
            print('X or O not chosen, case sensitive and no numbers!')

    # check for what index player1 is at, if == [0] or [1], assign opposite index to player 2

    if player1 == symbol[0]:
        player2 = symbol[1]
    else:
        player2 = symbol[0]

    return (player1, player2)

# Marker Placement

def place_marker(board, marker, position):
    board[position] = marker

# Win Check, takes in board and a player marker to see if that player has won

def win_check(board, mark):

    return ((board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark))

# First Move, randomly chooses

def choose_first():
    decided = random.randint(1, 2)
    return str(decided)

# Space Check, checks if a space a player chooses is actually available to place their marker

def space_check(board, position):
    return board[position] == ' '

# Full Board, used in case of a tie

def full_board_check(board):

    for x in range(1,10):

        if space_check(board,x):
            return False

    return True

# Player Choice, used to ask player where they'd like to place the marker.
# uses space_check function to see if move possible

def player_choice(board):
    choice = 0

    while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, choice):
        choice = int(input('Where do you want to place your marker? Pick 1-9: '))

    return choice

# Replay, play again?

def replay():
    again = ' '
    check = ['YES', 'NO']

    while again not in check:
        again = input('Wanna play again? Case sensitively, type YES or NO: ')

        if again == check[0]:
            return True

# GAME LOGIC #

print('Welcome to Tic Tac Toe!')

while True:

    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    player1, player2 = player_input()
    turn = choose_first()
    print(f'Player {turn} will go first!')

    play_game = input('Ready? Y or N: ').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == '1':

            # Player 1 Turn
            display_board(game_board)

            choice = player_choice(game_board)
            place_marker(game_board, player1, choice)

            if win_check(game_board, player1):
                display_board(game_board)
                print('Player 1 wins!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = '2'

        # Player2's turn.
        else:

            display_board(game_board)

            choice = player_choice(game_board)
            place_marker(game_board, player2, choice)

            if win_check(game_board, player2):
                display_board(game_board)
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = '1'

    if not replay():
        game_on = False
        break
