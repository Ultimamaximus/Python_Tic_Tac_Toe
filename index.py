import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    # Print the current state of the game board
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def get_player_move():
    while True:
        try:
            # Prompt the user to enter a move and subtract 1 to match the index of the board list
            player_move = int(input("Enter your move (1-9): ")) - 1
            # Check if the board position is empty, return the valid move
            if board[player_move] == " ":
                return player_move
            else:
                print("That position is already taken. Try again.")
        except ValueError:
            # Handle invalid input (not an integer)
            print("Invalid input. Try again.")

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
        # Check if the player has won
        if check_win("X"):
            print_board()
            print("Congratulations! You win!")
            break
        # Check if the game is a tie
        if check_tie():
            print_board()
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
        # Check if the computer has won
        if check_win("O"):
            print_board()
            print("Sorry, you lose.")
            break
        # Check if the game is a tie
        if check_tie():
            print_board()
            print("It's a tie!")
            break
        # Print the updated game board
        print_board()
# Start the game
play_game()


