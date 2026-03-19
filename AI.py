import fuzzywuzzy as fuzz



def welcome_message(text):
    welcome = ["hi","gamarjoba","hello",]







def change_turn(current):
    if current == "guest":
        return "bot"
    return "guest"






def main():
    current = "guest"
    text = []

    print("Welcome to AI ")
    while True:
        if current == "guest":
            guest = input("Enter: ")
            text.append(guest)
            change_turn(current)

        elif current == "bot":





if __name__ == "__main__":
    main().run()