# i've got the display going, now its time for the players to place their X and O's in the board
from display import *

win  = False 
start = 'O'
def turn():
    global win , start
    print("The player with symbol %s 's turn ." %(start))
    # now the player with the choice chosen starts
    # the player can choose any position
    choice = int(input("Enter the position that u wanna place your symbol : "))
    if(choice > 8 or choice < 0):
        print("Invalid choice")
    elif(board[choice] != "_") : 
        print("This position is already occupied ")
    else :
        board[choice] = start
        if start == 'O':
            start = 'X'
        else :
            start = 'O'
    # check the winning condition and check the board full condition
    display_board(board)
    # this is for row wins
    for i in [0, 3, 6] :
        if(board[i] == board[i+1] == board[i+2] != "_"):
            print("Player with choice %s won" %(board[i]))
            win = True
            return
    # this is for column wins
    for i in range(0,3):
        if(board[i] == board[i+3] == board[i+6] != "_"):
            print("Player with choice %s won" %(board[i]))
            win = True
            return
    # this is for diagonal wins
    
    if(board[0] == board[4] == board[8] != "_"):
        print("Player with choice %s won" %(board[0]))
        win = True
        return
    
    elif(board[2] == board[4] == board[6] != "_"):
        print("Player with choice %s won" %(board[2]))
        win = True
        return
    
def board_check(board):
    global win, start
    while win == False:
        turn()  # Call the turn function to let a player play
        
        # Check if the board is full after each turn
        if "_" not in board:  # If there's no "_" left, the board is full
            message = "Board is Full"
            print(message)  # Output the message
            return message  # Return the message when the board is full
board_check(board)
    