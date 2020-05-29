import singleplayer, multiplayer

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    print("+++++++++++")
    c = 1
    for i in board:
        print(f" {i} ", end='')
        if c % 3 == 0:
            print("\n", end='')
            c = 1
            continue
        print("|", end='')
        c += 1
    print("+++++++++++\n")


def handle_turn():
    while True:
        try:
            if switch == '2':
                print("X's Chance")
            position = int(input("Choose a position for  1 to 9: ")) - 1
        except:
            print("Invalid Input!!!")
        else:
            if 0 <= position < 9:
                if board[position] != 'X' and board[position] != 'O':
                    board[position] = 'X'
                    if switch == '2':
                        display_board()
                else:
                    print("Already Occupied Field")
                    continue
                break
            print("Invalid Input!!!")


def check_if_game_over():
    winner = check_if_win()
    if check_winner(winner):
        return winner
    winner = check_if_tie()
    if winner == "Tie":
        return winner


def check_rows():
    if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == \
            board[8] == 'X':
        return 'X'
    if board[0] == board[1] == board[2] == 'O' or board[3] == board[4] == board[5] == 'O' or board[6] == board[7] == \
            board[8] == 'O':
        return 'O'


def check_cols():
    if board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == \
            board[8] == 'X':
        return 'X'
    if board[0] == board[3] == board[6] == 'O' or board[1] == board[4] == board[7] == 'O' or board[2] == board[5] == \
            board[8] == 'O':
        return 'O'


def check_diag():
    if board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
        return 'X'
    if board[0] == board[4] == board[8] == 'O' or board[2] == board[4] == board[6] == 'O':
        return 'O'


def check_winner(winner):
    if winner == 'X' or winner == 'O':
        return True


def check_if_win():
    winner = check_rows()
    if check_winner(winner):
        return winner
    winner = check_cols()
    if check_winner(winner):
        return winner
    winner = check_diag()
    if check_winner(winner):
        return winner


def check_if_tie():
    flag = 0
    for i in board:
        if i == '-':
            flag = 1
    if flag == 0:
        return "Tie"


def flip_player():
    global board
    if switch == '1':
        board = singleplayer.flip_player(board)
        display_board()
    else:
        board = multiplayer.flip_player(board)
        display_board()


def play_game():
    display_board()
    while True:
        handle_turn()
        winner = check_if_game_over()
        if check_winner(winner) or winner == "Tie":
            return winner
        flip_player()
        winner = check_if_game_over()
        if check_winner(winner) or winner == "Tie":
            return winner


def congradulate(winner):
    if winner == "Tie":
        print("The Match is a Tie")
    else:
        print(f"{winner} Wins")


switch = 0
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe")
    print("1.Single Player")
    print("2.Multi  Player")
    print("Any other key to Quit")
    print("Enter your choice: ", end='')
    switch = input()
    if switch != '1' or switch != '2':
        winner = play_game()
        display_board()
        congradulate(winner)
    print("Thanks For Playing")
