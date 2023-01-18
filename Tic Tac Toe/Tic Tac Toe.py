#Create the empty board
board = [[3*b + a + 1 for a in range(3)] for b in range(3)]

#import time #for fanciness to make the user think the computer is thinking
from random import randrange #For the computers moves

def DisplayBoard(board):    #The function to make the display pretty
    print("+-------"*3, end = "+\n")
    for row in range(3):
        print("|       "*3, end = "|\n")
        for col in range (3):
            print("|  ", board[row][col],"  ", end = "")
        print("|\n", "|       "*3, sep = "", end = "")
        print("|\n", "+-------"*3, sep = "", end = "+\n")


def EnterMove(board): #Get the user to enter a move
    valid = False
    
    while not valid: # loop for sanity check
        move = input("Where would you like to place an O? ") #attempted move
        if move <"1" or move >"9": # range check
            print("Move invalid, enter a new move")
            continue
        move = int(move)
        if (move not in board[0] and move not in board[1]
                and move not in board[2]): # check if number already taken
            print("Move invalid, enter a new move")
            continue
        else:
            board[(move-1)//3][(move-1)%3] = "O"
            return True

def MakeListOfFreeFields(board):
#Checks to see free fields for move entry
    freemoves=[]
    for row in range (3):
        for col in range (3):
            if board[row][col] != "O" and board[row][col] != "X":
                freemoves.append((row,col))
    return freemoves #creates a list of free moves

def DrawMove(board):
    freemoves = MakeListOfFreeFields(board)
    left = len(freemoves)
    if left > 0:
        loc = randrange(left)
        row, col = freemoves[loc]
        board[row][col] = "X"
    

def VictoryFor(board, sign):
    if sign == "X":  #assigns who we are looking at for the victor
        victor = "Computer"
    if sign == "O":
        victor = "User"
    
    for i in range(3):
        #checks the rows
        if board[i][0] == sign and board[i][1] == sign and board [i][2] == sign:
            return victor
        #checks the columns
        if board[0][i] == sign and board[1][i] == sign and board [2][i] == sign:
            return victor
    #actually checks the columns
        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return victor
        if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return victor
    return

remaining = MakeListOfFreeFields(board)
computerturn = True

while len(remaining)>0:
    DisplayBoard(board)
    if computerturn:
        DrawMove(board)
        victor = VictoryFor(board, "X")
    else:
        EnterMove(board)
        victor = VictoryFor(board, "O")
    if victor != None:
        break
    computerturn = not computerturn
    remaining = MakeListOfFreeFields(board)

        
DisplayBoard(board)
if victor == "User":
    print("Congratulions, you won!")
elif victor == "Computer":
    print("Unlucky, the computer won!")
else:
    print("It's a tie...")
    
input("press enter to exit")
