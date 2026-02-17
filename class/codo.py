"""
כספומט - חלק ב׳

"""
#קבועים
LOGIN_SUCCEED = 1
LOGIN_CANCEL = 0
LOGIN_FAILED = -1

#רשימות
user_account_list = ["Alice", "Bob", ""]
on_the_general_account = [2000 , 300 , 0]


def generate_password(name): #יצירת סיסמה
    total_character_sum = 0
    for i in range(len(name)):
        total_character_sum += ord(name[i])
    return 10000 - total_character_sum * 2


def register(): #התחברות
    if user_account_list[2] != "" :
        print("At maximum capacity, Can't register more people")
        return LOGIN_FAILED

    else:
        name = input("Welcome, please enter your name:")
        password  = generate_password(name)
        user_account_list[2] = name
        print(f"*****\nYour password is {password}\nDO NOT TELL ANYONE YOUR PASSWORD!\n*****")
    return    name , password


def get_user_name(): #בדיקת שם משתמש
    counter = 0
    name = input("Please enter your name: ")

    while True:
        if name in user_account_list:
            break

        print("Not recognized")
        counter += 1

        if counter == 3:
            main_y_n = input("Do you want to return to the main screen? (y/n)")

            if main_y_n.lower() == 'y':
                print("Login canceled")

                return LOGIN_CANCEL

            else:
                counter = 0

        name = input("please enter your name again: ")

    return name


def login(): # התחברות
    user_name = get_user_name()

    if user_name == LOGIN_CANCEL:
        return LOGIN_CANCEL

    if check_password(user_name) == LOGIN_FAILED:
        return LOGIN_FAILED

    return user_name


def account_operations(name): #אופציות בחשבות
    print("Hello " + name + ", what can we do for you?")

    for index in range(len(user_account_list)): #לוקח את הערך של החשבון שלך
        if name == user_account_list[index]:
            money_amount = on_the_general_account[index]
            break


    while True:
        choice = input(" 1- Deposit to the account\n 2- Withdrawal from the account\n"
                       " 3- Viewing the balance\n 4- Exit")

        if choice == '1':
            deposit = int(input("How much money do you want to deposit?"))
            money_amount += deposit
            print("Your money has been successfully deposited")

        elif choice == '2':
            withdrawal = int(input("How much money do you want to withdraw?"))

            if money_amount - withdrawal < 0:
                print("You may not overdraw")

            else:
                money_amount -= int(withdrawal)
                print(withdrawal , " were withdrawn from the account")

        elif choice == '3':
            print("Your balance is " , money_amount)

        elif choice == '4':
            print("Goodbye " + name)
            on_the_general_account[index] = money_amount
            return money_amount


def check_password(true_password): #בדיקת סיסמה
    true_password = generate_password(true_password)
    chancess = 3

    while chancess != 0:
            password = int(input("Enter your password: "))
            if password == true_password:
                return LOGIN_SUCCEED
            chancess -= 1
            if chancess == 0:
                return LOGIN_FAILED

            print(f"Wrong, you have {chancess} more tries")

    return LOGIN_FAILED


def main(): #main
    while True:
        greeting = int(input("Greetings! Are you a first-time user of our ATM?\n "
                             "1-New   2-Returning   3-Quit\n"))

        if greeting == 1:
            register()

        elif greeting == 2:
            name = login()

            if name == LOGIN_FAILED:
                print("The identification failed, the ATM shuts down")
                break

            if name != LOGIN_CANCEL:
                account_operations(name)

        elif greeting == 3:
            break
    print("See you later...")