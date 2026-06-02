SIZE = 8

WHITE = ["WK", "WQ", "WR", "WB", "WN", "WP"]
BLACK = ["BK", "BQ", "BR", "BB", "BN", "BP"]


def create_board():
    board = []
    for i in range(SIZE):
        row = []

        for j in range(SIZE):
            if (j + i) % 2 == 0:
                row.append("⬜")
            else:
                row.append("⬛")

        board.append(row)


    return board


def add_figures(board):
    """
    for col in range(SIZE):
       board[6][col] = "BP"


    for col in range(SIZE):
        board[1][col] = "WP"
    """
    board[7] = ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"]
    board[0] = ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]

    return board


def print_map(board):
    letters = "A  B  C  D  E  F  G  H"

    print("     " + letters)
    print("    " + "-" * 25)

    for row in range(SIZE):
        print(SIZE - row, end=" | ")

        for col in board[row]:
            print(col, end=" ")

        print("|", SIZE - row)

    print("    " + "-" * 25)
    print("    " + letters)


def player_turn(turn):

    if turn % 2 == 0:
        return "white"

    return "black"


def check_win():
    pass


def parse_move(move):
    start, end = move.split()

    col_map = {
        "A": 0, "B": 1, "C": 2, "D": 3,
        "E": 4, "F": 5, "G": 6, "H": 7
    }

    start_col = col_map[start[0].upper()]
    start_row = 8 - int(start[1])

    end_col = col_map[end[0].upper()]
    end_row = 8 - int(end[1])

    return start_row, start_col, end_row, end_col


def move_king(board, row, col, new_row, new_col):
    pass


def move_queen(board, row, col, new_row, new_col):
    pass


def move_pawn(board, row, col, new_row, new_col):
    pass


def move_knight(board, row, col, new_row, new_col):
    pass


def move_rook(board, current_row, current_col, new_row, new_col):

    if current_row == new_row and current_col == new_col:
        return False

    if current_col != new_col:
        if new_col > current_col:
            step = 1

        else:
            step = -1

        for col in range(current_col + step, new_col, step):
            print("eliav")
            if board[current_row][col] != "⬜" and board[current_row][col] != "⬛":
                print("gay")
                if new_col < col:
                    print("double")
                    print("Invalid move!")
    else:
        if new_row > current_row:
            step = 1

        else:
            step = -1

        for row in range(current_row + step, new_row, step):
            print("davit")
            if board[row][current_col] != "⬜" and board[row][current_col] != "⬛":
                print("man")
                if new_row < row:
                    print("geo")
                    print("Invalid move!")

    board[current_row][current_col] = board[new_row][new_col]
    board[new_row][new_col] = "BR"


    return board


def move_bishop(board, row, col, new_row, new_col):
    pass

def main():
    print("Welcome to chess game!")

    board = create_board()
    board = add_figures(board)

    print_map(board)
    while True:
        move = input("Enter move (e.g. E2 E4): ")

        row, col, new_row, new_col = parse_move(move)


        board = move_rook(board, row, col, new_row, new_col)


        print_map(board)

        move_again = input("Do you want to play again? (y/n): ")
        if move_again == "n":
            break
main()