import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    # Print the current state of the game board
    for i in range(0, 9, 3):
        # Print a row of the board
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        
        if i < 6:
            # Print a horizontal divider between rows, except for the last row
            print("--+---+--")


def get_player_move():
    while True:
        player_input = input("Enter your move (1-9): ")
        
        if player_input.isdigit():
            # Convert player's input to an integer
            player_move = int(player_input) - 1
            
            if player_move in range(len(board)) and board[player_move] == " ":
                # Check if the player's move is within the valid range (0-8) and the chosen position is empty
                return player_move
            
        # If the input is not a valid digit or the position is already occupied, print an error message and ask for input again
        print("Invalid move. Try again.")



def check_win(player):
    # Define the possible winning combinations in tic-tac-toe
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    # Iterate over each winning combination
    for combo in winning_combinations:
        # Check if all three squares in the current combination are filled by the given player
        if all(board[i] == player for i in combo):
            # If so, the player has won the game, so return True
            return True
    # If none of the winning combinations are satisfied, the player has not won the game, so return False
    else:
        return False


def check_tie():
    return " " not in board

def play_game():
    # Display welcome message and instructions
    print("Welcome to Tic Tac Toe!")
    print("You will be X and the computer will be O.")
    print("To make a move, enter a number from 1-9 corresponding to the board position:")
    print_board()

    while True:
        # Player turn
        player_move = get_player_move()
        board[player_move] = "X"
        print_board()
        # Check if the player has won or the game is a tie
        if check_win("X"):
            print("Congratulations! You win!")
            break
        elif check_tie():
            print("It's a tie!")
            break

        # Computer turn
        print("Computer's turn...")
        while True:
            # Generate a random move for the computer
            computer_move = random.randint(0, 8)
            if board[computer_move] == " ":
                board[computer_move] = "O"
                break
        print_board()
        # Check if the computer has won or the game is a tie
        if check_win("O"):
            print("Sorry, you lose.")
            break
        elif check_tie():
            print("It's a tie!")
            break
# Start the game
play_game()


