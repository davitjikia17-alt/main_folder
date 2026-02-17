"""



"""
def get_user_name(name3):
    list_accaunts.append(name3)
def main():
    New_accaunt = int(input("Greetings! Are you a first-time user of our ATM?\n1-New 2-Returning 3-Quit 1"))
    if New_accaunt == 1:
        register()
    if New_accaunt == 2:
        name = input("please enter your name:")
        list.append(name)
        if name in list_accaunts :
            yoour_password = input("Enter your password:")
        else:
            while name not in list_accaunts:
                print("not right ")
                name = input("please enter your name:")



def generate_password(name):
    total_character_sum = 0
    for i in range(len(name)):
        total_character_sum += ord(name[i])
    return 10000 - total_character_sum * 2


def register():
    name = input("Welcome, please enter your name:")
    password = generate_password(name)
    print(f"*****\nYour password is {password}\nDO NOT TELL ANYONE YOUR PASSWORD!\n*****")
    return name


def is_recognized(name, name_3):
    if name == '':
        return False
    if name != NAME_1 and name != NAME_2 and name != name_3:
        return False
    return True


def login(name_3):
    user_name = get_user_name(name_3)
    if user_name == LOGIN_CANCEL:
        return LOGIN_CANCEL
    if check_password(user_name) == LOGIN_FAILED:
        return LOGIN_FAILED
    else:
        return user_name


def account_operations(name):
    print("Hello " + name + ", what can we do for you?")
    choice = '0'
    while choice != '4':
        choice = input(" 1- Deposit to the account\n 2- Withdrawal from the account\n"
                       " 3- Viewing the balance\n 4- Exit")
    print("Goodbye " + name)


# ################### STAGE 3 ###################

def account_operations(name):
    print("Hello " + name + ", what can we do for you?")

    while True:
        choice = input(" 1- Deposit to the account\n 2- Withdrawal from the account\n"
                       " 3- Viewing the balance\n 4- Exit")
        if choice == '1':
            deposit = input("How much money do you want to deposit?")
            money_amount = int(deposit)
            print("Your money has been successfully deposited")

        if choice == '2':
            withdrawal = input("How much money do you want to withdraw?")
            if money_amount - int(withdrawal) < 0:
                print("You may not overdraw")
            else:
                money_amount -= int(withdrawal)
                print(withdrawal + " were withdrawn from the account")

        if choice == '3':
            print("Your balance is " + money_amount)

        if choice == '4':
            print("Goodbye " + name)
            return 0


