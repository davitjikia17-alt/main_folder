def create_solved_cube():

    W = "w" #white
    G = "g" #green
    R = "r" #red
    Y = "y" #yellow
    O = "o" #orange
    B = "b" #blue

    W, Y, G, B, R, O = "w", "y", "g", "b", "r", "o"
    return {                    #returns solved cube's list for side
        "Up": [[W] * 3 for _ in range(3)],
        "Down": [[Y] * 3 for _ in range(3)],
        "Front": [[G] * 3 for _ in range(3)],
        "Back": [[B] * 3 for _ in range(3)],
        "Right": [[R] * 3 for _ in range(3)],
        "Left": [[O] * 3 for _ in range(3)]
    }


def create_your_cube():
    cube = {}
    #sides of cube
    sides = ["Front", "Back", "Right", "Left", "Up", "Down"]

    #prints sides , lines of side and colors of lines
    for side in sides:
        colors = []
        #sides's colors
        print(f"{side}'s 9 colors | wite = w |green = g |red = r |yellow = y |orange = o |blue = b|")
        for i in range(1,10):
            color = input(f"side({side}) ({i} colors): ")
            colors.append(color)
        cube[side] = [colors[0:3],colors[3:6],colors[6:9]]

    return cube


def rotate_clockwise(side):
    new_side = [[None] * 3 for _ in range(3)]

    # rotates clockwise
    for n in range(3):
        for l in range(3):
            new_side[l][2 - n] = side[n][l]

    return new_side


def rotate_counterclockwise(side):
    new_side = [[None] * 3 for _ in range(3)]

    #rotates counterclockwise
    for n in range(3):
        for l in range(3):
            new_side[2 - l][n] = side[n][l]

    return new_side


def rotate_middle_front_counterclockwise(cube):
    # up's mid lines
    temp = [cube["Up"][i][1] for i in range(3)]

    # Right to Up
    for i in range(3):
        cube["Up"][i][1] = cube["Right"][2 - i][1]

    # Down to Right
    for i in range(3):
        cube["Right"][2 - i][1] = cube["Down"][i][1]

    # Left to Down
    for i in range(3):
        cube["Down"][i][1] = cube["Left"][2 - i][1]

    # temp to Left
    for i in range(3):
        cube["Left"][2 - i][1] = temp[i]


def rotate_front(cube):

    # 1) side Front's rotation
    cube["Front"] = rotate_clockwise(cube["Front"])

    # 2) saving Up side
    temp = cube["Up"][2][:]

    # 3) Left to Up
    for i in range(3):
        cube["Up"][2][i] = cube["Left"][2 - i][2]

    # 4) Down to Left
    for i in range(3):
        cube["Left"][i][2] = cube["Down"][0][i]

    # 5) Right to Down
    for i in range(3):
        cube["Down"][0][i] = cube["Right"][2 - i][0]

    # 6) temp to Right
    for i in range(3):
        cube["Right"][i][0] = temp[i]


def rotate_up(cube):

    # 1) side Up's rotation
    cube["Up"] = rotate_clockwise(cube["Up"])

    # 2) saving front side
    temp = cube["Front"][0][:]

    # 3) Left to Front
    for i in range(3):
        cube["Front"][0][i] = cube["Left"][0][i]

    # 4) Back to Left
    for i in range(3):
        cube["Left"][0][i] = cube["Back"][0][i]

    # 5) Right to Back
    for i in range(3):
        cube["Back"][0][i] = cube["Right"][0][i]

    # 6) temp to Right
    for i in range(3):
        cube["Right"][0][i] = temp[i]


def rotate_down(cube):

    # side down's rotation
    cube["Down"] = rotate_clockwise(cube["Down"])

    # saving front side
    temp = cube["Front"][2][:]

    # right to front
    for i in range(3):
        cube["Front"][2][i] = cube["Right"][2][i]

    # back to right
    for i in range(3):
        cube["Right"][2][i] = cube["Back"][2][i]

    # left to back
    for i in range(3):
        cube["Back"][2][i] = cube["Left"][2][i]

    # temp to left
    for i in range(3):
        cube["Left"][2][i] = temp[i]


def rotate_left(cube):

    # side left's rotation
    cube["Left"] = rotate_clockwise(cube["Left"])

    # saving up side
    temp = [cube["Up"][i][0] for i in range(3)]

    # front to up
    for i in range(3):
        cube["Up"][i][0] = cube["Front"][i][0]

    # down to front
    for i in range(3):
        cube["Front"][i][0]= cube["Down"][i][0]

    # back to down
    for i in range(3):
        cube["Down"][i][0] = cube["Back"][2 - i][2]

    # temp to back
    for i in range(3):
        cube["Back"][2 - i][2] = temp[i]


def rotate_right(cube):

    # side right's rotation
    cube["Right"] = rotate_clockwise(cube["Right"])

    # saving up side
    temp = [cube["Up"][i][2] for i in range(3)]

    # front to up
    for i in range(3):
        cube["Up"][i][2] = cube["Front"][i][2]

    # down to front
    for i in range(3):
        cube["Front"][i][2] = cube["Down"][i][2]

    # back to down
    for i in range(3):
        cube["Down"][i][2] = cube["Back"][2 - i][0]

    # temp to back
    for i in range(3):
        cube["Back"][2 - i][0] = temp[i]


def rotate_back(cube):

    # 1) side Back's rotation
    cube["Back"] = rotate_counterclockwise(cube["Back"])

    # 2) saving up's side
    temp = cube["Up"][0][:]

    # 3) Left to Up
    for i in range(3):
        cube["Up"][0][i] = cube["Left"][2 - i][0]

    # 4) Down to Left
    for i in range(3):
        cube["Left"][2 - i][0] = cube["Down"][2][2 - i]

    # 5) Right to Down
    for i in range(3):
        cube["Down"][2][2 - i] = cube["Right"][2 - i][2]

    # 6) temp to Right
    for i in range(3):
        cube["Right"][2 - i][2] = temp[i]


def printing_cube(cube):

    Up = cube["Up"]
    Down = cube["Down"]
    Front = cube["Front"]
    Back = cube["Back"]
    Left = cube["Left"]
    Right = cube["Right"]

    print("\n               Up")
    for line1 in Up:
        print("           ", end=" ")
        for color1 in line1:
            print("", color1, end=" ")
        print()
    print()

    print("\n   Left       Front       Right        Back")
    for side in range(3):
        for line2 in [Left, Front, Right, Back]:
            for color2 in line2[side]:
                print("", color2, end=" ")
            print("   ", end="")
        print()
    print()

    print("\n              Down")
    for line3 in Down:
        print("           ", end=" ")
        for color3 in line3:
            print("", color3, end=" ")
        print()
    print()



def main():
    cube = create_solved_cube()
    #3your_cube = create_your_cube()

    print("solved cube:")
    printing_cube(cube)

    while True:

        #print("your cube:")
        #printing_cube(your_cube)
        print("solved cube:")
        printing_cube(cube)

        actions = int(input("what would you like to do??"
                            "\n1 | rotation left "
                            "\n2 | rotation right "
                            "\n3 | rotation up"
                            "\n4 | rotation down"
                            "\n5 | rotation front"
                            "\n6 | rotation back "
                            "\n7 | exit"
                            "\nEnter:"))

        if actions == 1:
            rotate_left(cube)

        if actions == 2:
            rotate_right(cube)

        if actions == 3:
            rotate_up(cube)

        if actions == 4:
            rotate_down(cube)

        if actions == 5:
            rotate_front(cube)

        if actions == 6:
            rotate_back(cube)

        if actions == 7:
            break


    print("nice one !")





main()