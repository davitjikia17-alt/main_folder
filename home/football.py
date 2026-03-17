import random


def create_soccer_ground():

    ground = []
    for i in range (2):
        row = []
        ground.append(row)
        for j in range (2):
            row.append(" ")

    return ground


def print_ground(ground):

    print("  ------")
    for row in range (len(ground)):
        print("| " , ground[row][0],ground[row][1] , " |")
    print("  ------")


def get_player_choice():

    choice_list = ["UL" , "UR" , "DL" , "DR"]
    while True:
        player_choice = input("which way do you want to kick a ball? ")


        if player_choice not in choice_list:
            print(f"Invalid input. Use one of them : {choice_list}.")
            continue

        if player_choice == "UL":
            row = 0
            col = 0

        if player_choice == "UR":
            row = 0
            col = 1

        if player_choice == "DL":
            row = 1
            col = 0

        if player_choice == "DR":
            row = 1
            col = 1

        return row, col


def get_goalkeeper_choice():

    gk_row = random.randint(0,1)
    gk_col = random.randint(0,1)

    return gk_row, gk_col


def main():
    score_list = []
    ball = "O"
    goalkeeper = "G"

    print("Welcome to Soccer game")
    gamers = input("would you like to play custom? y/n ")

    if gamers.lower() == "y":
        play = int(input("enter how many players would you like to play: "))
        tries = int(input("enter how many tries for players: "))

    else:
        play = 1
        tries = 1

    for i in range(1 , play+1):
        score = 0
        for j in range(1 , tries+1):
            ground = create_soccer_ground()

            print(f"-PLAYER 0{i}-")
            print_ground(ground)

            player_row , player_col = get_player_choice()
            gk_row , gk_col = get_goalkeeper_choice()

            if player_row == gk_row and player_col == gk_col:
                ground[player_row][player_col] = "O/G"
            else:
                ground[player_row][player_col] = "O"
                ground[gk_row][gk_col] = "G"

            print_ground(ground)

            if player_row == gk_row and player_col == gk_col:
                print("SAVE! The goalkeeper stopped your ball!")


            else:
                print("GOAL! Well done!")
                score += 1
        score_list.append(score)
        print(f"\nGame over for player {i}! Your total score: {score}")
    print("\nGame over!")
    y_n = input("would you like to see scores? y/n ")

    if y_n.lower() == "y":
        for i in range(len(score_list)):
            print(f"-player 0{i + 1}- score : {score_list[i-1]}")
        print("\nGood Game!")


main()










