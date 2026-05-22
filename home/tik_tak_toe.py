def print_board(board):
    print("---------")
    for row in board:
        print(" ".join(row))
    print("---------")


def create_matrix():
    return [["H" for _ in range(3)] for _ in range(3)]


def get_coordinates(current):
    while True:
        place = input(f"{current}, enter coordinates")

        if "," not in place:
            print("Invalid input. Use 'row,col'")
            continue

        row_col = place.split(",")
        if len(row_col) != 2:
            print("Invalid input. Use 'row,col'")
            continue

        row = row_col[0].strip()
        col = row_col[1].strip()

        if not row.isdigit() or not col.isdigit():
            print("Row must be between 1 to 3")
            continue

        row = int(row)
        col = int(col)

        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Column must be between 1 to 3")
            continue

        return [row, col]


def update_board(board, row, col, current):
    if board[row - 1][col - 1] == "H":
        board[row - 1][col - 1] = current
        return True
    else:
        print("This cell is taken")
        return False


def switch_player(current):
    return "O" if current == "X" else "X"


def check_if_board_is_full(board):
    for row in board:
        if "H" in row:
            return False
    return True


def check_winner(board, current):
    if (board[0][0] == current and board[1][1] == current and board[2][2] == current) or \
            (board[0][2] == current and board[1][1] == current and board[2][0] == current):
        return True

    for row in board:
        if all(cell == current for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == current for row in range(3)):
            return True

    return False


def play_turn(board, current):
    while True:
        row, col = get_coordinates(current)
        if update_board(board, row, col, current):
            break


def main():
    board = create_matrix()
    current = "X"
    print("Welcome to Tictactoe!")

    while True:
        print_board(board)
        play_turn(board, current)

        if check_winner(board, current):
            print(f"{current} is the winner!")
            print_board(board)
            break

        if check_if_board_is_full(board):
            print("Its a tie!")
            print_board(board)
            break

        current = switch_player(current)

    print("game have finished")
main()


