from random import randint


def flip_player(board):
    while True:
        i = randint(0, 8)
        if board[i] == '-':
            board[i] = 'O'
            break
    return board
