def gender(a,b):
    if a == "female" and b == "male":
        return "V"
    elif a == "male" and b == "male":
        return "M"
    return "f"

def main():
    count_f = 0
    count_m = 0
    for i in range(1371):
        a = input("Enter a gender: ")
        b = input("Enter another gender: ")
        a,b = gender(a,b)
        if a == "f" or b == "f":
            count_f += 1
        if a == "m" or b == "m":
            count_m += 1

    if count_f > count_m:
        print("female")
    if count_m > count_f:
        print("male")
    else:
        print("equal")

main()


