import random as rnd








def main():
    num = int(rnd.randint(1, 100))
    trys = 0
    while trys != 5 :
        player = int(input("try to guess number from 1 to 100:"))
        if player == num:
            print("well done!!!")
            break
        else:
            trys += 1

    print(num)

if __name__ == "__main__":
    main()
