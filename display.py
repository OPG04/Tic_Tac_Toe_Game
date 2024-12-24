# intialize the board first
# it contains 9 elements cuz we need three cross three square blocks
board = ["_" , "_", "_",
         "_" , "_", "_",
         "_" , "_", "_"]

def display_board(board):
    # Display the board
    list_ = [0, 3, 6]
    for i in list_:
        print("  " + board[i] + " | " + board[i+1] + " | " + board[i+2] + f"    {i} , {i+1} , {i+2}  ")  # Row content
    print("\n")
display_board(board)
