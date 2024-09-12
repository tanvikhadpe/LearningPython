def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_won = False
    
    while not game_won and not is_board_full(board):
        print_board(board)
        move = input(f"Player {current_player}, enter your move (row and column): ").split()
        
        if len(move) != 2 or not all(num.isdigit() for num in move):
            print("Invalid input. Please enter two numbers.")
            continue
        
        row, col = int(move[0]), int(move[1])
        
        if row not in range(3) or col not in range(3) or board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        
        board[row][col] = current_player
        game_won = check_win(board, current_player)
        
        if not game_won:
            current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    if game_won:
        print(f"Player {current_player} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()

