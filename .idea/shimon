def result_board(game_list):

    for i in range(len(game_list)):
        if 0 < game_list[i][1]:
            print(f"{game_list[i][0]} | score ", game_list[i][1])

        else:
            print(f"{game_list[1][0]} have lost a game !")


def turns(game_list , i):

    if i == len(game_list)-1:
        return 0

    return i + 1


def check_zero(game_list):

    zero_count = 0

    for i in range(len(game_list)):

        if 0 == game_list[i][1]:
            zero_count += 1

        if zero_count == len(game_list) - 1:
            return False

    return True


def welcome():

    print("wellcome to the game !")

    while True:
        start = input("Have you played this game before ? y/n")

        if start.lower() != "y" and start.lower() != "n":
            print("broooooo what the hell ? ")

        else :
            break

    if start.lower() == "n":

        print("rules:"
              "\nIn this game you can play with your friend! "
              "\nAll players have 3 points , then after one other, says the act he/she hasn't done. "
              "\nIf you ever done that 'act' you get minus point."
              "\nGame ends after all rounds are done!"
              "\nWinner will be who will remain most points in the game!!!  GOOD LUCK !!! \n")


def winner(game_list):
    point = 0

    for i in range(len(game_list)):

        if point <= game_list[i][1]:
            point = game_list[i][1]
            winner = game_list[i][0]

    return winner



def game_settings(play , round ):


    while True:
        custom = input("would you like to play custom game ? y/n")

        if custom.lower() == "y":
            play = int(input("enter how many players would you like to play: "))
            round = int(input("enter how many rounds in total: "))

            print()
            print("total players will be:",play)
            print("total round will be:",round)
            print()
            break



        elif custom.lower() == "n":
            print("total players will be:",play)
            print("total round will be:",round)
            break

        else:
            print("bro ar u damn ass ? just yes or no ")

    return play , round


def main():
    game_list = []
    score = 3
    play = 2
    round = 1

    welcome()

    play , round = game_settings(play, round)

    for i in range(1 , play + 1):
        game_list.append([input(f"enter 0{i}player's name:"), score])


    count = 0

    while round != 0 and check_zero(game_list) == True :
        count += 1
        round -=1
        print("round:",count )

        for i in range(len(game_list)):
            turn = turns(game_list , i)
            question = input(f"#{game_list[i][0]} | please enter act you've not done (score {game_list[i][1]}):\n")
            answer = input(f"#{game_list[turn][0]} | {question} ?Have you done ? y/n \n")

            if answer.lower() == "y":
                game_list[turn][1] -= 1

        print()
        print()
        print(f"round0{count} results:")
        result_board(game_list)
        print()
        print()

    print(f"winner of the game is: {winner(game_list)}")




main()
