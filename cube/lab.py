side = [ ["1", "2", "3"] , ["4", "5", "6"] , ["7", "8", "9"] ]

new_side = [[None] * 3 for _ in range(3)]

print(new_side)


for n in range(3):
    print(side[n])
    for l in range(3):
        new_side[l][2 - n] = side[n][l]


print(side)
print("new side :")
print(new_side)



def rotate_counterRight(cube):
    rotate_right(cube)
    rotate_right(cube)
    rotate_right(cube)


def rotate_counterLeft(cube):
    rotate_left(cube)
    rotate_left(cube)
    rotate_left(cube)


def rotate_counterUp(cube):
    rotate_up(cube)
    rotate_up(cube)
    rotate_up(cube)


def rotate_counterDown(cube):
    rotate_down(cube)
    rotate_down(cube)
    rotate_down(cube)


def rotate_counterFront(cube):
    rotate_front(cube)
    rotate_front(cube)
    rotate_front(cube)


def rotate_counterBack(cube):
    rotate_back(cube)
    rotate_back(cube)
    rotate_back(cube)
