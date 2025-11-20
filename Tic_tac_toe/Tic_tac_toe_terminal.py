import numpy as np
import pandas as pd

SIZE = 3
BOARD = np.full((SIZE, SIZE), ".", dtype=object)

def check_win_condition(x, y, player):
    diagonal_1 = [BOARD[i][i] for i in range(SIZE)]
    diagonal_2 = [BOARD[i][SIZE - 1 - i] for i in range(SIZE)]
    if len(set(BOARD[x])) == 1:
        print(f"{player} won! (row)")
        return True
    elif len(set(BOARD.T[y])) == 1:
        print(f"{player} won! (column)")
        return True
    elif (len(set(diagonal_1)) == 1 or len(set(diagonal_2)) == 1) and (set(diagonal_1) != set(".") and set(diagonal_2) != set(".")):
        print(f"{player} won! (diagonal)")
        return True
    else:
        return False
    
win = False
turn = 1

while win == False:
    correct_position = False

    if turn%2 != 0:
        player = "Player 1"
    else:
        player = "Player 2"

    if turn == SIZE*SIZE:
        print("Its a draw! Well played")
        break

    print(f"Turn {turn}")

    while correct_position == False:
        try:
            x_position, y_position = (int(x.strip()) for x in input(f"Where do you want to place your piece, {player}? Use coordinates like 0, 1 >>").split(","))
            if x_position not in range(SIZE) or y_position not in range(SIZE):
                print(f"That position is invalid, {player}, remember the format is 0, 1")
                continue
            if BOARD[x_position, y_position] != ".":
                print(f"That position is invalid, {player}, it is already occupied")
                continue
            correct_position = True
        except:
            print(f"That position is invalid, {player}, remember the format is 0, 1")

    if player == "Player 1":
        BOARD[x_position, y_position] = "X"
    else:
        BOARD[x_position, y_position] = "O"

    print(BOARD)
    win = check_win_condition(x_position, y_position, player)

    turn += 1
