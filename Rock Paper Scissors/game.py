#import random
import random
Score = [0, 0]

#Set variables
PlayerDict = {"r" : 0, "p" : 1, "s" : 2}
Outputlist = ("Rock", "Paper", "Scissor")
PlayerChoice = 0
ComputerChoice = 0

#define required functions
def PlayerInput(): #Get the player's choice.
    global PlayerChoice
    Choice = input("Enter a choice; (R)ock, (P)aper or (S)cissors: ")
    Choice = Choice.lower() #just to make things easier
    if Choice != "r" and Choice != "p" and Choice != "s": #sanity check
        print("Error, invalid option.  Try again")
        PlayerInput()
    else:
        PlayerChoice = PlayerDict[Choice]
    
def ComputerInput(): #get the computer's choice.
    global ComputerChoice
    ComputerChoice = random.randint(0,2)
    
def Comparison(Player, Computer): #compare the choices and get result
    print("You chose", Outputlist[PlayerChoice], "and the computer chose", Outputlist[ComputerChoice])
    if Player == Computer: #tie condition
        print("Both players chose", Outputlist[Player], ". It's a tie!")
    elif Player == 0: #player chooses rock
        if Computer == 1:
            print("Paper covers Rock! You Lose.")
            Score[1] += 1
        else:
            print("Rock breaks Scissors! You win.")
            Score[0] += 1
    elif Player == 1: #player chooses paper
        if Computer == 0:
            print("Paper covers Rock! You win.")
            Score[0] += 1
        else:
            print("Scissors cut Paper! You lose.")
            Score[1] += 1
    elif Player == 2: #player chooses scissors
        if Computer == 0:
            print("Rock breaks Scissors! You Lose.")
            Score[1] += 1
        else:
            print("Scissors cut Paper! You win.")
            Score[0] += 1
            

def cont(): #find if the player wants to continue
    global GameState
    choice = input("Play again? (y/n): ")
    choice = choice.lower() #incase someones a dick
    if choice == "y":
        GameState = True
    elif choice == "n":
        GameState = False
    else: #sanity check
        print("Error, invalid choice.  Try again.")
        cont()
    
GameState = True

#enter a while loop to allow repeated plays
while GameState == True:
    PlayerInput()
    ComputerInput()
    Comparison(PlayerChoice, ComputerChoice)
    cont()
    if GameState == False:
        print("Final Scores:")
        print("Computer:", Score[1])
        print("Player:", Score[0])
