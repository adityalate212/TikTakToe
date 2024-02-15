def print_board(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")


def get_player_input(board, player):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not is_position_available(board, position):
        position = int(input(f"{player}, choose your next position: (1-9) "))
    return position

def is_position_available(board, position):
    return board[position] == " "

def place_marker(board, marker, position):
    board[position] = marker

def is_winner(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))

def is_board_full(board):
    return " " not in board[1:]

def play_game():
    print("Welcome to Tic Tac Toe!")
    board = [" "] * 10
    player1_marker, player2_marker = get_player_markers()
    current_player = choose_first_player()
    game_on = True
    while game_on:
        print_board(board)
        position = get_player_input(board, current_player)
        place_marker(board, current_player, position)
        if is_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! {current_player} has won the game!")
            game_on = False
        else:
            if is_board_full(board):
                print_board(board)
                print("The game is a tie!")
                break
            else:
                current_player = get_next_player(current_player, player1_marker, player2_marker)

def get_player_markers():
    marker = ""
    while marker not in ["X", "O"]:
        marker = input("Player 1, choose your marker (X or O): ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def choose_first_player():
    import random
    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"

def get_next_player(current_player, player1_marker, player2_marker):
    if current_player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"

play_game()
