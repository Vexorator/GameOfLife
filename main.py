from board import init, display
import random
import time

WIDTH = 10
HEIGHT = 10

while True:
    board = init(WIDTH, HEIGHT)


    numB = range(random.randint(2, 4))
    for x in range(random.randint(2, 9)):
        board[random.randrange(HEIGHT)][random.randrange(WIDTH)] = "1"


    display(board)
    time.sleep(1)
    