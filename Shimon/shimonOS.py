import random as rnd

SIZE = 5
choices = ['X', 'O', 'Z', 'Y']

lst = []
for i in range(5):
    lst.append(1)


def init():

    mat = []
    for row in range(SIZE):
        curr_row = []
        for col in range(SIZE):
            item = choices[rnd.randint(0, 3)]
            curr_row.append(item)
        mat.append(curr_row)
    return mat


def print_board(mat):
    for row in mat:
        for item in row:
            print(item, end=' ')
        print()


def check_row(row, item):
    for i in range(SIZE - 2):
        if row[i] == row[i + 1] and row[i] == row[i + 2] and item == row[i]:
            return True
    return False


def check_win(mat):
    for item in choices:
        for row in mat:
            if check_row(row, item):
                print(f"item {item} is three time in a row {item}")
        for col in range(SIZE):
            if check_col(mat, item, col):
                print(f"item {item} is three times in a col {col + 1}")


def check_col(board, item, col_index):
    for row in range(SIZE - 2):
        if board[row][col_index] == item and board[row + 1][col_index] == item and board[row + 2][col_index] == item:
            return True
    return False


def main():
    board = init()
    print_board(board)
    check_win(board)


main()