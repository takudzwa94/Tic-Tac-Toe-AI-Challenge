import random

# initialize the board
board = [' ' for _ in range(9)]

# function to print the board
def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# function to check if a player has won
def check_win(player):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# function to check if the boardis full
def check_full():
    return ' ' not in board

# function for the AI to make a move
def ai_move(player):
    # check if AI can win
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            if check_win(player):
                return
            board[i] = ' '
    # check if player can win and block
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' if player == 'O' else 'O'
            if check_win('X' if player == 'O' else 'O'):
                board[i] = player
                return
            board[i] = ' '
    # make a random move
    while True:
        i = random.randint(0, 8)
        if board[i] == ' ':
            board[i] = player
            return

# play the game
print("Welcome to Tic-Tac-Toe!")
print_board()
while True:
    # player move
    x = int(input("Enter your move (1-9): ")) - 1
    if board[x] != ' ':
        print("Invalid move, try again.")
        continue
    board[x] = 'X'
    print_board()
    if check_win('X'):
        print("You win!")
        break
    if check_full():
        print("It's a tie!")
        break
    # AI move
    print("AI's turn...")
    ai_move('O')
    print_board()
    if check_win('O'):
        print("AI wins!")
        break
    if check_full():
        print("It's a tie!")
        break