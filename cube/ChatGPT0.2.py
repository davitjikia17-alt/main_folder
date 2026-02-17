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

    return cube


def rotate_up(cube):

    pass


def rotate_down(cube):

    pass


def rotate_left(cube):

    pass


def rotate_right(cube):

   pass


def rotate_back(cube):
    pass


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
    your_cube = create_your_cube()
    rotation_clockwise = rotate_clockwise(your_cube)

    print("solved cube:")
    printing_cube(cube)

    print("your cube:")
    printing_cube(your_cube)




main()