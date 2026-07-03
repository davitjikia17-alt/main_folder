import copy


SIZE = 8

WHITE = ["WK", "WQ", "WR", "WB", "WN", "WP"]
BLACK = ["BK", "BQ", "BR", "BB", "BN", "BP"]

moved_wk = False
moved_wr_left = False
moved_wr_right = False

moved_bk = False
moved_br_left = False
moved_br_right = False

# remember: if one man can hold you down , two man can eat your khinkali/matzah
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
        "BP": "♙",
        "BR": "♖",
        "BN": "♘",
        "BB": "♗",
        "BQ": "♕",
        "BK": "♔",
        "WP": "♟",
        "WR": "♜",
        "WN": "♞",
        "WB": "♝",
        "WQ": "♛",
        "WK": "♚",
    }
    """
    for col in range(SIZE):
        board[6][col] = "WP"

    board[0] = ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"]
    board[7] = ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]

    return board


def print_map(board):
    letters = "A  B  C  D  E  F  G  H"

    # 6six - 7seven
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
        return "black"
    return "white"


def legal_move(board, start_row, start_col, new_row, new_col, figure):

    global moved_wk, moved_wr_left, moved_wr_right, moved_bk, moved_br_left, moved_br_right

    fake_board = copy.deepcopy(board)
    result = False

    if figure[1].upper() == "R":
        result = move_rook(fake_board, start_row, start_col, new_row, new_col, figure)

        if result != False:
            if figure[0].upper() == "W" and start_row == 7:
                if start_col == 0:
                    moved_wr_left = True

                elif start_col == 7:
                    moved_wr_right = True


            elif figure[0].upper() == "B" and start_row == 0:
                if start_col == 0:
                    moved_br_left = True

                elif start_col == 7:
                    moved_br_right = True

    elif figure[1].upper() == "B":
        result = move_bishop(fake_board, start_row, start_col, new_row, new_col, figure)

    elif figure[1].upper() == "P":
        result = move_pawn(fake_board, start_row, start_col, new_row, new_col, figure)

    elif figure[1].upper() == "K":

        if ((new_col - start_col) == 2) or ((new_col - start_col) == -3):

            if figure[0].upper() == "W":
                result = castle(fake_board, start_row, start_col, new_row, new_col, figure, moved_wk, moved_wr_left, moved_wr_right)
            else:
                result = castle(fake_board, start_row, start_col, new_row, new_col, figure, moved_bk, moved_br_left, moved_br_right)

        else:
            result = move_king(fake_board, start_row, start_col, new_row, new_col, figure)

        if result != False:
            if figure[0].upper() == "W":
                moved_wk = True

            else:
                moved_bk = True

    elif figure[1].upper() == "Q":
        result = move_queen(fake_board, start_row, start_col, new_row, new_col, figure)

    elif figure[1].upper() == "N":
        result = move_knight(fake_board, start_row, start_col, new_row, new_col, figure)

    if result == False:
        return False

    if figure[0].upper() == "W":
        my_king = "WK"

    else:
        my_king = "BK"

    if is_check(fake_board, my_king):
        print("\nIllegal move! You cannot put your king in check!")
        return False

    return result


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


def is_draw(board, figure):

    if is_check(board, figure):
        return False

    for start_row in range(SIZE):
        for start_col in range(SIZE):
            my_figure = board[start_row][start_col]

            if my_figure != "⬜" and my_figure != "⬛" and my_figure[0] == figure[0].upper():
                for row in range(SIZE):
                    for col in range(SIZE):

                        if legal_move(board, start_row, start_col, row, col, my_figure):
                            return False

    #
    #⢀⣀⠀⠀⠀⠀⠀⠀⢀⠔⠂⠉⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #⠂⠀⠈⠁⠒⣤⠖⠒⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #⠀⠀⠀⠀⠀⣳⠋⣉⣻⡄⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #⠀⠀⠀⠀⡤⢸⡌⠄⠒⣷⡢⢥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #⠀⠀⠀⠀⠉⢉⣳⣊⠤⢚⣷⡝⡲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #⠀⠀⠀⠀⠀⠧⠒⢳⣔⡡⠘⣻⣔⡩⢃⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #⠀⠀⠀⠀⠀⠀⢰⡡⠛⢦⢊⠔⢨⠝⡷⣮⣎⡅⢠⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #⠀⠀⠀⠀⠀⠀⠀⠀⢰⣈⠟⢦⣇⠎⡔⠡⠊⡝⡳⠮⣤⣊⠆⢀⡀⠀⠀⠀⠀⠀
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⠊⠹⢳⠧⣼⣰⠁⠎⡔⠙⡶⣧⠂⢀⠀⠀⠀⠀
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠁⠀⣃⠍⡹⢲⣤⢊⠔⡩⠳⣥⠃⠀⠀⠀
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠁⣋⢿⣎⡔⡩⠼⣶⡸⠂⠀
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⡺⢿⡔⡉⠭⣧⢐⡄
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢒⠩⢯⠔⢈⣹⣅⣀
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⢽⡍⠄⠒⡗⠚
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠽⣗⠩⠭⣿⠩
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢧⣀⣠⡇⠀
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠶⡶⡙⡄
    #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠇⠐⠼
    #


    return True


def is_checkmate(board, figure):
    if not is_check(board, figure):
        return False

    for start_row in range(SIZE):
        for start_col in range(SIZE):
            my_figure = board[start_row][start_col]

            if my_figure != "⬜" and my_figure != "⬛" and my_figure[0] == figure[0].upper():
                for row in range(SIZE):
                    for col in range(SIZE):

                        if legal_move(board, start_row, start_col, row, col, my_figure):
                            return False
    return True


def is_check(board, figure):


    king_row = 0
    king_col = 0

    check_board = copy.deepcopy(board)

    for current_row in range(SIZE):
        for current_col in range(SIZE):

            if check_board[current_row][current_col] == figure.upper():

                king_row = current_row
                king_col = current_col


    for row in range(SIZE):
        for col in range(SIZE):

            target = check_board[row][col]

            if target != "⬜" and target != "⬛":
                if target[0] != figure[0].upper():

                    if target[1] == "R":
                        if move_rook(check_board, row, col, king_row, king_col, target):
                            return True

                    elif target[1] == "N":
                        if move_knight(check_board, row, col, king_row, king_col, target):
                            return True

                    elif target[1] == "Q":
                        if move_queen(check_board, row, col, king_row, king_col, target):
                            return True
                            # there little bugs
                        # 𖢥 𖢥 𖢥 𖢥 𖢥 𖢥
                    elif target[1] == "P":
                        if move_pawn(check_board, row, col, king_row, king_col, target):
                            return True

                    elif target[1] == "K":
                        if move_king(check_board, row, col, king_row, king_col, target):
                            return True

                    elif target[1] == "B":
                        if move_bishop(check_board, row, col, king_row, king_col, target):
                            return True

    return False


def move_king(board, current_row, current_col, new_row, new_col, figure):
    row = current_row - new_row
    col = current_col - new_col

    if ((row != 1 and row != -1 and row != 0) or
            (col != 1 and col != -1 and col != 0)):
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


def move_queen(board, current_row, current_col, new_row, new_col, figure):

    if current_row == new_row or current_col == new_col:

        board = move_rook(board, current_row, current_col, new_row, new_col, figure)
        return board

    """
                            
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣀⡤⠖⠒⠛⠳⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠶⠾⠛⠛⠛⠲⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡗⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⣀⣀⠤⠤⠖⠒⠒⡿⠏⠀⠀⠀⠀⠀⠀⠘⢻⣦⣄⠀⠀⠀⠀⠀⠀⣰⡾⠋⠁⢀⣀⣀⠀⠀⣀⣠⣀⣄⣴⣦⠶⠒⠊⠉⠉⠉⠙⠴
                        ⣠⡞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣄⣀⢸⣿⣿⣤⣀⢠⣶⣶⣿⣿⣿⣛⣟⣯⡿⣿⢿⡿⢿⣯⢍⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣽⡯⣿⣿⣿⣿⣿⣾⣽⣯⣾⣽⢯⡿⣽⣻⢮⢿⣽⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾⣷⣏⣿⣏⣷⡟⣏⣿⣏⣷⣇⡆⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣾⣽⣯⣿⣷⣻⢾⣯⡏⢴⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⢧⣤⣤⣤⣤⣤⣴⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣟⣶⡹⣸⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣯⠍⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣯⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠁⢸⣿⡿⠉⠀⠀⠈⠉⢻⣿⡛⠛⠛⠛⠛⠛⠋⠛⠻⠿⠿⠿⢿⡯⣄⣀⠀⠀⠀⠀⠀⢀
                        ⠺⣀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⣀⡼⠋⠁⠀⠀⠀⠀⠀⠀⠙⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠒⠶⠖⠚
                        ⠀⠛⠲⠦⠤⠤⠤⠔⠒⠿⣷⣤⣤⣤⣤⣤⡶⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠷⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⠤⣀⣀⣀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        
    """

    board = move_bishop(board, current_row, current_col, new_row, new_col, figure)
    return board


def move_knight(board, current_row, current_col, new_row, new_col, figure):

    row = current_row - new_row
    col = current_col - new_col

    if not (((row == 2 or row == -2) and (col == 1 or col == -1)) or
            ((row == 1 or row == -1) and (col == 2 or col == -2))):
        return False #𖢥

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


def move_pawn(board, current_row, current_col, new_row, new_col, figure):

    if figure[0].upper() == "W":
        step= -1
        start_row = 6

    else:
        step = 1
        start_row = 1

    row = new_row - current_row
    col = new_col - current_col

    legal_move = False

    if col == 0 and row == step:

        if board[new_row][new_col] == "⬜" or board[new_row][new_col] == "⬛":
            legal_move = True


    elif col == 0 and row == ( 2 * step ) and current_row == start_row:

        if ((board[new_row][new_col] == "⬜" or board[new_row][new_col] == "⬛") and
            (board[current_row + step][new_col] == "⬜" or board[current_row + step][new_col] == "⬛")):

            legal_move = True

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    #    ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣄⣀⣀⣤⣶⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀copy paste : high cortisol⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀spend 2 hours from wonderful life: low cortisol⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⡿⣻⣷⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⢤⣤⣀⣀⣀⣀⣀⣤⣴⣶⣾⣿⣿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣿⣷⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⡿⣻⣿⣾⣿⡿⠛⣿⣿⣿⣿⣿⣯⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⡿⠋⢹⣿⣿⣿⡿⠋⢠⣿⡿⠟⠉⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⡿⢋⣀⣀⣼⣿⣿⣟⡁⠰⠛⠁⠀⠀⠀⠀⠀⢸⣿⠇⠸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠠⠶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡿⠋⠉⠉⠉⠉⣿⠟⣉⣍⠉⠀⠀⠀⢀⠛⢛⠛⡛⠾⠿⢄⣀⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⢻⣿⣧⣿⣿⣿⡿⣻⣷⠶⠶⠶⠶⠚⠛⠒⠖⠉⠀⠀⠀⠀⠨⠦⣶⣶⣶⣦⣤⣍⠒⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣾⣿⣿⣿⣿⠁⠀⠀⢠⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣄⠀⠉⠑⣿⣿⣿⡟⠛⠿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢀⣀⠀⠉⡛⢉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠋⠀⠀⠀⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⣿⣿⡿⠟⠿⣿⣿⣧⠀⠋⠈⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠋⠀⣸⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⢀⠏⡶⠽⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠻⣿⣿⠿⠿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⡠⠾⠿⠿⠿⠿⡄⠘⣝⢳⢄⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⡗⢸⣿⣆⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠶⣶⣶⣶⣶⣦⣤⣤⣤⣶⣶⣶⣶⣿⣶⣄⡉⠀⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠟⠉⣠⠞⠛⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠤⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⢧⡈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⢿⡷⣿⣿⣿⣿⣲⣟⣿⣄⠑⢄⡈⠓⠤⣀⠀⠀⠀⠀⠀⠀⢀⡠⢴⠋⣸⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⣦⣄⠉⠒⠤⣀⠈⠁⠒⠒⠒⠊⣁⠴⠃⣰⣿⢸⣿⣿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⣠⣴⠿⠿⠛⣿⣿⣿⣿⣿⠿⠛⡿⠀⢸⣿⣿⣿⣿⣷⣦⣀⠀⠉⠉⡍⣶⠊⠉⢀⣠⣾⣿⣿⠺⢿⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠛⠉⠀⠀⣼⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢀⠘⢰⣿⣿⣿⣿⣿⣿⣿⡺⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⠀⠀⠀⢀⣸⠿⢻⠃⠀⠀⠀⣠⠃⠀⠀⢸⣿⣮⣻⣿⣿⣿⣿⣿⣿⣿⠈⠄⢸⣿⣿⣿⣿⣿⣿⡼⣄⠘⣧⠝⠲⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀⢀⣠⠂⠉⠀⠀⡞⠀⠀⠀⠀⠁⠀⠀⠀⣸⣿⣿⣿⣿⣿⣟⣻⡿⠿⣿⢀⣴⣾⣿⣿⣿⣿⣿⣿⡇⠜⢻⣛⠦⣄⣀⠜⠓⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    #    ⠀⠀
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    elif (col == 1 or col == -1) and row == step:
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

    row = current_row - new_row
    col = current_col - new_col

    if row != col and -row != col :
        return False

    if new_col > current_col:
        step_col = 1
    else:
        step_col = -1

    if new_row > current_row:
        step_row = 1
    else:
        step_row = -1

    """
              Nice day debugger <3
    ⣿⣿⣿⣿⣿⠿⢿⡿⠛⠛⠉⠉⠉⠉⠉⠙⠛⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠙⠛⠛⠛⠿⣿⣿⠿⣿⣿⣿⣿⣿
    ⣿⣿⠿⠋⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⡈⠙⢿⣿⣿
    ⠋⠁⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣚⣿⣿⣶⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⣀⣀⣀⢀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣴⣶⣶⣶⣶⣶⡶⣶⣤⣤⣀⡀⠀⠀⠈⠢⣄⠈⠙
    ⣷⣤⡀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⠇⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠸⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢧⠀⠉⠉⠙⠙⠉⠉⠉⠉⠉⠉⠋⠛⠛⠋⢹⣿⣿⣿⣿⣿⣿⣷⣦⣤⡀⠈⣠⣤
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⣀⠀⠁⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠒⠲⢷⡆⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢈⡿⠿⠛⠛⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⢠⣴⣾⠋⠀⠀⠀⠀⠀⠀⠒⠀⠀⢹⣆⠀⠲⣦⣤⣿⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢀⣾⣧⣤⡔⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣦⣀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣀⣀⣄⡀⠘⠻⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠷⠀⠙⢻⣿⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢀⣹⡿⠋⠀⠾⠿⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠿⠟⠛⠁⣀⠀⠈⢻⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠁⠀⢀⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⢀⣸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠈⣿⣿⣿⣿⠉⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⣠⣶⣿⣿⣿⠉⠀⠐⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠉⠁⢀⣀⣤⣾⣿⣿⣿⣿⡟⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⡛⠛⠛⠛⠛⠋⠉⠉⠉⠉⠁⣀⣀⣀⣀⣤⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """

    check_row = current_row + step_row
    check_col = current_col + step_col

    while check_row != new_row and check_col != new_col:
        if board[check_row][check_col] != "⬜" and board[check_row][check_col] != "⬛":
            return False

        check_row += step_row
        check_col += step_col


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


def castle(board, current_row, current_col, new_row, new_col, figure, moved_k, moved_rl, moved_rr):

    if moved_k:
        return False

    if figure[0].upper() == "W":
        row = 7

    else:
        row = 0

    if (current_row != row or new_row != row) and (current_col != 4):
        return False






    return board



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
        white_king = "WK"
        black_king = "BK"

        if is_draw(board, white_king) or is_draw(board, black_king):
            print(f"Stalemate !!!")
            break

        if is_checkmate(board, white_king):
            print(f"CHECKMATE ! Black king has won the game!")
            print()
            break

        elif is_checkmate(board, black_king):
            print(f"CHECKMATE ! Black king has won the game!")
            print()
            break


        if turn == "white":
            print("| White's turn! |")

            figure = input("Enter figure (wn. wq; to stop 'quit') : ")

            if figure.lower() == "quit":
                print()
                print("Goodbye!")
                print()
                break

            if figure.upper() not in WHITE and figure.upper() not in BLACK:
                print()
                print("You have to choose figure")
                continue

            while figure[0].upper() != "W":
                print()
                print("White figures to play!")
                figure = input("Enter figure (wn. wq; to stop 'quit') : ")

                if figure.lower() == "quit":
                    break

                if figure.upper() not in WHITE and figure.upper() not in BLACK:
                    print()
                    print("You have to choose figure")
                    continue


        elif turn == "black":
            print("| Black's turn! |")
            figure = input("Enter figure (bn. bq; to stop 'quit') : ")

            if figure.lower() == "quit":
                print()
                print("Goodbye!")
                print()
                break

            if figure.upper() not in WHITE and figure.upper() not in BLACK:
                print()
                print("You have to choose figure")
                continue

            while figure[0].upper() != "B":
                print()
                print("Black figures to play!")
                figure = input("Enter figure (bn. bq; to stop 'quit') : ")

                if figure.lower() == "quit":
                    break

                if figure.upper() not in WHITE and figure.upper() not in BLACK:
                    print()
                    print("You have to choose figure")
                    continue


        if figure.lower() == "quit":
            print()
            print("Goodbye!")
            print()
            break

        move = input(f"Enter move for {figure.upper()}.(a.h. E2 E5): ")
        start_row, start_col, new_row, new_col = parse_move(move)

        if start_row == new_row and start_col == new_col:
            print()
            print("Your figure is already there!")
            continue

        if board[start_row][start_col] != figure.upper():
            print()
            print("Invalid figure entered!")
            continue


        result = legal_move(board, start_row, start_col, new_row, new_col, figure)

        if result == False:
            print("\nInvalid move! please try again!")
            continue

        else:
            board = result

        print()
        print_map(board)
        print()
        turn_counter += 1

        if turn == "white" and is_check(board, "BK"):
            print("Check to Black King!")

        elif turn == "black" and is_check(board, "WK"):
            print("Check to White King!")


    print("Remember ! if game wasn't lesson, it's wors then lose!")

main()
