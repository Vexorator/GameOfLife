def init (width, height):
    board = []
    for x in range(height):
        row = []
        for y in range(width):
            row.append(" ")
        board.append(row)
    return board

def display(board):
    print("\033[H\033[J", end="")
    for x in board:
        print(x)