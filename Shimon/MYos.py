import random as rnd

SIZE = 5
choice = ["X", "O", "Z", "Y", "U", "$", "J"]

def random_matrix():

    mat = []

    for i in range(SIZE):
        row = []

        for j in range(SIZE):
            simbol = rnd.choice(choice)
            row.append(simbol)

        mat.append(row)

    return mat


def printing_mat(mat):

    for row in mat:
        for simbol in row:
            print(simbol, end="  ")
        print()


def check_row(row, simbol):

    for i in range (SIZE - 2) :
        if row[i] == simbol and row[i + 1] == simbol and row[i + 2] == simbol:
            return True
    return False


def check_col(mat, simbol, col):

    for row in range(SIZE - 2):
        if mat[row][col] == simbol and mat[row + 1][col] == simbol and mat[row + 2][col] == simbol:

            return True

    return False


def check_win(mat):
    for simbol in choice:
        for row in simbol:
            if check_row(mat, simbol):
                print(f"row {row} wins! Simbol {simbol} !")

        for col in range(SIZE):
            if check_col(mat, simbol, col):
                print(f"col {col} wins! Simbol {simbol} !")


def main():
    mat = random_matrix()
    printing_mat(mat)
    check_win(mat)


if __name__ == "__main__":
    main()