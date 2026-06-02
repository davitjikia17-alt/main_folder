from fuzzywuzzy import fuzz



def numbers_bin(text):

    if text == 0:
        return [0]

    binary = []

    while text != 0 :
        binary.append(text % 2)
        text = text // 2

    return binary[::-1]


def numbers_oct(text):
    if text == 0:
        return [0]

    octal = []
    while text > 0 :
        octal.append(text % 8)
        text = text // 8

    return octal[::-1]


def numbers_hex(text:int):

    if text == 0:
        return [0]

    hexadecimal = []
    hex_sing = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
        5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
        10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    }

    while text > 0 :
        num = text % 16

        hexadecimal.append(hex_sing[num])
        text = text // 16

    #bruh now i am alfa
    return hexadecimal[::-1]


def print_bin(text):

    print("BINARY | DEX")
    numbers_bin(text)

    for i in numbers_bin(text):
        print(i, end="")

    print(" = ", text)
    print()
    print()


def print_oct(text):

    print("OCAT | DEX")
    numbers_hex(text)

    for i in numbers_oct(text):
        print(i, end="")

    print(" = ", text)
    print()
    print()


def print_hex(text):

    print("HEXADECIMAL | DEX")
    numbers_hex(text)

    for i in numbers_hex(text):
        print(i, end="")

    print(" = ", text)
    print()
    print()


def options():
    while True:
        options = input("In which library would you like to translate numbers?"
                        "\nBinary | Hexadecimal | Octal ??? ")

        if options.lower() == "binary":
            return "binary"

        elif options.lower() == "hexadecimal":
            return "hexadecimal"

        elif options.lower() == "octal":
            return "octal"

        else:
            print("broo"*999)


def main():

    while True:
        option = options()

        print()
        print()

        text = int(input("Enter a number: "))

        if option == "binary":
            print_bin(text)

        elif option == "hexadecimal":
            print_hex(text)

        elif option == "octal":
            print_oct(text)

        y_n = input("Do you want to continue? (y/n): ")

        if y_n.lower() == "y" or y_n.lower() == "n":
            if  y_n.lower() == "n":
                break

        else:
            print("bruh what the actual sigma wolf fuck? ")

    print("never trust no one in virtual sociality!")


if __name__ == "__main__":
    main()