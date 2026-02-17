def room_capacity():
    room_list = []
    count = 1


    while True:
        room_size = [0,0]

        max_capacity = int(input(f"Room #{count}. Enter room capacity: "))

        room_size[1] += max_capacity
        room_list.append(room_size)

        y_n = input("Another room? yes / no: ")

        if y_n == "yes":
            count += 1

        else:
            break

    return room_list



order_room_list = [[0,0],[0,0]]

current = int(input(f"Enter room number: "))

for k in range (len(order_room_list[current - 1])):
    if k == current - 1:
        order_room_list[current - 1][1] += 1
        break
print(order_room_list)
