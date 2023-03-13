from board import init, display

WIDTH = 10
HEIGHT = 10

board = init(WIDTH, HEIGHT)

board[2][3] = "█"
board[3][2] = "█"
board[5][5] = "█"

display(board)