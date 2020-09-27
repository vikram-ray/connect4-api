def check_winner(board):
    # Checking rows 
    for r in range(7):
        for c in range(3):
            if (board[r][c] == board[r][c + 1] == board[r][c + 2] == board[r][c + 3]) and (board[r][c] != ""):
                return board[r][c]

    # Checking column
    for c in range(6):
        for r in range(3):
            if (board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 3][c]) and (board[r][c] != ""):
                return board[r][c]


    # TODO left-right diagnol case
    
    # TODO right-left diagnol case

    return ""