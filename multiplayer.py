def flip_player(board):
    while True:
        try:
            print("O's Chance")
            position = int(input("Choose a position for  1 to 9: ")) - 1
        except:
            print("Invalid Input!!!")
        else:
            if 0 <= position < 9:
                if board[position] != 'X' and board[position] != 'O':
                    board[position] = 'O'
                else:
                    print("Already Occupied Field")
                    continue
                break
            print("Invalid Input!!!")

    return board