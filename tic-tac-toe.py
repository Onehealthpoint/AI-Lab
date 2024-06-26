import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

# win Flags #
Win = 1
Draw = -1
Running = 0
Stop = 1
#  -------- #

Game = Running
Mark = 'X'


# This Function Draws Game Board
def DrawBoard():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")


# This Function Checks position is empty or not
def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False

    # This Function Checks player has won or not


def CheckWin():
    global Game
    # Horizontal winning condition
    if (board[1] == board[2]) and (board[2] == board[3]) and (board[1] != ' '):
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
        # Vertical Winning Condition
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
        # Diagonal Winning Condition
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
        # Match Tie or Draw Condition
    elif all(board[i] != ' ' for i in range(1, len(board))):
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe Game:")
while Game == Running:
    DrawBoard()
    if player % 2 != 0:
        print("Player 1's turn!")
        Mark = 'X'
    else:
        print("Player 2's turn!")
        Mark = 'O'
    choice = int(input("Enter the position [1-9] : "))
    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

DrawBoard()
if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 Won")
    else:
        print("Player 2 Won")
