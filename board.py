def init (width: int, height: int):
    board = []
    for x in range(height):
        row = []
        for y in range(width):
            row.append("0")
        board.append(row)
    return board

def display(board: list):
    print("\033[H\033[J", end="")
    for x in board:
        for y in x:
            if y == "1":
                print("█", end=" ")
            else:
                print(" ", end=" ")
        print("", end="\n")