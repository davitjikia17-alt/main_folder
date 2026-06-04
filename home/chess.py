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

    for col in range(SIZE):
       board[1][col] = "BP"
    """
    pieces = {
        "P": "♙",
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "p": "♟",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
    }
    """
    for col in range(SIZE):
        board[6][col] = "WP"

    board[0] = ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"]
    board[7] = ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]

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

    # 6six - 7seven
    print("    " + "-" * 25)
    print("    " + letters)


def player_turn(turn):

    if turn % 2 == 0:
        return "black"
    return "white"


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


def check_win():
    pass


def move_king(board, current_row, current_col, new_row, new_col, figure):
    pass


def move_queen(board, current_row, current_col, new_row, new_col, figure):
    pass


def move_pawn(board, current_row, current_col, new_row, new_col, figure):

    if figure[0].upper() == "W":
        direction = -1
        start_row = 6

    else:
        direction = 1
        start_row = 1

    row = new_row - current_row
    col = new_col - current_col

    legal_move = False

    if col == 0 and row == direction:
        if board[new_row][new_col] == "⬜" or board[new_row][new_col] == "⬛":
            legal_move = True


    elif col == 0 and row == ( 2 * direction ) and current_row == start_row:
        if ((board[new_row][new_col] == "⬜" or board[new_row][new_col] == "⬛") and
            (board[current_row + direction][new_col] == "⬜" or board[current_row + direction][new_col] == "⬛")):
            legal_move = True


    elif (col == 1 or col == -1) and row == direction:
        target = board[new_row][new_col]
        if (target != "⬜" and target != "⬛" and
                target[0] != figure[0].upper()):
            legal_move = True


    if  legal_move == False:
        return False


    if (current_row + current_col) % 2 == 0:
        board[current_row][current_col] = "⬜"

    else:
        board[current_row][current_col] = "⬛"

    board[new_row][new_col] = figure.upper()

    return board




def move_knight(board, current_row, current_col, new_row, new_col, figure):
    pass


def move_rook(board, current_row, current_col, new_row, new_col, figure):

    if current_row != new_row and current_col != new_col:
        return False

    if current_col != new_col:
        if new_col > current_col:
            step = 1

        else:
            step = -1

        for col in range(current_col + step, new_col, step):
            if (board[current_row][col] != "⬜" and
                    board[current_row][col] != "⬛"):
                return False

    else:
        if new_row > current_row:
            step = 1

        else:
            step = -1

        for row in range(current_row + step, new_row, step):
            if (board[row][current_col] != "⬜" and
                    board[row][current_col] != "⬛"):
                return False

    target = board[new_row][new_col]

    if target != "⬜" and target != "⬛":

        if target[0] == figure[0].upper():
            return False

    if (current_row + current_col) % 2 == 0:
        board[current_row][current_col] = "⬜"

    else:
        board[current_row][current_col] = "⬛"

    board[new_row][new_col] = figure.upper()


    return board


def move_bishop(board, current_row, current_col, new_row, new_col, figure):
    pass

def main():
    turn_counter = 1
    print("Welcome to chess game!")

    board = create_board()
    board = add_figures(board)

    print()
    print_map(board)
    print()

    while True:
        turn = player_turn(turn_counter)

        if turn == "white":
            print("| White's turn! |")

            figure = input("Enter figure (wn. wq; to stop 'quit') : ")

            if figure.lower() == "quit":
                print()
                print("Goodbye!")
                print()
                break

            while figure[0].upper() != "W":
                print()
                print("White figures to play!")
                figure = input("Enter figure (wn. wq; to stop 'quit') : ")

                if figure.lower() == "quit":
                    break


        elif turn == "black":
            print("| Black's turn! |")
            figure = input("Enter figure (bn. bq; to stop 'quit') : ")

            if figure.lower() == "quit":
                print()
                print("Goodbye!")
                print()
                break

            while figure[0].upper() != "B":
                print()
                print("Black figures to play!")
                figure = input("Enter figure (bn. bq; to stop 'quit') : ")

                if figure.lower() == "quit":
                    break

        if figure.lower() == "quit":
            print()
            print("Goodbye!")
            print()
            break

        move = input(f"Enter move for {figure.upper()}.(a.h. E2 E5): ")
        row, col, new_row, new_col = parse_move(move)

        if board[row][col] != figure.upper():
            print()
            print("Invalid figure entered!")
            continue

        result = False

        if figure[1].upper() == "R":
            result = move_rook(board, row, col, new_row, new_col, figure)

        elif figure[1].upper() == "B":
            pass

        elif figure[1].upper() == "P":
            result = move_pawn(board, row, col, new_row, new_col, figure)

        elif figure[1].upper() == "K":
            pass

        elif figure[1].upper() == "Q":
            pass

        elif figure[1].upper() == "N":
            pass

        if result == False:
            print()
            print("Invalid move! please try again!")
            continue

        else:
            board = result

        print()
        print_map(board)
        print()
        turn_counter += 1


main()
