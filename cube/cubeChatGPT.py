def create_cube():

    W = "w" #wite
    G = "g" #green
    R = "r" #red
    Y = "y" #yellow
    O = "o" #orange
    B = "b" #blue

    side1 = input(f"   up{W} {W} {W}\n   {W} {W} {W}\n   {W} {W} {W}")*3
    side2 = input(f"   front{G} {G} {G}\n   {G} {G} {G}\n   {G} {G} {G}")*3
    side3 = input(f"   back{R} {R} {R}\n   {R} {R} {R}\n   {R} {R} {R}")*3
    side4 = input(f"   down{Y} {Y} {Y}\n   {Y} {Y} {Y}\n   {Y} {Y} {Y}")*3
    side5 = input(f"   left{O} {O} {O}\n   {O} {O} {O}\n   {O} {O} {O}")*3
    side6 = input(f"   right{B} {B} {B}\n   {B} {B} {B}\n   {B} {B} {B}")*3

    W, Y, G, B, R, O = "w", "y", "g", "b", "r", "o"
    return {
        "Up":    [[W]*3 for _ in range(3)],
        "Down":  [[Y]*3 for _ in range(3)],
        "Front": [[G]*3 for _ in range(3)],
        "Back":  [[B]*3 for _ in range(3)],
        "Left":  [[R]*3 for _ in range(3)],
        "Right": [[O]*3 for _ in range(3)]
    }

def create_solved_cube():

    W = "w" #wite
    G = "g" #green
    R = "r" #red
    Y = "y" #yellow
    O = "o" #orange
    B = "b" #blue

    side1 = (f"   {W} {W} {W}\n   {W} {W} {W}\n   {W} {W} {W}")
    side2 = (f"   {G} {G} {G}\n   {G} {G} {G}\n   {G} {G} {G}")
    side3 = (f"   {R} {R} {R}\n   {R} {R} {R}\n   {R} {R} {R}")
    side4 = (f"   {Y} {Y} {Y}\n   {Y} {Y} {Y}\n   {Y} {Y} {Y}")
    side5 = (f"   {O} {O} {O}\n   {O} {O} {O}\n   {O} {O} {O}")
    side6 = (f"   {B} {B} {B}\n   {B} {B} {B}\n   {B} {B} {B}")

    W, Y, G, B, R, O = "w", "y", "g", "b", "r", "o"
    return {
        "Up":    [[W]*3 for _ in range(3)],
        "Down":  [[Y]*3 for _ in range(3)],
        "Front": [[G]*3 for _ in range(3)],
        "Back":  [[B]*3 for _ in range(3)],
        "Left":  [[R]*3 for _ in range(3)],
        "Right": [[O]*3 for _ in range(3)]
    }

def rotate_clockwise(side):
    return [[side[2-j][i] for j in range(3)] for i in range(3)]

# ფუნქციები ყველა ტრიალისთვის (F, B, U, D, L, R)
def rotate_front(cube):

    # 1) Front მხარის მობრუნება
    cube["Front"] = rotate_clockwise(cube["Front"])

    # 2) Up ქვედა ხაზის შენახვა
    temp = cube["Up"][2][:]

    # 3) Left → Up
    for i in range(3):
        cube["Up"][2][i] = cube["Left"][2 - i][2]

    # 4) Down → Left
    for i in range(3):
        cube["Left"][i][2] = cube["Down"][0][i]

    # 5) Right → Down
    for i in range(3):
        cube["Down"][0][i] = cube["Right"][2 - i][0]

    # 6) temp → Right
    for i in range(3):
        cube["Right"][i][0] = temp[i]

def rotate_back(cube):
    cube["Back"] = rotate_clockwise(cube["Back"])
    Up_row = cube["Up"][0].copy()
    Right_col = [cube["Right"][i][2] for i in range(3)]
    Down_row = cube["Down"][2].copy()
    Left_col = [cube["Left"][i][0] for i in range(3)]
    cube["Up"][0] = Right_col[::-1]
    for i in range(3):
        cube["Right"][i][2] = Down_row[i]
    cube["Down"][2] = Left_col[::-1]
    for i in range(3):
        cube["Left"][i][0] = Up_row[i]

def rotate_up(cube):
    cube["Up"] = rotate_clockwise(cube["Up"])
    Front_row = cube["Front"][0].copy()
    Right_row = cube["Right"][0].copy()
    Back_row = cube["Back"][0].copy()
    Left_row = cube["Left"][0].copy()
    cube["Front"][0] = Right_row
    cube["Right"][0] = Back_row
    cube["Back"][0] = Left_row
    cube["Left"][0] = Front_row

def rotate_down(cube):
    cube["Down"] = rotate_clockwise(cube["Down"])
    Front_row = cube["Front"][2].copy()
    Right_row = cube["Right"][2].copy()
    Back_row = cube["Back"][2].copy()
    Left_row = cube["Left"][2].copy()
    cube["Front"][2] = Left_row
    cube["Right"][2] = Front_row
    cube["Back"][2] = Right_row
    cube["Left"][2] = Back_row

def rotate_left(cube):
    cube["Left"] = rotate_clockwise(cube["Left"])
    Up_col = [cube["Up"][i][0] for i in range(3)]
    Front_col = [cube["Front"][i][0] for i in range(3)]
    Down_col = [cube["Down"][i][0] for i in range(3)]
    Back_col = [cube["Back"][2-i][2] for i in range(3)]
    for i in range(3):
        cube["Up"][i][0] = Back_col[i]
        cube["Front"][i][0] = Up_col[i]
        cube["Down"][i][0] = Front_col[i]
        cube["Back"][2-i][2] = Down_col[i]

def rotate_right(cube):
    cube["Right"] = rotate_clockwise(cube["Right"])
    Up_col = [cube["Up"][i][2] for i in range(3)]
    Front_col = [cube["Front"][i][2] for i in range(3)]
    Down_col = [cube["Down"][i][2] for i in range(3)]
    Back_col = [cube["Back"][2-i][0] for i in range(3)]
    for i in range(3):
        cube["Up"][i][2] = Front_col[i]
        cube["Front"][i][2] = Down_col[i]
        cube["Down"][i][2] = Back_col[2-i]
        cube["Back"][2-i][0] = Up_col[i]

def print_cube(cube):
    Up, Down = cube["Up"], cube["Down"]
    Front, Back = cube["Front"], cube["Back"]
    Left, Right = cube["Left"], cube["Right"]

    print("\n       Up")
    for row in Up:
        print("      ", end="")
        for c in row:
            print(c, end=" ")
        print()
    print()

    print("Left     Front     Right     Back")
    for i in range(3):
        for side in [Left, Front, Right, Back]:
            for c in side[i]:
                print(c, end=" ")
            print("   ", end="")
        print()
    print()

    print("      Down")
    for row in Down:
        print("      ", end="")
        for c in row:
            print(c, end=" ")
        print()
    print()

# --------- გამოყენება ---------
cube = create_solved_cube()
print("კუბის საწყისი მდგომარეობა:")
print_cube(cube)
moves = ["F", "R", "U", "L", "D", "B", "F", "R"]
for move in moves:
    if move == "F" :
        rotate_front(cube)

    elif move == "B":
        rotate_back(cube)

    elif move == "U" :
        rotate_up(cube)

    elif move == "D":
        rotate_down(cube)

    elif move == "L":
        rotate_left(cube)
    elif move == "R":
        rotate_right(cube)

print(f"კუბის მდგომარეობა ტრიალის შემდეგ:")
print_cube(cube)
print(create_cube())

