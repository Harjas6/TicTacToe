import random

gboard = ["__", "__", "__",
          "__", "__", "__",
          "__", "__", "__"]

gamerun = True
playAgain = True
currentPlayer = "X"
playerFirst = 'N'

# resets global varibales
def resetgame():
    global gboard
    global gamerun
    gboard = ["__", "__", "__",
              "__", "__", "__",
              "__", "__", "__", ]
    gamerun = True


def firstturn():
    global currentPlayer

    while True:
        first = input("Would the first player like to be a X or an O?(X/O) ").upper()

        if first == "O":
            currentPlayer = "O"
            break
        elif first == "X":
            currentPlayer = "X"
            break
        else:
            print("\n")


def firstComp():
    global playerFirst
    while True:
        playerFirst = input("Would you like to play first?(Y/N) ").upper()

        if playerFirst == "Y":
            break
        elif playerFirst == "N":
            break
        else:
            print("\n")


def printboard(board):
    print("|_" + board[0] + "_|_" + board[1] + "_|_" + board[2] + "_|")
    print("|_" + board[3] + "_|_" + board[4] + "_|_" + board[5] + "_|")
    print("|_" + board[6] + "_|_" + board[7] + "_|_" + board[8] + "_|")


def comp(board, player):
    while True:
        spot = random.randint(0, 8)
        if board[spot] == "__":
            board[spot] = player
            break


def player1(board, player):
    while True:
        spot = int(input(f"Where would {player} like to play(1-9)? "))
        spot -= 1
        if 0 <= spot <= 8 and board[spot] == "__":
            board[spot] = player
            break
        else:
            print("Spot taken!\n")


def switchplayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"

    else:
        currentPlayer = "X"


def checkwinner(board, winner):
    if board[0] == board[1] == board[2] and board[1] != "__":
        winner = board[0]
        print("\n" + winner + " wins!")
        return True

    elif board[3] == board[4] == board[5] and board[3] != "__":
        winner = board[3]
        print("\n" + winner + " wins!")
        return True

    elif board[6] == board[7] == board[8] and board[6] != "__":
        winner = board[6]
        print("\n" + winner + " wins!")
        return True

    elif board[0] == board[3] == board[6] and board[0] != "__":
        winner = board[0]
        print("\n" + winner + " wins!")
        return True

    elif board[1] == board[4] == board[7] and board[1] != "__":
        winner = board[1]
        print("\n" + winner + " wins!")
        return True

    elif board[2] == board[5] == board[8] and board[2] != "__":
        winner = board[2]
        print("\n" + winner + " wins!")
        return True

    elif board[0] == board[4] == board[8] and board[0] != "__":
        winner = board[0]
        print("\n" + winner + " wins!")
        return True

    elif board[2] == board[4] == board[6] and board[2] != "__":
        winner = board[2]
        print("\n" + winner + " wins!")
        return True

    elif "__" not in board:
        print("Tie game")
        return True


# loop for multiple playthrough
while playAgain:

    # setting board to blank spaces and resetting loops
    resetgame()

    # question used to allow computer to play
    while True:
        singleplayer = input("\nPlay against a computer?(Y/N) ").upper()
        # if two users playing asks if X or O goes first
        if singleplayer == "N":
            firstturn()
            break
        # if singleplayer asking computer to go first
        elif singleplayer == "Y":
            firstComp()
            break
        else:
            print("\n")

    printboard(gboard)

    # loop for current game
    while gamerun:
        # block of code needed just for computer to have a first turn if player chooses
        if singleplayer == "Y" and playerFirst == "N":
            print("\nComputer has picked")
            comp(gboard, currentPlayer)
            printboard(gboard)
            playerFirst = "N"
            switchplayer()

        # user controlled player(s)
        player1(gboard, currentPlayer)
        printboard(gboard)
        # checking for winner and ending game if winner found
        if checkwinner(gboard, currentPlayer) == True:
            gamerun = False
            break

        switchplayer()

        # code used if computer is needed
        if singleplayer == "Y":
            print("\nComputer has picked")
            comp(gboard, currentPlayer)
            printboard(gboard)
            if checkwinner(gboard, currentPlayer):
                gamerun = False
                break

            switchplayer()

    # asking user to play again
    while True:
        again = input("\nPlay again?(Y/N) ").upper()
        if again == "N":
            playAgain = False
            print("Thanks for playing!")
            break

        elif again == 'Y':
            break
        else:
            print("\n")
