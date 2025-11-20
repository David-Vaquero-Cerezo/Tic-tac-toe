import numpy as np
import pandas as pd
import pygame
import sys

def check_win_condition(board, row, col, player):
    size = len(board[0])
    diagonal_1 = [board[i][i] for i in range(size)]
    diagonal_2 = [board[i][size - 1 - i] for i in range(size)]
    if len(set(board[row])) == 1 and set(board[row]) != set("."):
        print(f"{player} won! (row)")
        return True
    elif len(set(board.T[col])) == 1 and set(board.T[col]) != set("."):
        print(f"{player} won! (column)")
        return True
    elif (len(set(diagonal_1)) == 1 or len(set(diagonal_2)) == 1) and (set(diagonal_1) != set(".") and set(diagonal_2) != set(".")):
        print(f"{player} won! (diagonal)")
        return True
    else:
        return False

def draw_board(size, color, width, height, line_width):
    try:
    # Vertical lines
        for i in range(1, size):
            pygame.draw.line(screen, color, (i*width/size, 0), (i*width/size, height), line_width)

        # Horizontal lines
        for j in range(1, size):
            pygame.draw.line(screen, color, (0, j*height/size), (width, j*height/size), line_width)

        return True
    except:
        print("There was an error trying to draw the board")
        return False

def get_cell_from_click(size, pos, width, height):
    x, y = pos
    row = y//(height//size)
    col = x//(width//size)
    return row, col

def draw_symbol(size, row, col, width, height, symbol_image):
    cell_width = width // size
    cell_height = height // size

    scale_x, scale_y = int(cell_width * 0.75), int(cell_height * 0.75)  # 75% of the cell size for padding
    transformed_image = pygame.transform.smoothscale(symbol_image, (scale_x, scale_y))

    x = col * cell_width + cell_width//2 - transformed_image.get_width()//2
    y = row * cell_height + cell_height//2 - transformed_image.get_height()//2
    screen.blit(transformed_image, (x, y))
    return True

def pos_is_correct(size, row, col):
    try:
        if row not in range(size) or col not in range(size):
            print(f"Something has gone terribly wrong, this shouldnt be possible")
            return False
        if BOARD[row, col] != ".":
            print(f"That position is invalid, {player["Text"]}, it is already occupied")
            return False
        return True
    except:
        print(f"Something has gone wron, time to debug")
        return False

pygame.init()

screen_width = 800
screen_height = 600

SIZE = 3
BOARD = np.full((SIZE, SIZE), ".", dtype=object)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")
black = (0, 0, 0)

background = pygame.image.load("background.jpg")
# Scale to window size
background = pygame.transform.scale(background, (screen_width, screen_height))
screen.blit(background, (0, 0))

FPS = pygame.time.Clock()
FPS.tick(1)

x_img = pygame.image.load("x.png")
o_img = pygame.image.load("o.png")
x_img.set_alpha(200)  # ~80% opacity
o_img.set_alpha(200)

turn = 1

# Main game loop
while True:

    if turn%2 != 0:
        player = {
            "Text": "Player 1",
            "image": x_img,
            "symbol": "X"
        }
    else:
        player = {
            "Text": "Player 2",
            "image": o_img,
            "symbol": "O"
        }
    
    if turn == SIZE*SIZE:
        print("Its a draw! Well played")
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detect mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_cell_from_click(SIZE, mouse_pos, screen_width, screen_height)
            if pos_is_correct(SIZE, row, col):
                print(f"Clicked on row {row}, column {col}")  # Debug
                BOARD[row][col] = player["symbol"]

                if check_win_condition(BOARD, row, col, player["Text"]):
                    pygame.quit()
                    sys.exit()
                turn +=1
            else:
                pass

    for row in range(SIZE):
        for col in range(SIZE):
            if BOARD[row][col] == "X":
                draw_symbol(SIZE, row, col, screen_width, screen_height, x_img)
            elif BOARD[row][col] == "O":
                draw_symbol(SIZE, row, col, screen_width, screen_height, o_img)

    draw_board(size = SIZE, color = black, width = screen_width, height = screen_height, line_width = 10)
    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second

