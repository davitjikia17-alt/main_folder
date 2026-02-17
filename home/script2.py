student = {}
player= ["Front", "Back", "Right", "Left", "Up", "Down"]

for play in player:
    while True:
        place = input(f" place: ")
        if len(place) == 9 :
            student[player] = [place[0:3] , place[3:6] , place[6:9]]

            break


print(student)

