import random as rnd

SIZE = 7
choice = ["X", "O", "Z", "Y", "U", "$", "J"]

def init():

    mat = []
    for row in range(SIZE):
        curr_row = []

        for col in range(SIZE):
            item = rnd.choice(choice)
            curr_row.append(item)

        mat.append(curr_row)

    return mat


def draw(mat):
    for row in mat:
        for col in row:
            print(col, end="  ")
        print()


def check_row(row, item):
    for i in range (SIZE - 2):
        if row[i] == item and row[i + 1] == item and row[i + 2] == item:
            return True
    return False


def check_col(mat, item, col):
    for row in range(SIZE - 2):
        if mat[row][col] == item and mat[row + 1][col] == item and mat[row + 2][col] == item:
            return True

    return False


def check_win(mat):

    for simbol in choice:

        # check rows
        for i in range(SIZE):
            row = mat[i]
            if check_row(row, simbol):
                print(f"row {i + 1} wins! Symbol {simbol}!")

        # check columns
        for col in range(SIZE):
            if check_col(mat, simbol, col):
                print(f"col {col + 1} wins! Symbol {simbol}!")


def main():
    mat = init()
    draw(mat)
    check_win(mat)



if __name__ == "__main__":
    main()