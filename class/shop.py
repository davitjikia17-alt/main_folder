def order_room(rooms):
    order_room_list = rooms

    current = int(input(f"Enter room number: "))

    if current < 1 or current > len(order_room_list):
        current = int(input("Invalid room number, please try again: "))

        return

    if rooms[current - 1][0] < rooms[current - 1][1]:
        rooms[current - 1][0] += 1

    else:
        print("Room is already full!")

def cancel_room(rooms):

    order_room_list = rooms

    current = int(input(f"Enter room number: "))


    if current < 1 or current > len(rooms):

        currentr = int(input("Invalid room number!"))


        return

    if rooms[current - 1][0] > 0:
        rooms[current - 1][0] -= 1

    else:
        print("Room is already empty!")




def change_rooms(rooms):

    order_room_list = rooms

    print("Which room to cancel?")
    room = int(input("Enter room number: "))

    print("Which room to add?")
    too_add = int(input("Enter room number: "))


    if (room < 1 or room > len(rooms)) or (too_add < 1 or too_add > len(rooms)):
        print("Invalid room number!")

        return

    if rooms[room -1][0] == 0 :
        print("Cancelroom is already empty!")

        return

    if rooms[too_add -1][0] >= rooms[too_add - 1][1] :
        print("Added room is already full!")

        return

    rooms[room - 1][0] -= 1
    rooms[too_add - 1][0] += 1

def rooming():
    print("Welcome to the Hostel Room Management App!")
    print("Room capacity input:")

    room_list = []
    count = 1

    while True:
        room_size = [0,0]

        max_capacity = int(input(f"Room #{count}. Enter room capacity: "))

        room_size[1] = max_capacity
        room_list.append(room_size)

        y_n = input("Another room? yes / no: ")

        if y_n == "yes":
            count += 1

        else:
            break

    while True:
        choice = int(input("Enter action num: 1. order room; 2. cancel room; 3. change rooms; 4. show rooms; 99. quit "))

        if choice == 1:
            order_room(room_list)

        elif choice == 2:
            cancel_room(room_list)


        elif choice == 3:
            change_rooms(room_list)


        elif choice == 4:
            for i in range(len(room_list)):
                print(f"Room #{1 + i}: {room_list[i][0]} / {room_list[i][1]}")



        elif choice == 99:
            print("Bye bye!")


            break

        else:
            choice = int(input("Wrong action num, try again: "))

def main():
    rooming()



main()
